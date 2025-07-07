1. Install PSQL in WSL ( Ubuntu )

    sudo apt update
    sudo apt install postgresql postgresql-contrib

2. Configure User and create the Database

  Start PSQL with:
    sudo service postgresql start

  Access the psql shell with:
    sudo -u postgres psql

  Create the database:
    CREATE DATABASE assignment;

  Create the user with password:
    CREATE USER postgres WITH PASSWORD 'password';    

3. Install DBeaver.

4. Create tables in the database ' assignment ' using Psql CLI.
        user_role_map
        document_data

5. Inside your project directory, setup the virtual environment and install all the requirements using `pip install -r requirements.txt`

6. Move to config.py and understand the code.

7. user_role.py --> messaging.py --> upload.py --> message-processor.py

8. Run the app using `python run.py` and verify all the routes.

9. After uploading the file, check for records in the `document_data table`.
   Also after adding a user-role, check for the records in the `user_role_map` table.
   using `select * from document_data;`
          `select * from user_role_map;`






