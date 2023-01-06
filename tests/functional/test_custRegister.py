from app import app


def testCustRegister(testClient):
    '''
    GIVEN a Flask app configured for testing
    WHEN the '/custRegister' page is requested
    THEN check that the response is valid
    '''

    response = testClient.get('/')
    assert response.request.method == 'GET'
    assert response.status_code == 200
    assert b'Customer Registration' in response.data
