from . import CALLS, status
from utils.api import call


@CALLS.register('set_var')
def set_var(key, value, groups, add, window):
    response = call('set_var', { 'type': 'default' },{
        'key': key,
        'value': value,
        'groups': groups,
        'add': add
    })

    return status(window, response)


@CALLS.register('del_var')
def del_var(key, window):
    response = call('del_var', { 'type': 'default' },{
        'key': key
    })

    return status(window, response)


@CALLS.register('add_group')
def add_group(name, window):
    response = call('add_group', { 'type': 'default' },{
        'name': name
    })

    return status(window, response)


@CALLS.register('update_group')
def update_group(name, window, **kwargs):
    response = call('update_group', { 'type': 'default' },{
        'name': name,
        'protected': kwargs.get('protected', None),
        'owner': kwargs.get('owner', None)
    })

    return status(window, response)


@CALLS.register('del_group')
def del_group(name, window):
    response = call('del_group', { 'type': 'default' },{
        'name': name
    })

    return status(window, response)
