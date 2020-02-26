import pytest
import System
import Student

def test_view_assignments(student_sys):
#view assignment without a course name
    course = ''
    if(student_sys.view_assignments(course)):
        assert False, "viewed assignments from an unnamed course"


@pytest.fixture
def student_sys():
    gradingSystem = System.System()
    gradingSystem.load_data()
    studentSys = Student.Student('akend3', gradingSystem.users, gradingSystem.courses)
    return studentSys