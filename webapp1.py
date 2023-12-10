from flask import Flask

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


app.run()