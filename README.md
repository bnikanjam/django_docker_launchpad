Web App Launchpad Deploying on Heroku with Docker 
-

## Setup
#### clone the repo to your local computer
>git clone ...
#### provide credentials and security settings via environmental variables in the .env file
>ENVIRONMENT for production, development or other. When in development DEBUG will be set to TRUE
>SECRET_KEY
>ADMIN_URL
>Email provider credentials
>AMAZON S3 credentials for user files (media files)

#### Pipenv virtual environment
>pipenv shell

#### Build the docker containers
>docker build .

#### Run the app within docker
>docker-compose up

#### Database migrations and create superuser
#### Login to admin and add settings for social login oauth accounts







##### Custom admin url instead of django's default 'admin'
>This is a recommended security measure not to reveal the admin login page


##### WhiteNoise for serving staticfiles 
>Making static files a self-contained unit that can be deployed anywhere 
without relying on nginx, Amazon S3 or any other external service.

##### Gunicorn Python WSGI HTTP UNIX Server for both Dev and Prod
>Production level WSGI server; Simply implemented, light on server resource usage, and fairly speedy. It natively supports WSGI, Django, and Paster.

##### DJ-Database-URL
>Simple utility to convert DATABASE_URL environment variable to configure database credentials and settings.
>
