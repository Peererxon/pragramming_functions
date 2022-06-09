import pytest
import study

def test_suma():
    a= 2
    b= 3
    result = a + b
    assert study.suma( a,b ) == result

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", "test_suma.py"])