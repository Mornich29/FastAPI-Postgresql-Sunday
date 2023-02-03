# FastAPI-Postgresql-Sunday
 This is the repository for assesment. This repository covers both Q1 and Q3 of the assesment.

## Docker and Postgres Setup:

1. Install Docker from https://www.docker.com/.
2. Pull the postgres-alpine by type "docker pull postgres:alpine"
3. Run the container by type "docker run --name name -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine". You can change password and name of the container.
4.type "docker exec -it name bash"
5.type "psql -U postgres"
6. Create Database by type "create database name_of_db"
7.create user role. You can add superuser role by type "CREATE ROLE name WITH LOGIN SUPERUSER PASSWORD 'password';"
8.connect to the Database by type "\c database name"


## Q1 
** I stored the Postgresql database by using Docker, so Please Install Docker, Setup the Server and Database before doing this task.
You can do Q4 (Docker Container Task) before dong this task.

 ### How to Run 
1. Make sure that you have created and connected to the database using Postgresql and Docker (If you dont, please checkout Q4 before doing this task.)
2. Create the virtual environment by type "python -m venv venv" in the folder you want to create. 
3. activate the environment by type "source venv/bin/activate" (MacOS) , "venv\Scripts\activate" (Windows OS)
4. install the required packages (You can find the packages in requirements.txt)
5. Change your database url by using the username and password that you used in Docker and Postgres Setup Step.
6. type 'python' in the command line and enter
7. type 'import services' in the command line and enter
8. type 'import services._add_tables()' in the command line and enter
9. type "uvicorn main:app --reload" in the command line to start.
10. Now you can access to the localhost:8000 (use localhost:8000/docs to try the functions )


## Q3

### How To Run
1. Connect to the database using Postgresql and Docker that you have created in Q1  (If you dont, please checkout Q1 before doing this task.)
2. Activate and use the virtual environement that you have created in Q1.
3. type "uvicorn main:app --reload" in the command line to start.
4. Run Request.py file to insert the random names and emails to the database by doing a hundred parallel requests.

