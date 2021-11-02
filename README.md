# ryde-backend-challenge

## Prerequisites

This project is run fully based on docker and docker-compose.

Please install docker at `https://docs.docker.com/install/` and docker-compose at `https://docs.docker.com/compose/install/`.

## Running the Project

1. Copy the `.env.example` file available and create an `.env` file at the same directory. Update the fields accordingly for secret data.
2. `docker-compose --env-file .env config`

   * This command will configure the `docker-compose.yml` by taking in the environment variables stated in `.env`
   * Note: please ensure to install docker-compose version 1.8+ for the config to work properly
3. `docker-compose up`

   1. This will start the process of building the backend image from the source Python 3.6 base image, and installing pip packages stated inside the `requirements.txt` file.

      - Please refer to `Dockerfile` for more details.
      - All codes will be mounted as a volume inside the `/code` directory.
   2. A MongoDB base image will also be pulled from the docker registry.

      * All data will be stored in the `/data/db` directory inside the mongodb image, while in the project directory itself, you can see them inside `./db` folder
   3. After building the image, the processes will be started as stated in the `docker-compose.yml` file.

      * Upon starting up, a data migration will be carried out based on the migrations stated inside the `migrations` folder.
4. Visit APIs documentation at `localhost:8000/swagger/`
5. To list running docker containers, you can run `docker ps`, note the container id stated in the output.
6. To execute commands inside the image, you can run `docker exec -it <container_id> bash` then run whatever commands you need.

   If you would like to run the test cases, run `python manage.py test` after getting into the backend image.
7. If you need to use the mongodb, the port 27017 is left open. You can access by `mongo -u <your_username> -p <your_password>`

## The Tech Stack

1. This project uses Django-Rest-Framework to deploy REST API.
2. The database used is MongoDB. To connect between Django ORM and MongoDB, a connector  [`djongo`](https://github.com/nesdis/djongo) is used.
3. `drf-yasg` is used to run Swagger for API documentation.

## The Project Scope

This project only implements one very basic django app, which is a user model stored in a MongoDB database.

The user data is stored in the following structure:

```json

        {
            "id": "<user_id>",  
            "name": "<user_name>", 
            "description": "<some_description>",
            "dob": "<dob_in_YYYY-MM-dd_format>", 
            "address": {
                    "address_1" : "<address_2>", 
                    "address_2": "<address_2>",
                    "city" : "<city>",  
                    "zip_code" : "<zip_code>", 
                    "state": "<state>",
            }
        }
```

The configuration of each fields are declared in the `ryde/users/models.py` file.

There are five REST APIs implemented. Please refer to `ryde/ryde/urls.py` and `ryde/users/urls.py`.

<table>
    <tr>
        <th>
            Method
        </th>
        <th>
            Endpoint
        </th>
        <th>
            Request Body
        </th>
        <th>
            Description
        </th>
    </tr>
    <tr>
        <td>
        GET
        </td>
        <td>
        /users
        </td>
        <td>
        </td>
        <td>
        View all users
        </td>
    </tr>
    <tr>
        <td>
        GET
        </td>
        <td>
        /users/< str:id >
        </td>
        <td>
        </td>
        <td>
        View user of a given user id
        </td>
    </tr>
    <tr>
        <td>
        POST
        </td>
        <td>
        /users/< str:id >
        </td>
        <td><pre lang='json'>
        {  
            "name": "<user_name>", 
            "description": "<some_description>",
            "dob": "<dob_in_YYYY-MM-dd_format>", 
            "address": {
                    "address_1" : "<address_2>", 
                    "address_2": "<address_2>",
                    "city" : "<city>",  
                    "zip_code" : "<zip_code>", 
                    "state": "<state>",
            }
        }
        </pre></td>
        <td>
        Add a new user 
        </td>
    </tr>
    <tr>
        <td>
        PUT
        </td>
        <td>
        /users/< str:id >
        </td>
        <td><pre lang='json'>
        {  
            "name": "<user_name>", 
            "description": "<some_description>",
            "dob": "<dob_in_YYYY-MM-dd_format>", 
            "address": {
                    "address_1" : "<address_2>", 
                    "address_2": "<address_2>",
                    "city" : "<city>",  
                    "zip_code" : "<zip_code>", 
                    "state": "<state>",
            }
        }
        </pre>
        </td>
        <td>
        Update data of a specific user of a given user id
        </td>
    </tr>
    <tr>
        <td>
        DELETE
        </td>
        <td>
        /users/< str:id >
        </td>
        <td>
        </td>
        <td>
        Delete data of a user of a given user id
        </td>
    </tr>
</table>
