import pytest
import Staff


def test_assignment(staff_sys):
    #add assignment to no course and no due date
    assignment_name = 'homeworkkk i guess'
    due_date = ''
    course = ''
    test = staff_sys.create_assignment(assignment_name, due_date, course)
    assert not test


@pytest.fixture
def staff_sys():
    staffSys = Staff.Staff()
    return staffSys