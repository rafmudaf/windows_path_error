
from pathlib import Path

class ClassWithPath():
    def __init__(self, path_string: str):
        self.path_string = path_string

    def path_exists(self) -> bool:
        return Path(self.path_string).exists()
