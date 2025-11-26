#test_faker_ex1
import pytest

@pytest.fixture(scope='session', autouse = True)
def faker_session_ru():
    return ['ru_RU']

@pytest.fixture
def user_data(faker):
    return {
        'username': faker.user_name(),
        'email': faker.email(),
    }

def test_user_data(user_data):
    assert len(user_data['username']) > 5
    assert '@' in user_data['email'] 