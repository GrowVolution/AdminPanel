from . import CALLS, status
from utils.api import call


@CALLS.register('bash')
def bash(window, cmd, path):
    response = call('bash', { 'type': 'default' },
                    { 'cmd': cmd, 'path': path })

    return status(window, response), response.get('output', '').strip()


@CALLS.register('check_path')
def get_updates(path):
    response = call('check_path', { 'type': 'default' },
                    { 'path': path })

    return response.get('exists', False)
