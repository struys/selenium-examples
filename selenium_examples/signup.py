from selenium_examples import app
from flask import request

@app.app.route('/signup')
def render_signup():
	return app.view.render_template('signup.html')

@app.app.route('/signup', methods = ['POST'])
def handle_signup():
	app.db.create_user(
		request.form['name'],
		request.form['email'],
		request.form['password']
	)

	return app.view.render_template('signup_success.html')

@app.app.route('/users')
def list_users():
	return str(app.db.get_users())

if __name__ == '__main__':
	app.app.run(debug=True,)
