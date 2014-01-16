from selenium_examples import app
from selenium_examples import signup
from selenium_examples import set_user_name

if __name__ == '__main__':
    signup.register(app)
    set_user_name.register(app)
    app.app.run(debug=True,)