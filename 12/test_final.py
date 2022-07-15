from pytest import approx
import pytest
from final_test import calculate_average, evaluate_program


def test_calculate_average():
    """ 
    Description: this function test the calculate_average function and use the approx to be able to work with decimals and also test if the function raise and Error when it was called with wrong arguments
    """
    assert calculate_average(4, 4, 5) == approx(4.33, 0.01)
    with pytest.raises(TypeError) as e:
        calculate_average(4, 4, '5')
    assert e.type == TypeError
    assert 'Arguments are not numbers' in str(e.value)


pytest.main(["-v", "--tb=line", "-rN", __file__])
