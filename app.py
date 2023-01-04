from flask import Flask, render_template as render, request
app = Flask(__name__)


@app.route('/')
def home():
    return render('index.html', **locals())


@app.route('/example',methods=["GET","POST"])
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
