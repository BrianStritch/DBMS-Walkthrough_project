# __DBMS WALKTHROUGH PROJECT__
## __WITHIN EACH FILE ARE ADDITIONAL NOTES RELEVANT TO THEM FILES__

### __Languages and technologies used__
- Flask
- Psycopg2
- python
- CRUD Database technology

### __Additional notes__
 - linting warnings are not always technically accurate, so to stop the warnings, we can
    add a comment at the end of each line, # noqa for 'No Quality Assurance'

## __Basic technologies you need to install__
  - __in the terminal window__
   - pip3 install Flask-SQLAlchemy psycopg2
      - By installing Flask-SQLAlchemy, this actually comes with both Flask and the SQLAlchemy requirements together in one download.
  - __in the __ init __ .py file__
   - We will start by importing the following:
     - import os 
     - from flask import Flask
     - from flask_sqlalchemy import SQLAlchemy

    
# __STAGE 1 Putting the Basics into Place__

## __ env.py __
 - touch env.py 
   - Next, we will be storing some sensitive data, and we need to hide them using environment
        variables hidden within a new file called 'env.py'.
   - make sure your env.py file is in your gitignore folder 
 - in env.py we need to import os

## __ taskmanager application , folder and init.py file__
 - the entire application will need to be its own Python package, so to make this
    a package, we need a new folder which we will simply call taskmanager/.
    Inside of that, a new file called          __ init __.py  (no spaces between underscores and name)
 - This will make sure to initialize our taskmanager application as a package, allowing us to use
    our own imports, as well as any standard imports.
 - 

## __routes.py__
 - Now we can create the new 'routes.py' file within our taskmanager package.
    We're going to start using some Flask functionality, so we can import render_template from flask to start with.


## __run.py__
 - Now it's time to create the main Python file that will actually run the entire application.

## __templates__
 - we need to render some sort of front-end template to verify that the application is running successfully.
    Within our taskmanager package, let's create a new directory called 'templates', which
    is where Flask looks for any HTML templates to be rendered.
    Then, within this templates directory, we will create a new file called base.html, which
    is what will be rendered from our routes.py file.
- We can type python3 run.py in order to launch our main file, which will import the necessary taskmanager package 
    and all of its dependencies we've specified.

## __End of stage 1__
 - We've learned how to set up a basic Flask application using the Flask-SQLAlchemy package.

# __STAGE 2 Creating the Database__

## __models.py__
 - We'll start by creating a new file called models.py within our taskmanager package.
  - see numbered notes in file for details, numbered in order of code writing

## __ back to routes.py __
 - At the top of the routes file, we need to import the classes from models in order to generate our database next.

## __taskmanager database__  and __Migrating your database__
- we've specified that our database will be
   called 'taskmanager', not to be confused with our 'taskmanager' Python package.
   This would be similar to the 'chinook' database we created in the previous lessons, so we
   will need to also create this 'taskmanager' database.
   Let's navigate to the Terminal, and login to the Postgres CLI by typing 'psql' and hitting enter.
   To create the database, we can simply type:
   CREATE DATABASE taskmanager;
   Once that's created, we'll switch over to that connection by typing:
   \c taskmanager;
   We don't need to do anything else within the Postgres CLI now that we have the database
   created, so let's come out of the CLI by typing \q.

- Next, we need to use Python to generate and __migrate__ our models into this new database.
   This will take the models that we've created for Category and Task, and build the database
   schema using the details we've provided.
   It's important to note, that if you were to modify your models later, then you'll need
   to migrate these changes each time the file is updated with new context.
   For example, __if you added a new column on the Task table for 'task_owner', once the__
   __file is saved, you'll need to make your migrations once again, so the database knows about these changes.__
   __To migrate your database follow these steps__
   - Let's go ahead and access the Python interpreter by typing "python3" and enter.
      From here, we need to import our 'db' variable found within the taskmanager package, so type:
      from taskmanager import db
      Now, using db, we need to perform the .create_all() method:
      That's it, pretty simple enough, our Postgres database should be populated with these two
      tables and their respective columns and relationships.
      Let's exit the Python interpreter by typing exit().



