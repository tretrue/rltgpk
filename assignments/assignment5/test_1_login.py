import pytest
import System

def test_login(grading_system):
    username = 'saab'
    password =  'boomr345'
    grading_system.login(username,password)
    assert grading_system.usr.name == username


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem