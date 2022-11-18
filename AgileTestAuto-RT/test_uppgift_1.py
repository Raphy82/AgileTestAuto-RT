import pytest
from uppgift_1 import Employee


@pytest.fixture
def emp1():
    emp1 = Employee("Walter", "White", 11223344, 40000)
    return emp1


@pytest.fixture
def emp2():
    emp2 = Employee("Jesse", "Pinkman", 55667788, 50000)
    return emp2


#Test fullname works
def test_fullname(emp1, emp2):
    assert emp1.fullname == "Walter White"
    assert emp2.fullname == "Jesse Pinkman"
    print(emp1.fullname)

#Test Changing name works
    emp1.first = 'John'
    assert emp1.fullname == "John White"
    print(emp1.fullname)


#Test wrong name is no match, test will fail
@pytest.mark.xfail()
def test_fullname_invalid(emp2):
    with pytest.raises(ValueError):
        assert emp2.fullname == "Sara Pinkman"


#Test email works
def test_email(emp1, emp2):
    assert emp1.email == "Walter.White@iths.se"
    assert emp2.email == "Jesse.Pinkman@iths.se"
    print(emp1.email)

