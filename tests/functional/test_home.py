def testHome(testClient):
    '''
    GIVEN a Flask app configured for testing
    WHEN the '/' page is requested
    THEN check that the response is valid and the method is GET
    '''
    
    response = testClient.get('/')
    assert response.request.method == 'GET'
    assert response.status_code == 200
    assert b'<h1>Home page' in response.data
