import pytest
import Staff


def test_grades(staff_sys):
#change grade to improbable grade
    username = 'hdjsr7'
    course = 'cloud_computing'
    assignment = "assignment1"
    test= staff_sys.change_grade(username, course, assignment, 1000)
    if test:
        assert False
    else:
        assert True


@pytest.fixture
def staff_sys():
    staffSys = Staff.Staff()
    return staffSys