
from pathlib import Path

class ClassWithPath():
    def __init__(self, path_string: str):
        self.path_string = path_string

    def path_exists(self) -> bool:
        return Path(self.path_string).exists()

    def path_resolve(self):
        # NOTE: Path.resolve uses strict=False by default
        return Path(self.path_string).resolve()
