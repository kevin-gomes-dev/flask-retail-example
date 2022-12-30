# Python (Flask) Retail Application Example
This is a simple application to simulate a customer based site that allows purchasing of items.
The database we will be using will be postgreSQL, and we will leverage frameworks to interact instead
of doing everything manually.

To run the backend:
1. Ensure python 3.10+ is installed, and create a virtual environment (install if you haven't via pip install virtualenv). Something like: virtualenv directoryName.
2. Tell your terminal to use this as the python (confirm with "which python" command). For Windows, this is (assuming my virtual env folder is called venv) source venv/Scripts/activate. For other OS, this is venv/bin/activate.
3. Install all requirements via pip install -r requirements.txt.
4. Use command: flask run (or python app.py for debugging).