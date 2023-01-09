from datetime import datetime
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
    'dob': '04/13/1996'
    
  }
  # testClient = app.test_client()
  response = testClient.post('/custRegister',data=data)
  data = request.form
  assert request.method == 'POST'
  assert response.content_type == 'application/json'
  assert len(data) <= 8
  assert type(data.get('fname')) == str
  assert type(data.get('lname')) == str
  assert dobCheck(data.get('dob'))
  
def dobCheck(date: str):
  '''
  Checks if date is in correct format. Accepted formats are mm-dd-yyyy and mm/dd/yyyy

  Args:
      date (str): The date to check
  '''
  result = True
  try:
    result = bool(datetime.strptime(date,'%m-%d-%Y'))
  except ValueError:
    try:
      result = bool(datetime.strptime(date,'%m/%d/%Y'))
    except ValueError:
      result = False
  return result