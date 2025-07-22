from pathlib import Path
import string, random

KEY_FOLDER = Path(__file__).parent.parent / "keys"
KEY_FOLDER.mkdir(parents=True, exist_ok=True)
USER = ''


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
