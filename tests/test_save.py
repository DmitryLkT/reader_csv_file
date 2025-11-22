import os
import pytest
from reports.save_file import save

def test_normal_save():
    data = [
        {'name': 'Maria', 'value': 13.55},
        {'name': 'Alex', 'value': 12.2}
    ]

    filename = 'tests/test'

    save(filename, data)

    with open(filename + ".csv", 'r', encoding='utf-8') as f:
        content = f.read()

        assert 'name,value' in content
        assert 'Maria,13.55' in content
        assert 'Alex,12.2' in content

def test_auto_add_csv_extension():
    data = [
        {'name': 'Maria', 'value': 13.55},
    ]

    filename = 'tests/test'

    save(filename, data)

    assert os.path.exists(filename + ".csv")

def test_validate_errors():

    with pytest.raises(ValueError) as err:
        save("test", [])
    assert str(err.value)

    with pytest.raises(ValueError) as err:
        save("test", [{}])
    assert str(err.value)

def test_different_type():
    data = [
        {"int": 1, "float": 1.5, "bool": True, "none": None}
    ]
    filename = 'tests/test'

    save(filename, data)

    assert os.path.exists(filename + ".csv")
