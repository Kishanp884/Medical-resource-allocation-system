from flask import Flask, render_template, jsonify
import copy

# Use package-relative imports so running with `-m EMRAS.web.app` works
from ..data.ambulances import ambulances as _AMB
from ..data.hospitals import hospitals as _HOS
from ..data.patients import patients as _PAT
from ..data.organs import organs as _ORG
from ..logic.allocator import allocate_all
from ..logic.monitoring import check_iv_alerts, check_organ_alerts, update_iv_status, update_organ_status

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/allocate", methods=["GET", "POST"])
def api_allocate():
    # use deep copies so repeated calls behave like fresh scenarios
    ambulances = copy.deepcopy(_AMB)
    hospitals = copy.deepcopy(_HOS)
    patients = copy.deepcopy(_PAT)

    results = allocate_all(patients, ambulances, hospitals)

    return jsonify({"results": results, "ambulances": ambulances, "hospitals": hospitals})


@app.route("/api/status")
def api_status():
    # Update IV and organ status before returning
    update_iv_status(_PAT)
    update_organ_status(_ORG)
    
    return jsonify({
        "patients": _PAT,
        "ambulances": _AMB,
        "hospitals": _HOS,
        "organs": _ORG
    })


@app.route("/api/alerts")
def api_alerts():
    iv_alerts = check_iv_alerts(_PAT)
    organ_alerts = check_organ_alerts(_ORG)
    
    return jsonify({
        "iv_alerts": iv_alerts,
        "organ_alerts": organ_alerts
    })


@app.route("/api/update_simulation", methods=["POST"])
def api_update_simulation():
    # Update all dynamic data
    update_iv_status(_PAT)
    update_organ_status(_ORG)
    
    return jsonify({"status": "updated"})


@app.route("/organs")
def organs_dashboard():
    return render_template("organs.html")


@app.route("/iv-monitoring")
def iv_monitoring_dashboard():
    return render_template("iv_monitoring.html")


@app.route("/allocation")
def allocation_dashboard():
    return render_template("allocation.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
