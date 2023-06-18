MARKER = """\
unit: mark a test as a unit test
integration: mark a test as an integration test
high: mark a test as a high priority test
medium: mark a test as a medium priority test
low: mark a test as a low priority test
"""

def pytest_configure(config):
    map(lambda line: config.addinivalue_line('markers', line), MARKER.split('\n'))
