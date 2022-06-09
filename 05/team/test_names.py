from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Marie', 'Toussaint') == 'Toussaint; Marie'
    assert make_full_name('Sergio-Orlando', 'Flores') == 'Flores; Sergio-Orlando'
    assert make_full_name('Anderson', '') == '; Anderson'

def test_extract_family_name():
    assert extract_family_name('Washington; George') == 'Washington'
    assert extract_family_name('Sergio-Orlando; Flores') == 'Sergio-Orlando'

def test_extract_given_name():
    assert extract_given_name('Washington; George') == 'George'
    assert extract_given_name('Sergio-Orlando; Flores') == 'Flores'

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])