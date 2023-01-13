from flask import request
import bcrypt
from utils import dateCheck, emailCheck, phoneCheck

def testCustRegister(testClient):
    '''
    GIVEN customer data to be registered and a Flask app configured for testing
    WHEN the '/custRegister' page is requested via POST
    THEN check that the response is valid and all data is valid

    Args:
        testClient (FlaskClient): The client to do the request
    '''
    data = {
        'fname': 'Kevin',
        'lname': 'Gomes',
        'dob': '04/13/1996',
        'email': 'kevin.gomes.dev@gmail.com',
        'phone': '+1234567890',
        'cardNum': '1234567890123456',
        'password': 'hshTg420Blz^4WAT?!'
    }
    response = testClient.post('/custRegister', data=data)
    requestData = request.form

    # We use the same salt each time in test to ensure encryption is working
    salt = b'$2b$12$DlR2UAnCQcJwZL1pxE68mu'

    # Encode the password into bytes to be hashed, using same format as the HTML form allows
    passBytes = requestData.get('password').encode('utf-8', 'strict')
    hashedPass = bcrypt.hashpw(passBytes, salt)

    # Encode the card number in bytes to be hashed
    cardBytes = requestData.get('cardNum').encode('utf-8', 'strict')
    hashedCard = bcrypt.hashpw(cardBytes, salt)

    # Potentially modularize so all the specific data checking is done in other tests?
    assert request.method == 'POST'
    assert response.content_type == 'application/json'
    assert len(requestData) <= 8
    # Start checking data
    assert type(requestData.get('fname')) == str
    assert type(requestData.get('lname')) == str
    assert dateCheck(requestData.get('dob'))
    assert emailCheck(requestData.get('email'))
    assert phoneCheck(requestData.get('phone'))
    # Since salt is same every time, the hashed values should be same. Note salt will be generated in app.
    assert hashedPass == b'$2b$12$DlR2UAnCQcJwZL1pxE68mu9nU3llLApzndGTbroJGAJ5PGNarjdRS'
    assert hashedCard == b'$2b$12$DlR2UAnCQcJwZL1pxE68muaFfczu1c55e4KuWdJ86hZ3LoC0nxHvq'
