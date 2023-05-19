import pytest


@pytest.fixture()
def right_word():
    return "колбаса"


@pytest.fixture()
def wrong_word():
    return 'калбаса'