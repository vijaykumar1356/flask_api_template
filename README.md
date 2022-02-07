# koshex-poc
URL Shortner Service

## Instructions to Setup this Project
  1. Create a free account in https://app.bitly.com/
     1. go to Profile Seaction -> Settings -> Under Developer Settings Click on API
     2. Enter Your Password and Generate Access Token -> keep it with you.
  2. Clone this repo to your local machine using the command `git clone git@github.com:vijaykumar1356/koshex-poc.git`
  3. come to koshex-poc directory `cd koshex-poc` 
  4. create a `.env` file in the project directory and add the data format mentioned in `.env_sample` file
     1. the Bitly Access TOken is must to run this project, have it in env file.
     2. The Database URI in .env file is optional with out it as well the project run with sqlite3 inmemory database. If you have a postgres database created under any owner, just add the Database URI in the format mentioned in `.env_sample`
  5. If Virtualenv package doesn't exist -> run this command `pip3 install virtualenv`
  6. Create a Virtual Environment using the command `python3 -m virtualenv env`
  7. activate virtual environment using `source env/bin/activate`
  8. Now install all the dependencies using the command `pip install -r requirements.txt`
  9. To run database migrations
     1. from the terminal type `export FLASK_APP=src`
     2. then run the command `flask db upgrade`
  10. To run the server you can do either of the following approaches.
     * ### Approach 1
       * from the terminal type `export FLASK_APP=src`
       * also type `export FLASK_ENV=development`
       * now run the server using `flask run`
     * ### Approach 2
       * from the terminal type `python run.py`
   1. Hopefully now the server is up and running.

## API information   
1. POST `/api/shortener`
   1. payload format example
   2. ```{"long_url": "https://www.youtube.com/watch?v=ZxCUnxwR89Q"}```
   3. It will create a short url and api response will return
2. GET `/api/shortener` 
   1. This will fetch all database records so far created for URL shortner service and return them
3. GET `/api/shortener?short_url=https://bit.ly/3J75wed`
   1. This will return shortener URL and its original long URL and total clicks registered for that short URL so far.
4. GET `/api/search?keyword=example`
   1. This will query all the database with the keyword and return the results with meta data