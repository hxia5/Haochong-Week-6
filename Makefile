install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy

extract:
	python main.py extract

load: 
	python main.py load

query:
	python main.py complex_query "SELECT t1.group, AVG(t1.spi) as avg_soccer_power_in_group, COUNT(t1.win) as win_possibility_0609, COUNT(t2.win) as win_possibility_0613 FROM default.wc609 t1 JOIN default.wc613 t2 ON t1.id = t2.id GROUP BY t1.group, t2.group ORDER BY win_possibility_0609 DESC LIMIT 3"
