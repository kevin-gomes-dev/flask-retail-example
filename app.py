import os
from flask import Flask, render_template as render, request
from dotenv import load_dotenv
from validation import validateCustomer
from models import Customer
from psycopg2 import pool
import psycopg2
load_dotenv()

# Connect to database. Use .getconn() and .putconn() respectively when connecting to db
# Get cursor via .cursor() and do SQL statements via cursor.execute. Close when done via cursor.close()
# Please also log whenever database is accessed!
try:
    dbPool = pool.SimpleConnectionPool(
        os.getenv('MIN_CONNECT_LIMIT') or 1,
        os.getenv('MAX_CONNECT_LIMIT') or 20,
        user=os.getenv('PSQL_USERNAME') or 'postgres',
        password=os.getenv('PSQL_PASSWORD') or 'password',
        host=os.getenv('DB_HOST') or 'localhost',
        port=os.getenv('DB_PORT') or '5432',
        database=os.getenv('DB_NAME') or 'flask-example')
    if dbPool:
        print('Successfully created PostgreSQL pool')
except (Exception, psycopg2.DatabaseError) as error:
    print('Error while creating PostgreSQL pool:', error)

# To allow creation of multiple apps, mainly for testing

app = Flask(__name__)
# Defining views here


@app.route('/', methods=["GET"])
def home():
    return render('index.html', **locals())


@app.route('/about', methods=["GET"])
def about():
    return render('about.html', **locals())


@app.route('/custRegister', methods=["GET", "POST"])
def custRegister():
    if request.method == "GET":
        return render('custRegister.html', **locals())
    else:
        return str(validateCustomer(Customer(**request.form)))


# Example code that will eventually get taken out


@app.route('/example', methods=["GET", "POST"])
def example():
    if request.method == "GET":
        return render('example.html', fname="")
    else:
        fname = str(request.form.get('fname'))
        return render('example.html', **locals())


# If we run via "python app.py", run in debug mode
if __name__ == "__main__":
    app.run('localhost', 5000, True, True)
