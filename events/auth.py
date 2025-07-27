from . import EVENTS
from app.dialogs import DIALOGS
from app.widgets import WIDGETS
from utils import KEY_FOLDER, set_user
from utils.api import call
from utils.crypt import generate_keypair, check_password, cache_private_key


@EVENTS.register('on_login')
def login(window, ui):

    name = ui.username.text().strip()
    if not name:
        window.show_status("Benutzername darf nicht leer sein", 'error')
        return

    if ui.create_new.isChecked():
        token = ui.creation_token.text().strip()
        response = call('verify_token', {
            'auth': token,
            'type': 'token'
        })
        if not response.get('valid', False):
            window.show_status("Ungültiges token", 'error')
            return

        public_key, password = generate_keypair(name)
        response = call('create_user', {
            'auth': token,
            'type': 'token'
        }, {
            'username': name,
            'public_key': public_key
        })
        if not response.get('success', False):
            window.show_status(f"Fehler beim Erstellen des Accounts: {response.get('error', "Unbekannter Fehler.")}.", 'error')
            key = KEY_FOLDER / f"{name}.pem"
            key.unlink(missing_ok=True)
            return

        show_password = DIALOGS.resolve('password_info')
        show_password(password)
        window.show_status("Benutzer erfolgreich erstellt!", 'success')

    password = ui.password.text().strip()
    if not password:
        window.show_status("Passwort darf nicht leer sein", 'error')
        return

    if not check_password(name, password):
        window.show_status("Ungültige Anmeldedaten", 'error')
        return

    window.show_status("Login erfolgreich!", 'success')

    cache_private_key(name, password)
    set_user(name)

    update_widget = EVENTS.resolve('update_widget')
    update_widget(window, 'dashboard')
    window.browser.ui.backend.setText(name)
