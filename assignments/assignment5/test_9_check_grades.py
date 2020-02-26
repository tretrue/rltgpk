import pytest
import System
import Student

def test_check_grades(student_sys):
    course = 'comp_sci'
    assert student_sys.check_grades(course)


@pytest.fixture
def student_sys():
    gradingSystem = System.System()
    gradingSystem.load_data()
    studentSys = Student.Student('akend3', gradingSystem.users, gradingSystem.courses)
    return studentSys