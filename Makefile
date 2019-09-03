

server:
	python manage.py runserver 127.0.0.1:8008


migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations
static:
	python manage.py collectstatic

install:
	pip install -r requirements.txt

deploy:
	rsync -av -e ssh --exclude='*.sqlite3' . apitest:~/bursdag

activate:
	. venv/bin/activate


image:
	@if [ -z ${v} ]; then \
		echo "version not provided:  make v=tag image" && exit 1; \
	fi
	docker build -t technocake/bursdag.club:v${v} .
	docker push technocake/bursdag.club:v${v}

stack:
	docker stack deploy -c docker-compose.yml bursdag
