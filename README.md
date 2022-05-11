# sqli-example
Quick showcase for SQL Injection with a Flask site and SQLiteDB

># Setup
>1. Clone this repository
>   
>2. Setup python virtual environment  
python3 -m venv venv
>  
>3. . venv/bin/activate
>  
>4. pip install -r requirements.txt
>
>5. Run run.py  
python run.py
  
# Usage
This is a simple web application which takes in a user's name, and adds it to a database. The insert statement is suspectable to SQL Injection.  
Example: '); DELETE from users where name='asdf'; --
