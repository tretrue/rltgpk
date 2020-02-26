import pytest
import Staff

def test_create_assignment(sta):
    assignment_name = "test"
    due_date = "1/1/2020"
    course = "comp_sci"
    sta.create_assignment(assignment_name, due_date, course)
    assert sta.all_courses[course]['assignments'], "not created"
    
    
@pytest.fixture
def sta():
    sta = Staff.Staff()
    return sta

