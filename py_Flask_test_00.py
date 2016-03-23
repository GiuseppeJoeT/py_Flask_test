from flask import Flask, abort

# We import the Flask class

app = Flask(__name__)

# We create an instance of our class and pass it the name of our module

ages = {
    'bob': '43',
    'alice': '29'
}


@app.route('/users/<user>')
def users(user):
    age = ages.get(user)
    if age:
        return '%s is %s years old' % (user, age)
    else:
        abort(404)


'''
we ve used -user- as a placeholder in the url.
This means that the function user_profiles will receive this part of the url as the user argument
'''


# We return a 404 to signify that this user has not been found

@app.route('/')
def hello_world():
    return "Hey"


'''
The decorator is saying:
if the user navigates to the address /, then run the function below.
i.e. the decorated function.
'''

if __name__ == '__main__':
    app.run(debug=True)
    # to activate debug mode: app.run(debug=True)

'''
- We use the IF to ensure the app is only run when instantiated directly
from the Python interpreter, not when imported from another file.
- We run our app using app.run()
'''
