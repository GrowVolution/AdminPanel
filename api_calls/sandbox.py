from . import CALLS, status
from utils.api import call


@CALLS.register('start_sandbox')
def start_sandbox(dev_note, container_key, group, window):
    response = call('start_sandbox', { 'type': 'default' }, {
        'dev_note': dev_note,
        'container_key': container_key,
        'group': group
    }, 60)

    return status(window, response)


@CALLS.register('stop_sandbox')
def stop_sandbox(window):
    response = call('stop_sandbox', { 'type': 'default' })
    return status(window, response)


@CALLS.register('sync_sandbox')
def sync_sandbox(window):
    response = call('sandbox_sync', { 'type': 'default' })
    return status(window, response)
