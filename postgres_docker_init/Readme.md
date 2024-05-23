# Alpha Project: Setting up infrastructure for local development

<<<<<<< HEAD
## Overview

This project provides a setup to use Docker Compose to create a PostgreSQL image and run a Python script to execute SQL files against the PostgreSQL database. The goal is to simplify the development and testing of SQL scripts in a consistent environment.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker
- Docker Compose
- Python 3.x

## Project Structure

The project structure is as follows:

```
├──postgres_docker_init
    ├── data
        ├── data.csv
    ├── infra_scripts
        ├── init.sql
    ├── src
        ├── __init__.py
        ├── db_manager.py
        ├── main.py
    ├── docker-compose.ynl
├── readme.md
├── requirements.txt

```

`docker-compose.yml`: Defines the Docker services, including the PostgreSQL database.
`init.sql`: The SQL file that contains the database schema and the sql statements to create the table and import the csv file into the table
`db_manager.py`: A python script containing the connection to the postgres database using psycopg2
`main.py`: A python script containing the sql statement
`requirements.txt`: Lists the Python dependencies for the project.
`README.md`: Project documentation.

## Getting Started

### Step 1: Set Up the Docker Environment

1. Create the Docker Compose File

   The docker-compose.yml file sets up the PostgreSQL container.

```
version: '3'

services:
  postgres:
    image: postgres:latest
    environment:
      POSTGRES_USER: alt_school_user
      POSTGRES_PASSWORD: secretPassw0rd
      POSTGRES_DB: alt_school_db
    ports:
      - "5434:5432"
    volumes:
      - ./pg_data:/var/lib/postgresql/data
      - ./data:/data
      - ./infra_scripts/init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  postgres_data:
```

2. Start the Docker Compose Services

   Run the following command to start the PostgreSQL container:
   `docker-compose up`
   This command starts the container in the background.

### Step 2: Install Python Dependencies

1. Create a Virtual Environment (optional but recommended)

```
py -3 -m venv .venv
To activate
.venv\Scripts\activate
```

2. Install dependencies.

```
pip install black
pip install psycopg2-binary
pip install python-dotenv
```

3. Create a requirments.txt file
   `type > requirements.text` for windows
4. Copy the dependencies into the requirement.txt file
   `pip freeze > requirements.txt `
5. Create the .env to keep the postgres connection details
6. Create the python script that will connect to the postgres database in the docker container and run it to see if it connects.
   `py -3 main.py`
7. Clean up: To stop and remove the PostgreSQL container,
   run:`docker-compose down`

## Conclusion

I have successfully set up a PostgreSQL database using Docker Compose and executed SQL commands using a Python script. This setup can be easily adapted for more complex database initialization and management tasks.
=======
This is a portfolio repository about projects I worked on during my final semester at AltSchool as a data engineering student.

## Projects
Alpha Project: This project involves setting up a PostgreSQL database using Docker Compose and executing an SQL script using Python. The purpose is to automate the creation of a PostgreSQL container, initialize the database, and run SQL commands.
>>>>>>> d64efbe6614d19b94f848c8233d9e1fb3a43f658
