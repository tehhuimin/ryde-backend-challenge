# ryde-backend-challenge

## Prerequisites

This project is run fully based on docker and docker-compose. Please install docker and docker-compose at `https://docs.docker.com/install/` and  `https://docs.docker.com/compose/install/`.

## Running the Project

1. Copy the `.env.example` file available and create an `.env` file at the same directory. Update the fields accordingly for secret data.
2. `docker-compose --env-file .env config` (Note: please ensure to install docker-compose version 1.8+ for the config to work properly)
3. `docker-compose up`
4. Visit APIs documentation at `localhost:8000/swagger/`
