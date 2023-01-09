from datetime import datetime
import re
from flask import request
from app import app


def testCustRegister(testClient):
    '''
    GIVEN customer data to be registered
    WHEN the '/custRegister' page is requested via POST
    THEN check that the response is valid and all data is valid

    Args:
        testClient (FlaskClient): The client to do the request
    '''
    data = {
        'fname': 'Kevin',
        'lname': 'Gomes',
        'dob': '04/13/1996',
        'email': 'kevin.gomes.dev@gmail.com'
    }
    # testClient = app.test_client()
    response = testClient.post('/custRegister', data=data)
    data = request.form
    assert request.method == 'POST'
    assert response.content_type == 'application/json'
    assert len(data) <= 8
    assert type(data.get('fname')) == str
    assert type(data.get('lname')) == str
    assert dobCheck(data.get('dob'))
    assert emailCheck(data.get('email'))


def dobCheck(date: str):
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
