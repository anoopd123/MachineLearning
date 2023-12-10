from flask import Flask
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

@app.route("/jobs")
def jobs():
    return "Jobs info will be posted shortly"

@app.route("/predict/<years>")
def predict(years):
    exp = float(years)
    salary = str(mymodel.predict([[exp]])[0])
    return f"Salary for the experience with {exp} is {salary}"

app.run()