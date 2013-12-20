from selenium_examples import app as A

A.db.initialize_schema()
A.db.create_user('Bob', 'bob@yelp.com', 'password')
print A.db.get_user(1)