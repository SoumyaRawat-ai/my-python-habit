from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to come'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f'hello {name}!'
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)