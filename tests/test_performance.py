from reports.performance import generate
import pytest

def test_generate_and_sort():
    data = [
        {'name':'Alex', 'value': '15'},
        {'name': 'Maria', 'value': '10.1'},
        {'name': 'Alex', 'value': '9.4'},
        {'name': 'Maria', 'value': '17'}
    ]

    expected  = [
        {'name': 'Maria', 'value': 13.55},
        {'name': 'Alex', 'value': 12.2}
    ]

    result = generate(data)

    assert result == expected

def test_empty():
    result = generate([])
    assert result == []

def test_empty_first_dict():
    data = [{}]

    with pytest.raises(ValueError) as err:
        generate(data)

    assert str(err.value)

def test_single_key():
    data = [
        {'name': 'Alex'}
    ]

    with pytest.raises(ValueError) as err:
        generate(data)

    assert str(err.value)

def test_conversion_value():
    data = [
        {'name': 'Alex', 'value': 'hi'}
    ]

    with pytest.raises(ValueError) as err:
        generate(data)
    assert str(err.value)

def test_missing_keys():
    data = [
        {'name': 'Alex', 'value': '10'},
        {'name': 'Maria'}
    ]

    with pytest.raises(ValueError) as err:
        generate(data)
    assert str(err.value)

def test_single_row():
    data = [
        {'name': 'Alex', 'value': '10'}
    ]

    expected = [
        {'name': 'Alex', 'value': 10}
    ]
    result = generate(data)

    assert result == expected

def test_negative_values():
    data = [
        {'name': 'Alex', 'value': '-10'},
        {'name': 'Alex', 'value': '11'},
        {'name': 'Maria', 'value': '-5'}
    ]

    expected = [
        {'name': 'Alex', 'value': 0.5},
        {'name': 'Maria', 'value': -5}
    ]
    result = generate(data)

    assert result == expected

def test_zero_values():
    data = [
        {'name': 'Alex', 'value': '0'}
    ]

    expected = [
        {'name': 'Alex', 'value': 0}
    ]
    result = generate(data)

    assert result == expected