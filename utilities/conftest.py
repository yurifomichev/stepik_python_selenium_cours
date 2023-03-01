import pytest

@pytest.fixture
def set_up():
    print('Start test')
    yield
    print('Finish test')

@pytest.fixture(scope='cls')
def set_group():
    print('Start test')
    yield
    print('Finish test')

