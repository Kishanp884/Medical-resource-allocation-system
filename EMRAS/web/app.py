from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

BACKEND_URL = "http://127.0.0.1:8000"  # FastAPI backend

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/iv")
def iv():
    return render_template("iv.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

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
