from flask import Flask
'''
It create an instance of the Flask class,
which is your WSGI (wev server Gateway Interface) application
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask course This  be an amazing course"

@app.route("/index")
def index():
    return 'welcome to index'

if __name__ == "__main__":
    app.run(debug=True)
    