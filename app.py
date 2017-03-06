from xml.etree.ElementTree import fromstring
from flask import Flask, render_template, request,json,jsonify, redirect

import urllib
import random
import string
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

@app.route('/')
def index():
	return render_template("formSubmission.html");

@app.route('/displayAll')
def displayAll():
	conn = mysql.connect()
	cursor = conn.cursor()
	resultsFromDB = "SELECT u.battletagid, s.username, s.score, s.timerecorded FROM users u INNER JOIN scorelogs s ON s.battletagid = u.battletagid"
	cursor.execute(resultsFromDB)
	results = cursor.fetchall()
	print(results)
	print(len(results))
	for row in results:
		print(row)
	return render_template("displayAll.html",JSONResults=results);


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

	# Clean all data
	# stmt5 = "DELETE From scorelogs"
	# cursor.execute(stmt5);
	# conn.commit()
	# stmt6 = "DELETE FROM users"
	# cursor.execute(stmt6);
	# conn.commit()

	stmt1 = "INSERT IGNORE INTO users (battletagid) VALUES (%s)"
	cursor.execute(stmt1, battleid)
	conn.commit()

	stmt2 = "INSERT INTO scorelogs (battletagid, score, timerecorded, username) VALUES (%s, %s, %s, %s)"
	data2 = (battleid, level, time, username)
	cursor.execute(stmt2, data2)
	conn.commit()

#CREATE TABLE users(
#battletagid VARCHAR(50) NOT NULL,
#PRIMARY KEY (battletagid)
#)

#CREATE TABLE scorelogs(
#battletagid VARCHAR(50) NOT NULL,
#score int NOT NULL,
#timerecorded VARCHAR(50) NOT NULL,
#username VARCHAR(50) NOT NULL,
#PRIMARY KEY (timerecorded),
#FOREIGN KEY (battletagid) REFERENCES users(battletagid)
#)
	return redirect('/displayAll');


if __name__ == '__main__':
	app.run(debug=True)
