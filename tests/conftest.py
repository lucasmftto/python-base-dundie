import pytest

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
