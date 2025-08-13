from . import CALLS, status
from utils.api import call
from data import get_actions


@CALLS.register('publish_queue')
def add_queue(window):
    queue = get_actions()
    if len(queue) == 0:
        window.show_status("Keine Aktionen in der Warteschlange gefunden.", 'warning')
        return False

    queue_data = {}
    for item in queue:
        queue_data[item.name] = item.data

    response = call('add_queue', { 'type': 'default' }, {
        'queue': queue_data
    })
    return status(window, response)


@CALLS.register('get_actions')
def get_queue_actions(queue):
    response = call('get_actions', { 'type': 'default' }, {
        'queue': queue
    })
    return response.get('actions', {}), response.get('error', None)


@CALLS.register('get_comments')
def get_comments(action):
    response = call('get_comments', { 'type': 'default' }, {
        'action': action
    })
    return (response.get('comments', {}), response.get('commented', False),
            response.get('error', None))


@CALLS.register('add_comment')
def add_comment(action, content):
    response = call('add_comment', { 'type': 'default' }, {
        'action': action,
        'content': content
    })
    return response.get('error', None)


@CALLS.register('vote')
def vote(window, queue, action):
    response = call('vote', { 'type': 'default' }, {
        'action': action,
        'queue': queue
    })
    return status(window, response)
