from . import EVENTS
from utils import status
from utils.api import call


@EVENTS.register('set_var')
def set_var(key, value, window):
    response = call('set_var', { 'type': 'default' },
                    { 'key': key, 'value': value})

    return status(window, response)


@EVENTS.register('del_var')
def del_var(key, window):
    response = call('del_var', { 'type': 'default' },
                    { 'key': key })

    return status(window, response)
