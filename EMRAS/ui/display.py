def show_header():
    print("Emergency Medical Resource Allocation System\n")


def show_result(result):
    pid = result.get("patient")
    aid = result.get("ambulance")
    hid = result.get("hospital")

    if aid and hid:
        print(f"Patient {pid} → Ambulance {aid} → Hospital {hid}")
    else:
        print(f"Patient {pid} → No resources available")
