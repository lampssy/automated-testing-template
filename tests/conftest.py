import pytest


@pytest.fixture
def fixture(monkeypatch):
    pass


@pytest.fixture(scope="session")
def fixture_scoped():
    pass
