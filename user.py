from flask import Flask, abort

app = Flask(__name__)

# We create an instance of our class and pass it the name of our module


ages = {
    'bob': '43',
    'alice': '29'
}


@app.route('/users/<user>')
def users(user):
    return '<html>Hello %s</html>' % user


@app.route('/users/<user>')
def users(user):
    age = ages.get(user)
    if age:
        return '%s is %s years old' % (user, age)
    else:
        abort(404)


@app.route('/')
def hello_world():
    return "Hey"

if __name__ == '__main__':
    app.run(debug=True)