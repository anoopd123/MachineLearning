from flask import Flask, request
import pickle

f=open("mymodel.pkl","rb")
mymodel = pickle.load(f)
f.close()

app = Flask(__name__)


@app.route('/')
def abcd():
    return "Hello from flask"

@app.route("/contact")
def xyz():
    return "This is Optum, how can I help you"

@app.route("/predict")
def createform():
    text = """
    <form method="post" action="/predict2">
    <input type=text name="x1"> Square Feet<br>
    <input type=text name="x2"> Room Count<br>
    <input type=text name="x3"> Area<br>
    <input type=submit>
    </form>
    """
    return text

@app.route("/predict2", methods=["POST"])
def predict():
    x1 = request.form.get("x1")
    x2 = request.form.get("x2")
    x3 = request.form.get("x3")

    return "here comes your prediction" + x1 + x2 +x3
    


app.run()