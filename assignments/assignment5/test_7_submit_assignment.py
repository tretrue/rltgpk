import pytest
import System
import Student


def test_submit_assignment(student_sys):
    course = 'comp_sci'
    assignment_name = 'assignment2'
    submission = 'Beep Boop'
    submission_date = '02/05/20'
    assert student_sys.submit_assignment(course, assignment_name, submission, submission_date)
   


@pytest.fixture
def student_sys():
    gradingSystem = System.System()
    gradingSystem.load_data()
    studentSys = Student.Student('akend3', gradingSystem.users, gradingSystem.courses)
    return studentSys