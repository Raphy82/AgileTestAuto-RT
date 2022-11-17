import pytest
from uppgift_1 import Employee

def test_fullname():
    emp1 = Employee("Walter", "White", 11223344, 40000)
    emp2 = Employee("Jesse", "Pinkman", 55667788, 50000)
    assert emp1.fullname == "Walter White"
    assert emp2.fullname == "Jesse Pinkman"

@pytest.mark.xfail() #Create a failed test case that checks if name is no match.
def test_fullname_invalid():
    with pytest.raises(ValueError):
        emp2 = Employee("Jesse", "Pinkman", 55667788, 50000)
        assert emp2.fullname == "Sara Pinkman"

