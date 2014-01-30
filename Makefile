.PHONY: all flakes tests clean scss presentation

all: flakes

flakes:
	pyflakes selenium_examples tests setup.py

test_venv: requirements.txt node_requirements.txt
	rm -rf test_venv
	rm -rf node_env
	virtualenv test_venv

	bash -c 'source test_venv/bin/activate && \
		pip install -r requirements.txt && \
		pip install -e . && \
		nodeenv node_env --requirement=node_requirements.txt && \
		source node_env/bin/activate && \
		npm install bower && \
		npm install node-sass && \
		bower install'

scss: assets/yelp_reveal.css assets/presentation.css

presentation: scss
	(which google-chrome && google-chrome selenium_presentation.html) || \
	(which firefox && firefox selenium_presentation.html) &

test_user_name: flakes test_venv
	bash -c "source test_venv/bin/activate && \
		testify tests.test_set_user_name"

test_signup: flakes test_venv
	bash -c "source test_venv/bin/activate && \
		testify tests.test_signup"

test_rosi: flakes test_venv
	bash -c "source test_venv/bin/activate && \
		testify tests.test_rosi_login"

serve: flakes test_venv
	bash -c "source test_venv/bin/activate && \
		python selenium_examples/main.py"

selenium_start:
	bash -c "java -jar bin/selenium-server-standalone-2.39.0.jar \
		-Dwebdriver.chrome.driver=bin/chromedriver"

selenium_start_linux:
	bash -c "java -jar bin/selenium-server-standalone-2.39.0.jar \
		-Dwebdriver.chrome.driver=bin/chromedriver-linux"

create_fixtures: test_venv
	bash -c "source test_venv/bin/activate && \
		python create_fixtures.py"

delete_fixtures:
	rm -f example.db

clean: delete_fixtures
	rm -rf test_venv
	rm -rf node_env
	find . -iname '*.pyc' -delete

%.css: %.scss test_venv
	bash -c "source test_venv/bin/activate && \
		source node_env/bin/activate && \
		node-sass $^ -o $@"
