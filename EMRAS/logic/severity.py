priority = {
    "Critical": 1,
    "Serious": 2,
    "Moderate": 3,
    "Minor": 4
}


def sort_by_severity(patients):
    """Return patients sorted by priority (low number = higher priority)."""
    return sorted(patients, key=lambda x: priority.get(x.get("severity"), 99))


def classify_severity(score):
    """Simple helper to classify a numeric score into severity labels.

    This is a tiny helper for simulations where you might derive severity
    from a vitals score. Lower score => more severe.
    """
    if score <= 3:
        return "Critical"
    if score <= 6:
        return "Serious"
    if score <= 8:
        return "Moderate"
    return "Minor"
