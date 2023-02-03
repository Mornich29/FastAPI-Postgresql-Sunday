# FastAPI-Postgresql-Sunday
 This is the repository for assesment. This repository covers both Q1 and Q3 of the assesment.


## Q1 
** I stored the Postgresql database by using Docker, so Please Install Docker, Setup the Server and Database before doing this task.
You can do Q4 (Docker Container Task) before dong this task.

 ### How to Run 
1. Make sure that you have created and connected to the database using Postgresql and Docker (If you dont, please checkout Q4 before doing this task.)
2. Create the virtual environment by type "python -m venv venv" in the folder you want to create. 
3. activate the environment by type "source venv/bin/activate" 
4. install the required packages (You can find the packages in requirements.txt)
5. type "uvicorn main:app --reload" in the command line to start.
6. Now you can access to the localhost:8000 (use localhost:8000/docs to try the functions )


## Q3

### How To Run
1. Connect to the database using Postgresql and Docker that you have created in Q1  (If you dont, please checkout Q1 before doing this task.)
2. Activate and use the virtual environement that you have created in Q1.
3. type "uvicorn main:app --reload" in the command line to start.
4. Run Request.py file to insert the random names and emails to the database by doing a hundred parallel requests.

