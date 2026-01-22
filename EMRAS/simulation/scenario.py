from ..logic.severity import sort_by_severity
from ..logic.allocator import allocate_all
from ..data.ambulances import ambulances
from ..data.hospitals import hospitals
from ..data.patients import patients
from ..ui.display import show_header, show_result


def run_simulation():
    show_header()

    # Copy data structures so the originals in data/ are mutated during simulation
    # (they are simple lists of dicts and this keeps state obvious for demo.)
    results = allocate_all(patients, ambulances, hospitals)

    for r in results:
        show_result(r)


if __name__ == "__main__":
    run_simulation()
