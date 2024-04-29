# crypto_tracker

## Scrapes data from coin market cap using selenium

## Application Demo
Scrapes data from coin market cap after every 15 seconds.
https://github.com/Amangiri99/crypto_tracking/assets/44581374/d535fdf4-6a12-423d-9a4c-96b0405a744a

## Scraper Demo 
https://github.com/Amangiri99/crypto_tracking/assets/44581374/f5422ba5-fa37-438e-9f78-a5464b50ffc2

## Prerequisites
1. Setup postgres
2. Setup Redis 

## Steps to be followed
1. Copy the .env.example and create a .env file.
2. Update the secrets.
3. Run `pipenv shell` to create a virtual env.
4. Run `pipenv install` in order to install all dependencies.
5. Use the below commands to get the service up and running.

## Commands to run the service
- To get all db migrations in place: `python manage.py migrate`
- To start the server: `python manage.py runserver`
- To start the celery beat:  `celery -A apps.celery beat -l info`
- To start the celery worker: `celery -A apps.celery worker -l info`

## Note
We need an active selenium web driver and it is to be configured through env.
