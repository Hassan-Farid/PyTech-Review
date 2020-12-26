#Flask application that greets its users
from flask import Flask, render_template, request, escape
app = Flask(__name__)

@app.route('/')
def greet_user_query():
    #Generates a greeting to the user when /?username=UserName is used with the general URL 
    return render_template('hello.html', username=request.args.get("name", "user"))


@app.route('/greet', methods=['GET'])
def greet_user_form():
    #Generates a form which when submitted greets the user
    return render_template("greet.html", username=request.args.get("name", "User"))

@app.route('/<username>')
def greet_user_url(username):
    #Generates a greeting to the user when /UserName is used with the general URL
    return "Hello %s" % escape(username)
