from .distance import calculate_distance
from .severity import sort_by_severity


def allocate(patient, ambulances, hospitals):
    """Allocate the nearest available ambulance and a suitable hospital for one patient.

    Returns a tuple (ambulance_id, hospital_id) or None if allocation failed.
    """
    available = [a for a in ambulances if a.get("available", True)]
    if not available:
        return None

    # Prioritize ambulances with IV supplies if patient requires IV
    iv_required = patient.get("iv_required", False)
    ambulance = min(
        available,
        key=lambda a: (
            0 if a.get("iv_supplies", False) == iv_required else 1,  # Prefer matching IV capability
            calculate_distance(a["location"], patient["location"])
        )
    )

    suitable = []
    for h in hospitals:
        if h.get("capacity", 0) <= 0:
            continue
        if patient.get("severity") == "Critical" and not h.get("icu", False):
            continue
        suitable.append(h)

    if not suitable:
        return None

    # Prioritize hospitals with needed organ if patient needs one
    needed_organ = patient.get("needs_organ")
    hospital = min(
        suitable,
        key=lambda h: (
            0 if needed_organ and needed_organ in h.get("organs", []) else 1,  # Prefer hospitals with organ
            calculate_distance(h["location"], patient["location"])
        )
    )

    # Update status
    ambulance["available"] = False
    hospital["capacity"] = hospital.get("capacity", 1) - 1

    return ambulance["id"], hospital["id"]


def allocate_all(patients, ambulances, hospitals):
    """Allocate resources for a list of patients, returns list of results.

    Each result is a dict: {"patient": id, "ambulance": id|None, "hospital": id|None}
    """
    results = []
    ordered = sort_by_severity(patients)

    for p in ordered:
        res = allocate(p, ambulances, hospitals)
        if res:
            amb_id, hosp_id = res
            results.append({"patient": p["id"], "ambulance": amb_id, "hospital": hosp_id})
        else:
            results.append({"patient": p["id"], "ambulance": None, "hospital": None})

    return results
