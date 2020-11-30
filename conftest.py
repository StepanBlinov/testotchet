import pytest


@pytest.fixture(scope="function")
def url():
    return {"reportserver_url": "http://172.16.211.31:8080/BOIreportServerMES/"}

