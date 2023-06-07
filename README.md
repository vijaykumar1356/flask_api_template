# koshex-poc
URL Shortner Service

## Instructions to Setup this Project
  1. create a `.env` file in the project directory and add the data format mentioned in `.env_sample` file
     
  2. If Virtualenv package doesn't exist -> run this command `pip3 install virtualenv`
  3. Create a Virtual Environment using the command `python3 -m virtualenv venv`
  4. activate virtual environment using `source env/bin/activate`
  5. Now install all the dependencies using the command `pip install -r requirements.txt`
  6. To run database migrations
     1. from the terminal type `export FLASK_APP=src`
     2. then run the command `flask db upgrade`
  7. To run the server you can do either of the following approaches.
     * ### Approach 1
       * from the terminal type `export FLASK_APP=src`
       * also type `export FLASK_ENV=development`
       * now run the server using `flask run`
     * ### Approach 2
       * from the terminal type `python run.py`
   1. Hopefully now the server is up and running.
