from pathlib import Path
from PySide6.QtCore import QTimer, QEventLoop
import string, random

KEY_FOLDER = Path(__file__).parent.parent / "keys"
KEY_FOLDER.mkdir(parents=True, exist_ok=True)
USER = ''


def wait(milliseconds: int = 1000):
    loop = QEventLoop()
    QTimer.singleShot(milliseconds, loop.quit)
    loop.exec()


def connection_check(socket_thread, success_fn, failed_fn = lambda: None):
    def check():
        if socket_thread.success:
            success_fn()
            return

        elif socket_thread.failed:
            failed_fn()
            return

        QTimer.singleShot(100, check)

    check()


def key_list() -> list[str]:
    return [f.stem for f in KEY_FOLDER.glob("*.pem") if f.is_file()]


def random_password(length: int = 16) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))


def set_user(name: str):
    global USER
    USER = name


def get_user() -> str:
    if not USER:
        raise ValueError("User not set")
    return USER


def status(window, response) -> bool:
    success = response.get('success', False)
    if not success:
        window.show_status(f"Fehler beim Ausführen der Aktion: {response.get('error', 'Unbekannter Fehler.')}.", 'error')

    return success
