selenium-examples
=================

A Presentation for U of T about Selenium Testing at Yelp

Instructions
---------------

1. Clone the repo
git clone https://github.com/struys/selenium-examples.git
cd selenium-examples

2. Setup the virtualenv for python/node and bower install libraries for presentation
make test_venv

3. Start the Selenium Server
make selenium_start

4. Create the test Database/Fixures
make create_fixtures

5. Serve the application for the test (set_user_name, signup)
make serve
make serve_signup

6. Run the selenium test for the application (set_user_name, signup)
make test_set_user_name
make test_signup

7. Run the selenium Test Against ROSI (U of T's course registration site)
make test_rosi


