from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
	user = { 'name' : 'Barcenas', 'city' : 'Madrid' }
	sobres =[{
			'company' : { 'name' : 'ACS' },
			'Amount' : '100.000EUR'
		 },
		 {
			'company' : { 'name' : 'FCC' },
			'Amount' : '150.000EUR'
		 },
		]
	return render_template("index.html",
		pagetitle = 'Home',
		user = user, envelopes = sobres)
