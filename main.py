from PySide6.QtWidgets import QApplication
from app import MainWindow
from events import EVENTS
from threads import THREADS
from app.widgets import WIDGETS
from app.dialogs import DIALOGS
from dispatcher import init_dispatcher
from socket_client import setup_handling
import sys


def main():
    print("Creating application...")
    app = QApplication(sys.argv)
    window = MainWindow()
    setup_handling(window)
    init_dispatcher()

    start_session = EVENTS.resolve("on_start")
    start_session(window)

    exit_handler = EVENTS.resolve("on_exit")
    app.aboutToQuit.connect(exit_handler)
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Starting...")
    EVENTS.initialize()
    THREADS.initialize()
    DIALOGS.initialize()
    WIDGETS.initialize()

    print("Finished initializing, starting main loop.")
    main()
