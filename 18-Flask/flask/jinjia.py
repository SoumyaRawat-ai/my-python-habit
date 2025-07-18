### Building url Dynamically
## Variable Rule
### jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{}} expression to print output in html
{%..%} condition, for loops
{#..#} this is for comments
'''
from flask import Flask, render_template, request, redirect, url_for

app = Flask('__name__')

@app.route('/')
def home():
    return 'welcome to my python tutorial'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method =="POST":
        name = request.form['name']
        return 'hello soumya how are you'
    return render_template('form.html')

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method =="POST":
#         name = request.form['name']
#         return 'hello soumya how are you'
#     return render_template('form.html')

## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res =''
    if score >= 50:
        res ='PASSED'
    else:
        res = 'FAILED'
    exp = {'score':score, 'Result':res}
    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):
    res =''
   
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result1.html',results=score)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + math + data_science + c)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres', score=total_score))
if __name__ == '__main__':
    app.run(debug=True)