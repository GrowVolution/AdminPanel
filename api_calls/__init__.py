from packaging import Package

from pathlib import Path

CALLS = Package(Path(__file__).parent)


def status(window, response) -> bool:
    success = response.get('success', False)
    if not success:
        window.show_status(f"Fehler beim Ausführen der Aktion: {response.get('error', 'Unbekannter Fehler.')}.", 'error')

    return success
