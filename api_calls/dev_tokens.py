from . import CALLS, status
from utils.api import call


def _status(window, response):
    return status(window, response), response.get('output', [])


@CALLS.register('create_token')
def create_token(name: str, valid_opt: int, window):
    response = call('dev_tokens', { 'type': 'default' },
                    { 'cmd': '1', 'name': name, 'valid_opt': str(valid_opt) })

    return _status(window, response)


@CALLS.register('del_token')
def del_token(name: str, window):
    response = call('dev_tokens', { 'type': 'default' },
                    { 'cmd': '2', 'name': name })

    return _status(window, response)
