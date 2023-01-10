from datetime import datetime
import re
from flask import request
import bcrypt
from models import ShipAddr


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
        'shipAddr': ShipAddr('123 Sesame St', 'Bristol', 'RI', '12345'),
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

    # Add shipping address validation, which calls a helper to validate


def dateCheck(date: str):
    '''
    Checks if date is in correct format. Accepted formats are mm-dd-yyyy and mm/dd/yyyy

    Args:
        date (str): The date to check
    '''
    result = True
    try:
        result = bool(datetime.strptime(date, '%m-%d-%Y'))
    except ValueError:
        try:
            result = bool(datetime.strptime(date, '%m/%d/%Y'))
        except ValueError:
            result = False
    return result


def emailCheck(email: str):
    '''
    Checks if email is correctly formatted. Accepted format is a@b.c (any amount of .c, like a@b.c.d.e)

    Args:
        email (str): The email to validate
    '''
    # To match email patterns. Broken up this reads:
    # The pattern for everything before the @. Match at least 1-unlimit alphanumeric
    # followed by 0-unlimit of + or . or any alphanumeric or -. Then have @
    reg1 = r'^\w+[\+\.\w-]*@'
    # Pattern for domain. First have a group that matches 1-unlimit alphanumeric or -,
    # then must have . char. This group can be repeated 0-unlimit times. Then match a word 1-unlimit,
    # then 0-unlimit an alphanumeric or - followed by a .
    reg2 = r'([\w-]+\.)*\w+[\w-]*\.'
    # Pattern for extension. A group that matches lowercase letters 2-4 times OR matches 1-unlimit digit
    reg3 = r'([a-z]{2,4}|\d+)$'
    regex = reg1+reg2+reg3
    return re.match(regex, email)


def phoneCheck(phone: str):
    '''
    Checks for valid phone numbers using pattern matching. Note the number could be fake...
    Valid phone numbers potentially start with +, followed by the whole number including area code
    If international, can use 44 as well, but no spaces or - within number

    Args:
        phone (str): The phone number to check
    '''
    # Replace unwanted characters
    phone = phone.strip('-')
    phone = phone.strip()
    # Start with 0-1 +, then 1-15 numbers after
    regex = r'^[+]?([0-9]{1,15})$'
    return re.match(regex, phone)
