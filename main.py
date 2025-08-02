from app import MainWindow
from app.loading_screen import show_loading_screen, loading_message, update_progress
from events import EVENTS
from threads import THREADS
from app.widgets import WIDGETS
from app.dialogs import DIALOGS
from dispatcher import init_dispatcher
from utils import wait
from socket_client import setup_handling
from debugger import log, set_loglevel

from PySide6.QtWidgets import QApplication
import sys, argparse, os

_loading_steps = []
_args = None
_debug = False
APP = None
WINDOW = None


def _step(func):
    _loading_steps.append(func)
    return func


@_step
def parse_args():
    global _args
    loading_message("Verarbeite Startargumente...")
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug mode.")
    parser.add_argument("--backend", "-b", type=str, default="default", help="Set the panels backend.")
    _args = parser.parse_args()

@_step
def process_args():
    global _debug
    _debug = _args.debug
    log('info', f"App is running in {'debug' if _debug else 'productive'} mode.")
    loading_message(f"App läuft im {'Debugmodus' if _debug else 'produktiven Modus'}.")
    set_loglevel(_debug)
    wait()

    os.environ['BACKEND'] = _args.backend
    backend = os.getenv('BACKEND') if os.getenv('BACKEND') !=  "default" else "standard Backend"
    log('info', f"Using backend: {os.getenv('BACKEND')}")
    loading_message(f"Verwende Backend: {backend}...")

@_step
def update_ui():
    if _debug:
        from qt_ui import compile_ui
        log('info', "Compiling UI templates...")
        loading_message("Aktualisiere Benutzeroberfläche...")
        compile_ui()

@_step
def init_packages():
    log('info', "Initializing packages...")
    loading_message("Initialisiere Pakete...")
    EVENTS.initialize()
    THREADS.initialize()
    DIALOGS.initialize()
    WIDGETS.initialize()

@_step
def dispatcher():
    log('info', "Initializing dispatcher...", True)
    loading_message("Initialisiere Hauptverarbeitungsschleife...")
    init_dispatcher()

@_step
def setup_window():
    global WINDOW
    log('info', "Creating main window...", True)
    loading_message("Hauptfenster wird geladen...")
    WINDOW = MainWindow()

@_step
def handling():
    log('info', "Initializing disconnect handler...", True)
    loading_message("Initialisiere Verbindungsüberwachung...")
    setup_handling(WINDOW)

@_step
def session():
    log('info', "Starting session...", True)
    loading_message("Sitzung wird gestartet...")
    start_session = EVENTS.resolve("on_start")
    start_session(WINDOW, loading_dialog)

@_step
def finish():
    log('info', "Finished loading, finalizing...", True)
    loading_message("Laden beendet, finalisiere Ladeschleife...")
    exit_handler = EVENTS.resolve("on_exit")
    APP.aboutToQuit.connect(exit_handler)


def load():
    steps = len(_loading_steps)
    current = 1
    for step in _loading_steps:
        step()
        current += 1
        update_progress(int((current / steps) * 100))
        wait()


if __name__ == "__main__":
    log('start', "Welcome to the GrowVolution AdminPanel!")
    log('start', "GrowVolution 2025 - GNU General Public License")

    APP = QApplication(sys.argv)

    loading_dialog = show_loading_screen()
    wait()
    load()

    sys.exit(APP.exec())
