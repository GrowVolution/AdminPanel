from app.loading_screen import loading_message
from debugger import log
from utils import wait

from pathlib import Path
import importlib

_root_dir = Path(__file__).parent.resolve()


class Package:
    def __init__(self, path: Path, wrapper=lambda *a: lambda o: lambda *args, **kwargs: o(*args, **kwargs)):
        self.storage = {}
        self.wrapper = wrapper

        path = path.resolve()
        if not str(path).startswith(str(_root_dir)):
            raise ValueError(f"Package path {path} is not inside root {_root_dir}")

        self.path = path
        self.import_base = ".".join(path.relative_to(_root_dir).parts)
        self.initialized = False

    def initialize(self):
        log('info', f"Initializing package {self.import_base}...", True)
        loading_message(f"Initialisiere Paket: {self.import_base}")
        wait(250)
        for file in self.path.glob("*.py"):
            if file.name == "__init__.py":
                return
            module_name = f"{self.import_base}.{file.stem}"
            log('info', f"Loading module {module_name}...", True)
            loading_message(f"Lade Modul: {module_name}")
            importlib.import_module(module_name)
            wait(150)

    def register(self, key: str, *args) -> callable:
        def decorator(obj):
            wrapped = self.wrapper(*args)(obj)
            self.storage[key] = wrapped
            return wrapped
        return decorator

    def resolve(self, key: str):
        if key not in self.storage:
            raise ValueError(f"Unknown package: {key}")
        return self.storage[key]
