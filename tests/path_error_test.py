
from pathlib import Path
from win_path.class_with_path import ClassWithPath

## Test Path.exists

def test_exists_valid_path():
    path_class = ClassWithPath("C:/Users")
    assert path_class.path_exists() == True

def test_exists_valid_string_invalid_path():
    path_class = ClassWithPath("C:/Users/Invalid")
    assert path_class.path_exists() == False

def test_exists_valid_path_asterisk():
    path_class = ClassWithPath("C:/Users/*/")
    assert path_class.path_exists() == False

def test_exists_invalid_path():
    path_class = ClassWithPath("<some text>")
    assert path_class.path_exists() == False

## Test Path.resolve

def test_resolve_valid_path():
    path_class = ClassWithPath("C:/Users")
    new_path = path_class.path_resolve()
    print(new_path)
    assert isinstance(new_path, Path)

def test_resolve_valid_string_invalid_path():
    path_class = ClassWithPath("C:/Users/Invalid")
    new_path = path_class.path_resolve()
    print(new_path)
    assert isinstance(new_path, Path)

def test_resolve_valid_path_asterisk():
    path_class = ClassWithPath("C:/Users/*/")
    new_path = path_class.path_resolve()
    print(new_path)
    assert isinstance(new_path, Path)

def test_resolve_invalid_path():
    path_class = ClassWithPath("<some text>")
    new_path = path_class.path_resolve()
    print(new_path)
    assert isinstance(new_path, Path)
