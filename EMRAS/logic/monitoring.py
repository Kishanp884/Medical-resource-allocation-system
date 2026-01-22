def check_iv_alerts(patients):
    """Check for IV drip alerts: low remaining time or abnormal flow rate."""
    alerts = []
    for p in patients:
        if p.get("iv_status") == "active":
            remaining = p.get("iv_remaining_time", 0)
            flow = p.get("iv_flow_rate", 0)
            if remaining < 30:  # Alert if less than 30 minutes
                alerts.append(f"IV for patient {p['id']} is about to finish ({remaining} min left)")
            if flow < 20 or flow > 100:  # Abnormal flow rate
                alerts.append(f"Abnormal IV flow rate for patient {p['id']}: {flow} ml/hr")
    return alerts

def check_organ_alerts(organs):
    """Check for organ viability alerts."""
    alerts = []
    for o in organs:
        temp = o.get("temperature", 4.0)
        transport = o.get("transport_time", 0)
        preservation = o.get("preservation_duration", 0)
        if temp > 6.0 or temp < 2.0:
            alerts.append(f"Organ {o['id']} temperature out of range: {temp}°C")
        if transport > preservation:
            alerts.append(f"Organ {o['id']} transport time exceeded preservation duration")
        if not o.get("viable", True):
            alerts.append(f"Organ {o['id']} is no longer viable")
    return alerts

def update_organ_status(organs, time_elapsed=10):
    """Simulate time passing and update organ status."""
    for o in organs:
        o["transport_time"] += time_elapsed
        # Simulate temperature fluctuation
        o["temperature"] += (0.1 if o["transport_time"] % 20 == 0 else 0)
        if o["transport_time"] > o["preservation_duration"] or o["temperature"] > 6.0:
            o["viable"] = False

def update_iv_status(patients, time_elapsed=10):
    """Simulate IV drip usage."""
    for p in patients:
        if p.get("iv_status") == "active" and p.get("iv_remaining_time"):
            p["iv_remaining_time"] = max(0, p["iv_remaining_time"] - time_elapsed)
            if p["iv_remaining_time"] == 0:
                p["iv_status"] = "finished"