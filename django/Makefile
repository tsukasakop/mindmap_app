APP_NAME = api
PROJECT_NAME = config

PP_USER = 5
PP_FOLLOW = 5
PP_POST = 5
PP_LIKE = 5
PP_APPLY = 5
#!/bin/sh
# TIME=`date +%M:%S:%N`
# echo "$TIME : $MSG"
# export MSG := Hello!
# # VAL := $(shell ./now.sh)
# VAL := `./now.sh`
# run :
# 	@echo $(VAL)
# 	@echo $(VAL)
# 	@echo $(VAL)

# alias:
# 	alias p='p'
# 	alias manage='python manage.py'
# 	alias populate='python populate.py'

p:
	python

startproject:
	django-admin startproject $(PROJECT_NAME)

superuser:
	python manage.py createsuperuser

startapp:
	python manage.py startapp $(APP_NAME)

migrate:
	python manage.py makemigrations && python manage.py migrate

backup:
	python manage.py dumpdata --indent=2 --exclude=admin --exclude=auth --exclude=contenttypes --exclude=sessions > backup_all.json

recover:
	python manage.py loaddata backup.json

pp_user:
	python populate.py user $(PP_USER)

pp_follow:
	python populate.py follow $(PP_FOLLOW)

pp_post:
	python populate.py post $(PP_POST)

pp_apply:
	python populate.py apply $(PP_APPLY)

pp_like:
	python populate.py like $(PP_LIKE)

pp: pp_user  pp_post pp_follow pp_apply pp_like
