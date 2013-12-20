
from selenium_examples import app

@app.app.route('/')
def homepage():
	return render_homepage(1)

def render_homepage(user_id):
	user_info = app.db.get_user(user_id)

	return app.view.render_template(
		'set_user_name.html',
		user_name=user_info['name']
	)

if __name__ == '__main__':
	app.app.run(debug=True,)
