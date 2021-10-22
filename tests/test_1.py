import pytest

from r_logger import RLogger


@pytest.fixture()
def r_main_logger():
    return RLogger()


def test_checking_info(caplog, r_main_logger):
    r_main_logger.info('salam')

    assert 'salam' in caplog.text
    assert 'INFO' in caplog.text
