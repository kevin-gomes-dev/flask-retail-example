from flask import Flask, render_template as render, request
from dotenv import load_dotenv
load_dotenv()

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
        return "Customer registration not yet implemented. Data entered:" + str(list(request.form.values()))


# Example code that will eventually get taken out


@app.route('/example', methods=["GET", "POST"])
def example():
    if request.method == "GET":
        return render('example.html', fname="")
    else:
        fname = str(request.form.get('fname'))
        return render('example.html', **locals())


@app.route('/exampleForm', methods=["POST"])
def exampleForm():
    return "Submitted! Name: " + str(request.form.get('fname'))


# If we run via "python app.py", run in debug mode
if __name__ == "__main__":
    app.run('localhost', 5000, True, True)
