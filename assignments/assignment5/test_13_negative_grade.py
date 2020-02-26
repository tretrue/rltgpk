import pytest
import Staff


def test_grades(staff_sys):
    #change grade to negative value
    username = 'hdjsr7'
    course = 'cloud_computing'
    assignment = "assignment1"
    test= staff_sys.change_grade(username, course, assignment, -33)
    if test:
        assert False
    else:
        assert True


@pytest.fixture
def staff_sys():
    staffSys = Staff.Staff()
    return staffSys