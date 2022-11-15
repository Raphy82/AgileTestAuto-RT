from uppgift_1 import Employee
def test_fullname():
    emp1 = Employee("James", "White", 11223344, 40000)
    assert emp1.fullname == "James White"