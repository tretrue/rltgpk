import pytest
import System
import Professor


def test_drop_student(prof_sys):
    name = 'akend3'
    course = 'comp_sci'
    if prof_sys.drop_student(name, course) is None:
        assert True
    else:
        assert False


@pytest.fixture
def prof_sys():
    gradingSystem = System.System()
    gradingSystem.load_data()
    professorSys = Professor.Professor("saab", gradingSystem.users, gradingSystem.courses)
    return professorSys