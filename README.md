selenium-examples
=================

A Presentation for U of T about Selenium Testing at Yelp

Instructions
---------------

Clone the repo

```
git clone https://github.com/struys/selenium-examples.git
cd selenium-examples
```

Setup the virtualenv for python/node and bower install libraries for presentation

```
make test_venv
```

Start the Selenium Server

```
make selenium_start
```

Create the test Database/Fixures

```
make create_fixtures
```

Serve the application for the test (set_user_name, signup)

```
make serve
make serve_signup
```

Run the selenium test for the application (set_user_name, signup)

```
make test_set_user_name
make test_signup
```

Run the selenium Test Against ROSI (U of T's course registration site)

```
make test_rosi
```
