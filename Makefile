migrate:
	@python manage.py migrate

superuser:
	@echo "Creating superuser"
	@echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', '', 'admin')" | python manage.py shell

run-server:
	@python manage.py runserver 0.0.0.0:8000

run-test:
	@echo "Running tests..."
	@coverage run manage.py test --deprecation all
	@coverage report -m
