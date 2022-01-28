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

## __back to routes.py __
 - At the top of the routes file, we need to import the classes from models.py in order to generate our database next.

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
   - To test that the tables exist in your database you type into the terminal:
       - psql -d taskmanager
       - \dt 
       this should list the tables in the console.
       like this:
        -   Schema |   Name   | Type  | Owner  
        -   --------+----------+-------+--------
        -   public | category | table | gitpod
        -   public | task     | table | gitpod
        -   (2 rows)

## __end of stage 2__
 - we've set up our tables and created and migrated our database

# __STAGE 3 Template Inheritance__
 In the last stage, we managed to get our database schema created and migrated to Postgres.
   Before we can do any data manipulation using CRUD functionality, we need some sort of front-end
   user interface to interact with the database.

 - If you recall from the previous lessons using Flask on the Thorin project, we used something called template inheritance.
   This allows us to extend various HTML templates, to avoid duplicating code, such as a navbar
   or footer that's identical across all pages.
   Also, in the introduction video, we discussed the use of a CSS framework called Materialize,
   which we will be using throughout this project.
   This will allow us to make use of their responsive behaviors using the grid system, similar to
   Bootstrap, and various components to make our application more user-friendly.

 - At the time of recording, the latest version of Materialize is 1.0.0 as you can see in the top-left corner of their site. 
## __setting up Materialize__
 - The first thing that we need to do, is to grab the CDN link and script tags from the 'Getting Started' page.    
     - We'll paste the CSS link within our base template head element,
      - <!-- Compiled and minified CSS -->
      - <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
     - and then paste the JavaScript script tag at the bottom of our body element.
      - <!-- Compiled and minified JavaScript -->
      - <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
### __static__
  - In addition to using Materialize, we are going to incorporate some of our own custom CSS and JavaScript.
      When using a templating language such as Flask, any assets that we use such as images, CSS,
      and JavaScript, need to be stored in a directory called 'static'.
     
  - Let's create this new folder within our taskmanager package, 
      - we'll also want to add the css/ and js/ folders within this static directory.
      - As with tradition, we'll call our CSS file 'style.css', and our JavaScript file 'script.js' in their respective folders. 
