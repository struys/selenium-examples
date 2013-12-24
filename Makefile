.PHONY: flakes tests clean

all: flakes

flakes:
	pyflakes tests setup.py

test_venv: requirements.txt node_requirements.txt
	rm -rf test_venv
	rm -rf node_env
	virtualenv test_venv

	bash -c 'source test_venv/bin/activate && \
		pip install -r requirements.txt && \
		pip install -e . && \
		nodeenv node_env --requirement=node_requirements.txt && \
		source activate && \
		bower install'

scss: test_venv
	bash -c "source test_venv/bin/activate && cd assets && node-sass yelp_reveal.scss && node-sass presentation.scss"

test_user_name: flakes test_venv
	bash -c "source test_venv/bin/activate && testify tests.test_set_user_name"

test_signup: flakes test_venv
	bash -c "source test_venv/bin/activate && testify tests.test_signup"

test_rosi: flakes test_venv
	bash -c "source test_venv/bin/activate && testify tests.test_rosi_login"

serve_signup: flakes test_venv
	bash -c "source test_venv/bin/activate && python selenium_examples/signup.py"

serve: flakes test_venv
	bash -c "source test_venv/bin/activate && python selenium_examples/set_user_name.py"

selenium_start:
	bash -c "java -jar bin/selenium-server-standalone-2.35.0.jar \
		-Dwebdriver.chrome.driver=bin/chromedriver"

create_fixtures: test_venv
	bash -c "source test_venv/bin/activate && python create_fixtures.py"

delete_fixtures:
	if [ -a example.db ] ; \
	then \
		rm example.db  ; \
	fi;

clean: delete_fixtures
	rm -rf test_venv
	rm -rf node_env
	find . -iname '*.pyc' -delete

