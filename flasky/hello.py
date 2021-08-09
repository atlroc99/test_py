from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html', name='user')


@app.route('/user/<username>')
def greet(username):
    return render_template(template_name_or_list='user.html', username=username)


@app.route('/dictionary-test')
def test_dictionary():
    user_dictionary = {'name': 'jon', 'age': 24, 'gender': 'male'}
    return render_template('user.html', user_dictionary=user_dictionary)
