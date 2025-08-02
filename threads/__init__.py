from packaging import Package
from debugger import log

from PySide6.QtCore import QThread
from pathlib import Path
from uuid import uuid4
import time

RUNNING = {}


class BaseThread(QThread):
    def __init__(self):
        super().__init__()
        self.running = True
        self.no_loop = False
        self.id = uuid4()
        log('info', f"Created thread {self.id}.", True)

    def loop(self):
        raise NotImplementedError("loop() not implemented")

    def task(self):
        raise NotImplementedError("task() not implemented")

    def start(self, /, priority = ...):
        super().start()
        time.sleep(.5)

    def run(self):
        log('info', f"Starting thread {self.id}...", True)
        RUNNING[self.id] = self
        if self.no_loop:
            self.task()
            return

        while self.running:
            self.loop()

    def stop_task(self):
        raise NotImplementedError("stop_task() not implemented")

    def stop(self):
        RUNNING.pop(self.id, None)
        if self.no_loop:
            self.stop_task()
            return
        self.running = False
        self.wait()


THREADS = Package(Path(__file__).parent)
