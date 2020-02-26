#method returns true regardless of what is sent in ...

import pytest
import System
import Student


def test_check_ontime(student_sys):
    due_date = '07/30/20'
    submission_date = '07/11/20'
    testdate = '09/13/20'
    if student_sys.check_ontime(submission_date, due_date) and not student_system.check_ontime(testdate, due_date):
        assert True
    else:
        assert False


@pytest.fixture
def student_sys():
    gradingSystem = System.System()
    gradingSystem.load_data()
    studentSys = Student.Student('akend3', gradingSystem.users, gradingSystem.courses)
    return studentSys