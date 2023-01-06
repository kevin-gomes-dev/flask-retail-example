import pytest
from app import app


@pytest.fixture(scope='module')
def testClient():
    app.testing = True
    with app.test_client() as c:
        with app.app_context():
            yield c
