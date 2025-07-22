from pathlib import Path
import importlib

_root_dir = Path(__file__).parent.resolve()


class Package:
    def __init__(self, path: Path, wrapper=lambda *a: lambda o: lambda *args: o(*args)):
        self.storage = {}
        self.wrapper = wrapper

        path = path.resolve()
        if not str(path).startswith(str(_root_dir)):
            raise ValueError(f"Package path {path} is not inside root {_root_dir}")

        self.path = path
        self.import_base = ".".join(path.relative_to(_root_dir).parts)
        self.initialized = False

    def initialize(self):
        print(f"Initializing package {self.import_base}")
        for file in self.path.glob("*.py"):
            if file.name == "__init__.py":
                continue
            module_name = f"{self.import_base}.{file.stem}"
            print(f"Loading module {module_name}")
            importlib.import_module(module_name)

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
