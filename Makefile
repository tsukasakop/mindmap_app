# container name
CNTN = backend
# docker-compose
DC = docker-compose -f docker-compose.yml

# docker commands
up:
	$(DC) up

build:
	$(DC) build
	make up

stop:
	$(DC) stop

down:
	$(DC) down --rmi all --volumes --remove-orphans

re: down up


iprune:
	docker image prune

cprune:
	docker container prune

clean: cprune iprune


ps:
	$(DC) ps

bash:
	$(DC) exec $(CNTN) bash

# django command
test:
	$(DC) exec backend python manage.py test

migrate:
	$(DC) exec backend bash -c "python manage.py makemigrations && python manage.py migrate"
