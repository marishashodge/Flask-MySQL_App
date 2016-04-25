from flask import Flask, request
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'thirteeneer'
app.config['MYSQL_DB'] = 'EmpData'
app.config['MYSQL_HOST'] = 'localhost'


@app.route("/")
def hello():
    return "Welcome to Python Flask App!"

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    print username
    password = request.args.get('Password')
    print password
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cur.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"


if __name__ == "__main__":
    app.run(debug=True)
