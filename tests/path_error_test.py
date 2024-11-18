
from win_path.class_with_path import ClassWithPath

def test_valid_path_that_does_exists():
    path_class = ClassWithPath("C:/Users")
    print(path_class.path_string)
    assert path_class.path_exists() == True

def test_valid_path_that_does_not_exist():
    path_class = ClassWithPath("C:/Users/Invalid")
    print(path_class.path_string)
    assert path_class.path_exists() == False

def test_invalid_path_asterisk():
    path_class = ClassWithPath("C:/Users/*/")
    print(path_class.path_string)
    assert path_class.path_exists() == False

def test_invalid_path_carrot():
    path_class = ClassWithPath("<some text>")
    print(path_class.path_string)
    assert path_class.path_exists() == False
