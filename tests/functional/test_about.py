def testAbout(testClient):
    '''
    GIVEN a Flask app configured for testing
    WHEN the '/about' page is requested
    THEN check that the response is valid and the method is GET
    '''
    
    response = testClient.get('/about')
    assert response.request.method == 'GET'
    assert response.status_code == 200
    assert b'<h1>About' in response.data
