from flask import Flask, render_template, request;

import pandas as pd;

from sklearn.tree import DecisionTreeClassifier;

from sklearn.metrics import accuracy_score;

data = pd.read_csv('Training.csv');

X = data.iloc[:,0:-1].values;
Y = data.iloc[:,-1].values;

k = pd.get_dummies(data.prognosis);

Y = k.values;

classifier = DecisionTreeClassifier();

classifier.fit(X,Y);

app = Flask(__name__);

@app.route('/')

def homepage():
	return render_template('log.html');

@app.route('/login', methods=['POST'])

def checkLogin():
	username = request.form['userid']
	password = request.form['pwd']
	
	if username == 'kits' and password == 'cse':
		return render_template('reg.html');
	else:
		return render_template('log.html', err_log='Check Out your Credentials');

@app.route('/evaluate', methods=['POST'])

def evaluate_User():
	name = request.form['name']
	aadhaar = request.form['aadhaar']
	district = request.form['district']
	village = request.form['village']
	phone = request.form['phone']
	age = request.form['age']
	gender = request.form['gender']
	symptoms = request.form['symptoms']
	
	print(name,aadhaar, district, village, phone, age, gender, symptoms);
	return render_template('out.html')

if __name__ == "__main__":
	app.run();
