import pytest
from user import CheckUserLogin, NameErr


@pytest.fixture
def func():
    obj = CheckUserLogin()
    obj.load_users()
    return obj


def test_access(func):
    assert func.get_login_level('Новиков') == 'Пользователь найден'


def test_except(func):
    with pytest.raises(NameErr):
        func.get_login_level('Федоров')


if __name__ == '__main__':
    pytest.main(['-v'])
