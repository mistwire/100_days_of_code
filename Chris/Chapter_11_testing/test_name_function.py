from name_function import get_formatted_name

def test_first_last_name():
    """Does 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin' 

def test_first_last_middle_name():
    """Do middle names like John Lee Hooker work?"""
    formatted_name = get_formatted_name('john', 'hooker', 'lee')
    assert formatted_name == 'John Lee Hooker'

