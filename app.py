from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return """Welcome to the home page! Seeing this means the flask app is running successfully. Any
requests you wish to make to the REST API can be done now."""


@app.route('/example')
def example():
    return render_template('example.html', **locals())


@app.route('/exampleForm', methods=["POST"])
def exampleForm():
    return "Submitted! Name: " + str(request.form.get('fname'))


# If we run via "python app.py", run in debug mode
if __name__ == "__main__":
    app.run('localhost', 5000, True, True)
