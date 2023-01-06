from app import app


def testHome():
    '''
    GIVEN a Flask app configured for testing
    WHEN the '/' page is requested
    THEN check that the response is valid and the method is GET
    '''
    app.testing = True

    with app.test_client() as testClient:
        response = testClient.get('/')
        assert response.request.method == 'GET'
        assert response.status_code == 200
        assert b'Home page' in response.data