### __back to base.html__ 
  - Now, in order to link to any static file that we have, it's important to note that we must use the correct syntax.
      You should be rather familiar with just adding the standard front-end method.
      However, with templating languages, this method can cause errors or the files not loading properly.
      We must use double curly brackets, and then use the 'url_for()' method, which takes two values.
      The first value is the 'static' directory, so it knows to look within this main folder.
      Separate the values with a comma, then we need to use filename='css/style.css', and
      make sure to watch out for the double vs single quotes.
      As you can see, I'm using the double-quotes to wrap the entire href property.
      Then, for anything within the href, I've used single-quotes, because by using double-quotes
      again, it will think that our href is finished, and throw a syntax error.

  - Let's do the same exact thing for our JavaScript file.
      The script source will use double-quotes, wrapping everything in double curly-brackets,
      and the url_for() method points to our static file in single-quotes.
      Then, a comma to separate the filename, which is equal to 'js/script.js' in single-quotes,
      pointing to our js/ folder and the file itself.
      You don't need to use this method for any external CDN links, such as the Materialize links for example.
      It's only needed for any files that we actually own within our workspace or project, including images.
      This is due to the fact that you’re working with a framework, which relies on using “url_for()”
      methods to find the relevant files locally to your own project.

   - You don't need to use this method for any external CDN links, such as the Materialize links for example.
      It's only needed for any files that we actually own within our workspace or project, including images.
      This is due to the fact that you’re working with a framework, which relies on using “url_for()”
      methods to find the relevant files locally to your own project.
      Also, quite often when working with a templating language, if you make changes to your CSS
      or JavaScript files, and then reload the page, it might not show your changes.
      This is very likely an issue to do with caching, so here are three steps to always remember to check.
       - First, try a hard-reload, which is generally CTRL+SHIFT+R in most cases, but depending
         on your computer and which browser you use, it could be one of these combinations on screen.

       - Second, if that doesn't work, open a new Incognito window with your project URL, and if you do
         see the changes, it's certainly a caching issue, since Incognito doesn't store cache.
      
      - Finally, if neither of those options work, stop the application in your terminal from
         running, and just restart it. __by holding CTRL and C__ in the terminal where flask is running and then restarting
         flask with __python3 (filename.py)run.py__

    - This may sound asinine, but quite often with Flask and Django, a fresh restart of the app
      is required to take effect of any new additions to your code.

   #### __HEADER__
    - __NAVBAR__ Now that we have our static files connected to the base template, let's start adding a
         few components, such as a navbar.
         - From the Materialize docs, click on Components to expand it, then click Navbar.
           We'll be using the Mobile Collapse option, which will make a responsive navbar for smaller screens.
         - Copy the code, and let's paste this within a header tag, which will replace our text of 'Hello World'.
           The reason why it shows the unordered list twice, is because one is for the navbar on
           the top of the page, and the other is for our mobile side navbar.
         - __NAVBAR LINKS__
          - For the logo, we'll just call the project Task Manager, and have it load our main page when clicked.
               Similar to our static files, we need to use the url_for() method for any links within our project.
               Double curly-brackets, url_for(), and then in single-quotes the name of our Python function to call, which is 'home'.
               If you recall from our routes.py file, this is the only route that we've created so far,
               and we've called it 'home', which will render the base.html template.
               We don't need to include the 'static' or 'filename' properties, since this is calling an actual function.
               Again, using this approach is very important, so if you only type href="base.html", then
               your project won't compile properly by Flask, and you'll likely get an error.
          - We're going to have 3 links within our navbar, so we'll remove their sample links.
               These links will be: Home, New Task, and Categories.
               We already have the function created for our 'Home' link, so we can copy that, and paste it within the hrefs.
               Since we haven't created the other two functions or routes yet, then we cannot include those as placeholder links.
               If we try to load the site using placeholder links, Flask will throw an error saying that
               it can't find the intended function you're attempting to call.
         __SIDENAV__
            - For the mobile menu icon, the Materialize docs include Google's Material Design icons,
                  so you're welcome to those as well, but be sure to include the CDN link from the 'Icons' page.
                  However, Font-Awesome contains over a thousand more icons to choose from, so I'll include
                  the Font-Awesome CDN link from the CDNJS library site.
                  I'll copy the link tag, and paste it within my head element before the Materialize CDN
                  link, then replace the menu icon with a Font-Awesome icon instead.
                     - <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

            - Next, even though we don't have the Python functions created, I'm going to duplicate
                  the Home link, and create empty links for the others now.
                  The second link will be for adding a New Task, and the final link will be for all Categories.
                  Remember, these need to be blank href links for now, so we'll delete the paths, and then
                  we can go ahead and copy these two new links, then paste them below in the sidenav list.
               
         - __SIDENAV FUNCTIONALITY__ 
            - In order for the sidenav to work, we need to initialize the JavaScript functionality from Materialize.
                  Let's copy the initialization code, either the vanilla JavaScript snippet, or if you're
                  using jQuery, the snippet below, then let's paste it within our script.js file.
                  We are actually going to be using a few different elements from Materialize, so let's give our
                  variables a more unique name.
                  The querySelector will be 'sidenav', and then we'll just initialize that without defining any variable.
         
   #### __FOOTER__
    - Before we create any template that extends this, we'll quickly add a Materialize footer.
         Paste the footer below the main element, and you can style this any way you'd like,
         but I'll keep it simple and clean by removing some unnecessary bulk.
         It'll be 'blue darken-3', removing the container link section, adding 'For educational purposes
         only', then a link to Code Institute in a new blank tab.
         Since we've been using semantic HTML elements such as header, nav, main, and footer, we
         can simply force the footer to stay at the bottom of the page by using the 'Sticky Footer' CSS code.
         Paste that into your CSS file, and this will make the footer always stay at the bottom
         of the page, no matter how much or how little content is on each page.

   #### __TEMPLATE INHERITANCE WITH FLASK__      
      - __flask injected content__      
         -  The next section will be where all of our main content will be injected, so we'll use
               the Template Inheritance {% block %} element.
               Let's wrap this inside of a semantic main element with the Materialize class of 'container'.
               In exactly the same way that we did on our previous Flask lessons, we'll call this block
               element 'content', making sure to close the {% endblock %} tag as well.

         - Now we can start using the template inheritance functionality, and extend our base template across various files.
         __CREATE TEMPLATES IN TEMPLATES DIRECTORY__
          - Let's create a new template in the templates directory, and call it __'tasks.html'__, which
               is where we will display any task that will be stored within our database later.

          - This will use the {% extends %} block, which will extend our base.html template.
               This means that by extending from the base template, anything created on our base template
               will display on this page as well, which includes our navbar and footer.
               Then, we'll inject anything from this tasks template into the 'content' block element,
               making sure to close the {% endblock %} as well.

          - We will add the content for this page in a later video, so for now, let's simply just
               add an h3 element for 'Tasks', with some of the Materialize helper classes.

### __Back to routes.py__
 - Finally, let's go back to our routes.py file, and update the rendered template to be 'tasks.html' instead.
 
 - This will become our home page now, so that when a user visits our site, they're brought
      to the tasks page, which will automatically extend all of the content from our base template.

         
## __end of stage 3__
   - Save all of your files, and if your app isn't currently running, go ahead and start it within
      the terminal by typing 'python3 run.py' and then open your browser.
   - We now have the basic front-end template set up with a navbar, a footer, and a tasks template
      that uses Template Inheritance to extend from the base file.



