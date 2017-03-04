from xml.etree.ElementTree import fromstring
from flask import Flask, render_template, request,json,jsonify, redirect

import urllib
import random
import string
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
# MySQL configurations
# https://flask-mysql.readthedocs.io/en/latest/#usage
# https://blogs.msdn.microsoft.com/cdndevs/2015/03/11/python-and-data-sql-server-as-a-data-source-for-python-applications/
app.config['MYSQL_DATABASE_USER'] = 'overwatchtester'
app.config['MYSQL_DATABASE_PASSWORD'] = 'orangy'
app.config['MYSQL_DATABASE_DB'] = 'overwatch'
app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
mysql.init_app(app)
print ('LOOOL')



@app.route('/')
def index():
    return render_template("formSubmission.html");

@app.route('/send')
def send():
    return render_template("send.html");

# Database: overwatch
# Username: overwatchtester
# Email: lin.ruth@outlook.com

@app.route('/submit', methods=['POST'])
def submit():
    battleid = request.form["BattleTagID"]
    username = request.form["Username"]
    level = request.form["Level"]
    time = request.form["Time"]
    print battleid
    print username
    print level
    print time

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users''')
    results = cursor.fetchone()
    print(results)

#CREATE TABLE users(
#battletagid VARCHAR(26) NOT NULL,
#username VARCHAR(26) NOT NULL,
#PRIMARY KEY (battletagid)
#)
#CREATE TABLE scorelogs(
#battletagid VARCHAR(26) NOT NULL,
#score int NOT NULL,
#timerecorded VARCHAR(26) NOT NULL,
#PRIMARY KEY (timerecorded),
#FOREIGN KEY (battletagid) REFERENCES users(battletagid)
#)

    return redirect('/send');





if __name__ == '__main__':
    app.run(debug=True)
