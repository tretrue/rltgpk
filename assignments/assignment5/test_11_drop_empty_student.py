import pytest
import Professor
import System


def test_student(prof_sys):
    #drop a student from a course you do not teach; if successful, assert error.
    name = 'akend3'
    course = 'databases'
    test = prof_sys.drop_student(name, course)
    assert test


@pytest.fixture
def prof_sys():
    gradingSystem = System.System()
    gradingSystem.load_data()
    professorSys = Professor.Professor("saab", gradingSystem.users, gradingSystem.courses)
    return professorSys