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
    
  }
  # testClient = app.test_client()
  response = testClient.post('/custRegister',data=data)
  data = request.form
  assert request.method == 'POST'
  assert response.content_type == 'application/json'
  assert len(data) <= 8
  assert nameTest(data.get('fname')) == True
  assert nameTest(data.get('lname')) == True
  
# Helper
def nameTest(name: str):
  '''
  GIVEN a name to test
  WHEN the name is going to be used
  THEN check that the name is valid

  Args:
      name (str): The name to test
  '''
  # In this case, we just check if it's a string. Don't need to get into naming laws...
  return type(name) == str