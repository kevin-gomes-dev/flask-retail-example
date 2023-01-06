# Python (Flask) Retail Application Example
This is a simple application to simulate a customer based site that allows purchasing of items.
The database we will be using will be postgreSQL. Connections will be pooled to avoid extensive resource use.
Flask will run by default on port 5000, host localhost (so it expects your database to be local)

To run the backend:
1. Ensure python 3.10+ is installed, and create a virtual environment (install if you haven't via pip install virtualenv). Something like: virtualenv directoryName.
2. Tell your terminal to use this as the python (confirm with "which python" command). For Windows, this is (assuming my virtual env folder is called venv) source venv/Scripts/activate. For other OS, this is venv/bin/activate.
3. Install all requirements via pip install -r requirements.txt.
4. Ensure a file called ".env" is placed at the root of the project with PostgreSQL credentials and the name of the database we connect to. Create a database to connect to if you haven't already via pgAdmin or psql. Ex: CREATE DATABASE flask-example

The fields we are most interested in (if empty or not provided, defaults will be used)
- PSQL_USERNAME=(default 'postgres')
- PSQL_PASSWORD=(default 'password')
- DB_NAME=(default 'flask-example')
- DB_PORT=(default '5432')
- DB_HOST=(default 'http://localhost')

5. Use command: flask run (or python app.py for debugging).