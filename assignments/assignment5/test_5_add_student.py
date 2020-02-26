import pytest
import Professor
import System

def test_add_student(prof_sys):
    name = 'akend3'
    course =  'comp_sci'
    if prof_sys.add_student(name,course) is None:
        assert False
    else:
        assert True
    


@pytest.fixture
def prof_sys():
    gradingSystem = System.System()
    gradingSystem.load_data()
    professorSys = Professor.Professor("saab", gradingSystem.users, gradingSystem.courses)
    return professorSys