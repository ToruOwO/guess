from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def post():
	name=request.form['inputName']
	if name.lower() == 'toruowo':
		return render_template('submit_right.html')
	return render_template('submit_wrong.html')