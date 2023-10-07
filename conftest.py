from unittest.mock import patch

import pytest
from sqlmodel import create_engine

from dundie import models

MARKER = """\
unit: mark a test as a unit test
integration: mark a test as an integration test
high: mark a test as a high priority test
medium: mark a test as a medium priority test
low: mark a test as a low priority test
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield


@pytest.fixture(autouse=True, scope="function")
def setup_testing_database(request):
    """For each test, create a database file on tmpdir
    force database.py to use that filepath.
    """
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = str(tmpdir.join("databasetest"))

    engine = create_engine(f"sqlite:///{test_db}")
    models.SQLModel.metadata.create_all(bind=engine)
    with patch("dundie.database.engine", engine):
        yield
