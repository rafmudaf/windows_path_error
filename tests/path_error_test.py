
from win_path.demo_error import DemoError

def test_demo_error():
    error = DemoError("This is a test error")
    print(error)
    assert str(error) == "This is a test error"
