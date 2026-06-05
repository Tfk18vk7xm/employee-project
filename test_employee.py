from employee import *

def setup_function():
    employees.clear()

def test_add_employee():
    add_employee("John")
    assert "John" in get_employees()

def test_remove_employee():
    add_employee("John")
    remove_employee("John")
    assert "John" not in get_employees()

def test_multiple_employees():
    add_employee("John")
    add_employee("Maria")

    assert len(get_employees()) == 2