# crypto_tracker

## Screaps data from coin market cap using selenium

## To use 
1. Setup postgres
2. Setup Redis 

## Steps to be followed
1. Copy the .env.example and create a .env file.
2. Update the secrets.
3. Use the below commands to get the service up and running.

## Commands to run the service
- To get all db migrations in place: `python manage.py migrate`
- To start the server: `python manage.py runserver`
- To start the celery beat:  `celery -A apps.celery beat -l info`
- To start the celery worker: `celery -A apps.celery worker -l info`

## Note
We need an active selenium web driver and it is to be configured through env.