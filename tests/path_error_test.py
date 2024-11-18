
from win_path.class_with_path import ClassWithPath

def test_valid_path_that_does_exists():
    error = ClassWithPath("C:/Users")
    assert error.path_exists() == True

def test_valid_path_that_does_not_exist():
    error = ClassWithPath("C:/Users/Invalid")
    assert error.path_exists() == False

def test_invalid_path():
    error = ClassWithPath("C:/Users/*/")
    assert error.path_exists() == False
