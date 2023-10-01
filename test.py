
from REST_API import *
import pytest

pytest.fixture()


def test_step_1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert 80657 in lst_id


def test_step_2(get_token):
    create_post(get_token)
    result = get_by_description(get_token)
    print(result)
    lst = result['data']
    lst_id = [el["description"] for el in lst]
    assert 'desc45678' in lst_id


if __name__ == '__main__':
    pytest.main(['-v'])
