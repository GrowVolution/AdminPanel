from . import get_user
from .crypt import create_signature
from socket_client import CLIENT
from datetime import datetime, UTC
from socketio.exceptions import TimeoutError
import socketio


def call(handler: str, ident: dict, data: dict | None = None):
    if not CLIENT.connected:
        raise ConnectionError('Client not connected.')

    data = data or {}

    if ident['type'] == 'default':
        ident['auth'] = get_user()
        data['timestamp'] = datetime.now(UTC).isoformat()
        ident['signature'] = create_signature(data)

    try:
        return CLIENT.call('default_event', {
            'event': handler,
            'ident': ident,
            'payload': data,
        }, timeout=5)
    except TimeoutError:
        CLIENT.disconnect()
        return {}
