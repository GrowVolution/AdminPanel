from . import EVENTS
from utils import status
from utils.api import call


@EVENTS.register('deploy_updates')
def deploy_updates(window):
    response = call('production_update', { 'type': 'default' })
    return status(window, response)
