from PySide6.QtWidgets import QApplication
from app import MainWindow
from events import EVENTS
from threads import THREADS
from app.widgets import WIDGETS
from app.dialogs import DIALOGS
from dispatcher import init_dispatcher
from socket_client import setup_handling
from dotenv import load_dotenv
import sys, os


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
    load_dotenv()
    exec_mode = os.getenv('EXEC_MODE')
    print(f"App is running in {exec_mode.lower()} mode.")

    if exec_mode == "DEBUG":
        from qt_ui import compile_ui
        print("Compiling UI templates...")
        compile_ui()

    EVENTS.initialize()
    THREADS.initialize()
    DIALOGS.initialize()
    WIDGETS.initialize()

    print("Finished initializing, starting main loop.")
    main()
