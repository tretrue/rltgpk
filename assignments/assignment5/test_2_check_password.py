import pytest
import System

@pytest.mark.parametrize("username, password",[("saab","boomr345"),("akend3","123454321"),("saab","bamr345"),("calyam","yote"),("calyam","#yeet")])
def test_check_password(grading_system, username, password):
    assert grading_system.check_password(username,password), "incorrect password ("+password+") for user "+username+"."
    


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem