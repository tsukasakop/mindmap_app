# container name
CNTN = backend
# docker-compose
DC = docker-compose -f docker-compose.yml

# docker commands
build:
	$(DC) up --build

up:
	$(DC) up

stop:
	$(DC) stop

down:
	$(DC) down --rmi all --volumes --remove-orphans

re: down build


iprune:
	docker image prune

cprune:
	docker container prune

clean: cprune iprune


ps:
	$(DC) ps

# django command
bcom:
	$(DC) exec backend bash

# nuxt command
fcom:
	$(DC) exec frontend sh

test:
	$(DC) exec backend python manage.py test

migrate:
	$(DC) exec backend bash -c "python manage.py makemigrations && python manage.py migrate"
