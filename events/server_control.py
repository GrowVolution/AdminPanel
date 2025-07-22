from . import EVENTS


@EVENTS.register('server_start')
def start_server():
    pass


@EVENTS.register('server_stop')
def stop_server():
    pass
