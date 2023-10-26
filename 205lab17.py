
#task 2

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
   a1 = '<h2> lab 17 task 2!</h2>'
   b1 = '<p>breakout room is a name I havent heard in a long time<p>'
   return a1 + b1

#flask --app 205lab17 --debug run


#task 3 

@app.route('/jake')
def t_test():
   return render_template('templates.html')


#task 4

from flask_bootstrap import Bootstrap5
bootstrap = Bootstrap5(app)