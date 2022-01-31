# __DBMS WALKTHROUGH PROJECT__
#### __WITHIN EACH FILE ARE ADDITIONAL NOTES RELEVANT TO THEM FILES__

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

    
## __STAGE 1 Putting the Basics into Place__

##### __ env.py __
 - touch env.py 
   - Next, we will be storing some sensitive data, and we need to hide them using environment
        variables hidden within a new file called 'env.py'.
   - make sure your env.py file is in your gitignore folder 
 - in env.py we need to import os

##### __ taskmanager application , folder and init.py file__
 - the entire application will need to be its own Python package, so to make this
    a package, we need a new folder which we will simply call taskmanager/.
    Inside of that, a new file called          __ init __.py  (no spaces between underscores and name)
 - This will make sure to initialize our taskmanager application as a package, allowing us to use
    our own imports, as well as any standard imports.
 - 

##### __routes.py__
 - Now we can create the new 'routes.py' file within our taskmanager package.
    We're going to start using some Flask functionality, so we can import render_template from flask to start with.


##### __run.py__
 - Now it's time to create the main Python file that will actually run the entire application.

##### __templates__
 - we need to render some sort of front-end template to verify that the application is running successfully.
    Within our taskmanager package, let's create a new directory called 'templates', which
    is where Flask looks for any HTML templates to be rendered.
    Then, within this templates directory, we will create a new file called base.html, which
    is what will be rendered from our routes.py file.
- We can type python3 run.py in order to launch our main file, which will import the necessary taskmanager package 
    and all of its dependencies we've specified.

##### __End of stage 1__
 - We've learned how to set up a basic Flask application using the Flask-SQLAlchemy package.

## __STAGE 2 Creating the Database__

##### __models.py__
 - We'll start by creating a new file called models.py within our taskmanager package.
  - see numbered notes in file for details, numbered in order of code writing

##### __back to routes.py __
 - At the top of the routes file, we need to import the classes from models.py in order to generate our database next.

##### __Taskmanager database__  and __Migrating your database__
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

##### __end of stage 2__
 - we've set up our tables and created and migrated our database

## __STAGE 3 Template Inheritance__
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
##### __setting up Materialize__
 - The first thing that we need to do, is to grab the CDN link and script tags from the 'Getting Started' page.    
     - We'll paste the CSS link within our base template head element,
      - <!-- Compiled and minified CSS -->
      - <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
     - and then paste the JavaScript script tag at the bottom of our body element.
      - <!-- Compiled and minified JavaScript -->
      - <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
##### __static__
      - In addition to using Materialize, we are going to incorporate some of our own custom CSS and JavaScript.
            When using a templating language such as Flask, any assets that we use such as images, CSS,
            and JavaScript, need to be stored in a directory called 'static'.
         
      - Let's create this new folder within our taskmanager package, 
            - we'll also want to add the css/ and js/ folders within this static directory.
            - As with tradition, we'll call our CSS file 'style.css', and our JavaScript file 'script.js' in their respective folders. 
##### __back to base.html__ 
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
###### __note:__

         - You don't need to use this method for any external CDN links, such as the Materialize links for example.
            It's only needed for any files that we actually own within our workspace or project, including images.
            This is due to the fact that you’re working with a framework, which relies on using “url_for()”
            methods to find the relevant files locally to your own project.
            Also, quite often when working with a templating language, if you make changes to your CSS
            or JavaScript files, and then reload the page, it might not show your changes.
            This is very likely an issue to do with caching, so here are three steps to always remember to check.

###### __hard reset__

         - First, try a hard-reload, which is generally CTRL+SHIFT+R in most cases, but depending
            on your computer and which browser you use, it could be one of these combinations on screen.

         - Second, if that doesn't work, open a new Incognito window with your project URL, and if you do
            see the changes, it's certainly a caching issue, since Incognito doesn't store cache.

         - Finally, if neither of those options work, stop the application in your terminal from
            running, and just restart it. __by holding CTRL and C__ in the terminal where flask is running and then restarting
            flask with __python3 (filename.py)run.py__

         - This may sound asinine, but quite often with Flask and Django, a fresh restart of the app
            is required to take effect of any new additions to your code.

   ##### __HEADER__
   ###### __NAVBAR__ 
         - Now that we have our static files connected to the base template, let's start adding a
           few components, such as a navbar.
         - From the Materialize docs, click on Components to expand it, then click Navbar.
           We'll be using the Mobile Collapse option, which will make a responsive navbar for smaller screens.
         - Copy the code, and let's paste this within a header tag, which will replace our text of 'Hello World'.
           The reason why it shows the unordered list twice, is because one is for the navbar on
           the top of the page, and the other is for our mobile side navbar.
   ###### __NAVBAR LINKS__
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
   ###### __SIDENAV__
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
               
   ###### __SIDENAV FUNCTIONALITY__ 
            - In order for the sidenav to work, we need to initialize the JavaScript functionality from Materialize.
                  Let's copy the initialization code, either the vanilla JavaScript snippet, or if you're
                  using jQuery, the snippet below, then let's paste it within our script.js file.
                  We are actually going to be using a few different elements from Materialize, so let's give our
                  variables a more unique name.
                  The querySelector will be 'sidenav', and then we'll just initialize that without defining any variable.
         
   ##### __FOOTER__
    - Before we create any template that extends this, we'll quickly add a Materialize footer.
         Paste the footer below the main element, and you can style this any way you'd like,
         but I'll keep it simple and clean by removing some unnecessary bulk.
         It'll be 'blue darken-3', removing the container link section, adding 'For educational purposes
         only', then a link to Code Institute in a new blank tab.
         Since we've been using semantic HTML elements such as header, nav, main, and footer, we
         can simply force the footer to stay at the bottom of the page by using the 'Sticky Footer' CSS code.
         Paste that into your CSS file, and this will make the footer always stay at the bottom
         of the page, no matter how much or how little content is on each page.

   ##### __TEMPLATE INHERITANCE WITH FLASK__      
   ###### __flask injected content__      
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

##### __Back to routes.py__
      - Finally, let's go back to our routes.py file, and update the rendered template to be 'tasks.html' instead.
      
      - This will become our home page now, so that when a user visits our site, they're brought
            to the tasks page, which will automatically extend all of the content from our base template.

         
##### __end of stage 3__
      - Save all of your files, and if your app isn't currently running, go ahead and start it within
         the terminal by typing 'python3 run.py' and then open your browser.
      - We now have the basic front-end template set up with a navbar, a footer, and a tasks template
         that uses Template Inheritance to extend from the base file.

## __STAGE 4 CREATE - Adding Categories__
 - Before we can start adding tasks to our database, we first need to have some functionality that handles the categories.
   If you recall from when we built the database schema in a previous video, each Task must
   have a Category assigned, which makes it the foreign key to the Category model.
   In this video, we'll build a front-end template that then allows us to add new categories to the database.
 ##### __Adding categories__
      - Let's start by creating a couple new templates; categories.html and then another template called add_category.html.
            Both of these files will of course be extended from the base template, and have their code
            injected into the 'content' {% block %}, so we can simply copy/paste from the 'tasks' template.
            Then, update the
            title for each, which will be "Categories" and "Add Category".
##### __categories.html__
   For now, we aren't going to focus on viewing each of the categories

      - we do need a button that will bring us to the form to add a new category.
            To make this responsive, we'll use the Materialize grid helper classes and layout.
            First, start with a row, which has a column that spans all 12 spaces, and is center-aligned.
            Within this column, we'll add a link that will use the Materialize 'btn-large' class,
            which will make it a larger button than their default button size.
            It will also have some helper color classes to make it light-blue and darken-2.
            The link will be "Add Category", and include an icon of your choosing, so I'll add a generic Font-Awesome 'plus' symbol.
            As for the href, since we'll be targeting a file within our own project, we must use
            the double curly-brackets and url_for() method.
            We haven't built this function yet, but let's go ahead and assign the URL to be 'add_category'.
##### __back to routes.py__
      - Let's then open the routes.py file, and create some functions that will generate these templates.
            In our navbar, we have a link for "Categories", so we need a function that will populate the
            new categories template that we've just created.
            The app route will be "/categories", and for the function name itself, that will be consistent,
            so we'll also call that "categories".
            Whenever you use the url_for() method on your links, it's important to note that these are
            calling the actual Python functions, not the app.route, even though these are often the same name.
            For now, we don't have any data from the database yet, so we can simply just return the rendered template of 'categories.html'.

##### __back to base.html__
       - Let's quickly link that navbar button to this function, so open your base.html template, and find the navbar links.
            Copy the href for our 'Home' link, and paste it within the href for 'Categories'.
            Since our new function is called 'categories', let's update this to reflect that, and then
            we can copy this new href and paste it below into the mobile sidenav link.

##### __back to routes.py__
       - Go back to the routes.py file, and now we'll create a new route that will render our template for adding a new category.
            The app route will be "/add_category", and this time we need to include a list of the
            two methods "GET" and "POST", since we will be submitting a form to the database.
            Our function name will match 'add_category', which, if you recall, is the same name we
            added to the link href to target this function that we're creating now.
            When a user clicks to add a new category, it should render the template that contains
            a form, and by displaying the form to users, this uses the "GET" method to 'get' the page.
            We can copy the render template line from one of the functions above, and just replace
            the template name with 'add_category.html'.

       -  However, when a user eventually submits this form, the form will attempt to 'post' the
            data into the database, and this is why we need to specify both methods in the app route.
            Don't worry about this part too much right now, because we will come back to this function
            later, and go into a bit more detail.

Now that the basic routes are created for each template, start the application in your
terminal using python3 run.py, just to confirm everything is working fine.
Clicking on the Categories button in our navbar opens up the 'categories.html’ template,
and shows the 'Add Category' button, so let's click that.

##### __back to models.py__
   -let's go ahead and start building the form to allow users to add a new category to the database.

__go to materialize website to obtain code block for form__

       - Taking a look at our Category model, the only real form element we need to collect is the
            'category_name', since the ID will be set by default, and 'tasks' gets applied behind the scenes.
            Let's navigate to the Materialize page under 'Forms' called 'Text Inputs', and copy the entire code snippet provided.

##### __add_category.html__            

          - We'll paste that within the 'add_category.html' template, and let's remove all but one input row.
            If you recall from the introduction video, one of the Materialize components is a 'card',
            and there are a few different card types to choose from.
            We don't need anything fancy at this stage, so we'll just utilize the 'card-panel' class
            for a basic card motif, and apply that to the main 'row'.
            I'm also going to apply a light grey color to the card, just so it stands out a bit more on our white background.
            The form itself will use the "POST" method once submitted, and for the action, that's
            going to point back to the same function of 'add_category'.
            Let's make sure this input spans all 12 spaces on the grid, so update the column class from 's6' to 's12'.
            If you wanted the input to have an icon before the box, then we can simply use the 'prefix'
            class on an icon, using any icon you'd like.
            In order for Python to recognize the form data, we need to use the name-attribute, and
            it's considered best practice to have the name, ID, and label-for all matching.
            This box will be for our 'category name' field on the database, so let's call it 'category_name'
            for each of those, removing the placeholder text as well.
            Then, let's make this field required, and add a minimum length of 3, with a max length of 25.
            After the row for our category_name, let's add one more row, with a column spanning 12
            spaces once again, and this time it will be center aligned.
            This will be for our submit button on the form, and we're going to give it a class of
            'btn-large' plus any Materialize color class you'd like.
            The button will read 'Add Category', and I'm going to add another Font-Awesome icon here
            on the right-hand side of the button.
            We're actually finished with this template now, it's fairly short, but if we attempt
            to submit the form, it will not work, due to the fact that we haven't created the POST method yet.
##### __back to routes.py__
 - Let's return to the route.py file, and now we can add the POST method functionality for
users to add a new category to the database.

       - If the requested method is equal to POST, then we will create a new variable called
            'category', which will be set to a new instance of the Category() model imported at the top of the file.
            By using the 'request' method, we need to also import that from Flask at the top here.
            We need to make sure that this Category model uses the same exact keys that the model is
            expecting, so when in doubt, copy from the model directly.
            For this category_name field, we can then use the requested form being posted to retrieve the name-attribute.
            This is why it's important to keep the naming convention consistent, which means our name-attribute
            matches that of our database model.            

       - Once we've grabbed the form data, we can then 'add' and 'commit' this information to the
            SQLAlchemy database variable of 'db' imported at the top of the file.
            This will use the database sessionmaker instance that we learned about in some of the previous videos.
            After the form gets submitted, and we're adding and committing the new data to our database,
            we could redirect the user back to the 'categories' page.
            We'll need to import the 'redirect' and 'url_for' classes at the top of the file from our flask import.

###### __end of stage 4__
       - That completes our function, so let's quickly recap what's happening here.
            When a user clicks the "Add Category" button, this will use the "GET" method and render the 'add_category' template.
            Once they submit the form, this will call the same function, but will check if the request
            being made is a “POST“ method, which posts data somewhere, such as a database.
            Anything that needs to be handled by the POST method, should be indented properly within this condition.
            By default, the normal method is GET, so it will behave as the 'else' condition since
            it's not part of the indented POST block.
            If you wanted to, technically you could separate this into two separate functions, which would
            handle the GET and POST methods completely apart.
            Also, in a real-world scenario in a production environment, you'd probably want to consider
            adding defensive programming to handle brute-force attacks, along with some error handling.
            But for now, it's the moment of truth, so go ahead and save all of your files, and start
            the application in the terminal if it isn’t running anymore.
            After that loads, navigate to the Categories page, and then click on the button to add a new category.
            I'm going to call my category 'Travel', and hit the button to submit the form.
            As you can see, the page submits, and redirects me back to the Categories page without any errors.
            Assuming that worked properly due to the fact that there weren't any errors, it should've
            added "Travel" to the database.
            Currently, we have no way to verify that submitted properly, unless we access the Postgres database on the CLI.
            Instead of using the CLI, in the next video, we are going to learn how to extract data
            from the database, and display it to our users.

###### __Important note__
 - when i was trying to add a category it was throwing an error where the database was not found. i had to exit the flask, set_pg, open psql, exit psql, and then reload flask. this then allowed it to work.

## __Stage 5 READ - reading the categories we have added.__
In the last stage we managed to add a new category into our database, which is just one part of performing CRUD functionality.
The C in CRUD means to Create, by creating a new category and having it post to the database.
In this stage we are going to focus on the R in CRUD, which means to Read from the database.

If your application isn't currently running, go ahead and start it in the terminal by typing 'python3 run.py' and navigate to the Categories page from the navbar. On this page, we'd like to retrieve all of the categories listed in the database, and
display them to our users here. Currently, from the previous stage, we've only added a single category so far, which
was "brian", but we don't see it displayed here yet.

From the introduction video, we mentioned the Materialize 'card' component, and we used
the card class in the last video on our form.
This time, we are going to include some buttons in the card, and we need to use a different
version of the card component, so let's head over to the Materialize site.

###### __Materializecss.com website__
      - From the Cards page within the Materialize components, we are going to use the Basic Card at the top, which already comes 
         with two links.

###### __back to categories.html__
      - just underneath the row that contains the 'Add Category' button.
            The current grid sizes listed from this code show that the card will display across the
            entire screen on small devices, and only half the screen on medium devices and up.
            We don't necessarily need the cards to be that big on larger devices, so let's add another grid class of 'l3'.
            This means, for larger devices, the card should occupy 25% of the parent element, since the
            number of spaces available per row is 12, and means it can contain 4 cards per row.
            We can design the card however we'd like, so choose any color combination from the helper
            color classes, making sure that your text and background don't contrast each other.
            Also, since this will only contain the name of the category itself, then I'm going to
            add the helper class of 'center-align', and remove the paragraph tag entirely.

       - We aren't finished yet, but let's save the file, and reload the page to see how things are looking.
            As you can see, the card is indeed spanning only 25% of the parent element, which, if
            you recall, is our main-container class from the base template.
            If we check the responsiveness using the Developer Tools, the card flows smoothly, only spanning
            50% of the width on medium devices, and on smaller devices, the entire width.
            However, if you notice, the links that we have so far are rather squashed, and this
            happens when the content in those links are too long, but the card is set to specific size.
            For this project, these links will actually become buttons, and the text will be much
            shorter, since they will be the buttons for Editing and Deleting our categories later.
            Let's go back to the workspace, and update those links accordingly.
            The first link will be 'Edit', and the second link will be 'Delete'.
            I mentioned that these will be buttons instead of links, so let's apply the Materialize class
            of 'btn' to make these styled like buttons.
            We will then style the buttons using more of the Materialize helper classes, just make
            sure the background and text don't have color contrast issues.
            Now, it's time to start building the code that will extract the data from within our
            database, so let's head over to the routes.py file.

###### __back to routes.py__
       - In the previous video, we added a temporary placeholder route, which allows us to pull
            up the categories template itself.
            All we need to do here now, is add some code to query the database so we can use that within our template.
            First, let's define a new variable within the categories function, which will also be
            called categories to keep things consistent.
            We just need to query the 'Category' model that is imported at the top of the file from
            our models.py file, and we can do that by simply typing:
            Category.query.all()
            Sometimes though, categories might be added at different times, so this would have the
            default method of sorting by the primary key when things get added.
            Let's go ahead and use the .order_by() method, and have it sort by the key of 'category_name'.
            We also need to make sure that we tell it the specific model as well, even though it
            might seem redundant, it's possible to use other sorting methods.
            You need to make sure the quantifier, which is .all() in this case, is at the end of the
            query, after the .order_by() method.
            Whenever we call this function by clicking the navbar link for Categories, it will query
            the database and retrieve all records from this table, then sort them by the category name.
            Now, all that's left to do here is to pass this variable into our rendered template,
            so that we can use this data to display everything to our users.
            By using the .all() method, this is actually what's known as a Cursor Object, which is
            quite similar to an array or list of records.
            Even if the result comes back with a single record, it's still considered a Cursor Object,
            and sometimes Cursor Objects can be confusing when using them on front-end templates.
            Thankfully, there's a simple Python method that can easily convert this Cursor Object
            into a standard Python list, by wrapping the variable inside of 'list()'.
            You might be slightly confused as to what 'categories=categories' represents, so let's quickly explain this part.
            The first declaration of 'categories' is the variable name that we can now use within the HTML template.
            The second 'categories', which is now a list(), is the variable defined within our function
            above, which is why, once again, it's important to keep your naming convention quite similar.
            Perfect, now that we have this template variable available to us, let's go back to our categories.html

###### __back to categories.html__
       - let's go back to our categories.html template, and start incorporating it into our cards.
            Eventually, we are going to have more than one category listed here, but so far we've
            only added the single category of 'brian'.
            However, let's prepare the code to recognize multiple cards, by using the Jinja syntax of a for-loop.
            We don't want each card to stack on top of each other, but instead, to flow within the
            same row, each having their own column.
            Make sure to add the for-loop just inside of the row, so everything within the row is repeated and looped.
            The closing {% endfor %} should be just after the div for this column, so follow that down,
            and add the closing element there.
            Similar to JavaScript, we need to define a new index for each iteration of this loop,
            so to keep things consistent, we will call ours 'category'.
            This means that for each 'category' in the ‘list of categories' being passed over from
            our Python function, it will generate a new column and card.
            Finally, we need to display the actual category name that's stored within our database, so
            we can update the card-title.
            Since we are within a for-loop, we need to use the newly defined index variable of 'category'.
            We also need to use dot-notation and tell it which key should be printed here, so in
            this case, it should be 'category.category_name', which means, “this category’s key of category_name”.
            If you wanted to show the primary key instead, that's stored within our database as 'id',
            so it would be 'category.id' for example.
###### __End of stage 5 __
         That's all there is to it, so make sure all of your files are saved now, then go ahead
         and reload the preview page.
         Wonderful, you can see that we now have a card for the 'Travel' category that we added
         in the previous video, which confirms that it was indeed added successfully.
         Let's go ahead and put that to the test, by adding a few more new categories now.
         Pause the video, and add some of your own custom Categories.
         Welcome back, I hope you managed to add a few more categories to your database, like
         you can see I have here on the screen now.
         As you can see, each category is successfully adding to the database, as well as displaying
         the card for each one, and sorting them alphabetically by the category name.
         We have now covered 50% of CRUD functionality, allowing users to Create and Read records from the database.
         In the next video, we are going to focus on the U in CRUD, which will allow users to Update
         the category name by clicking the 'Edit' button.


## __Stage 6 UPDATE - update the categories__

###### __edit_category.html__
    - The first thing we need to do is make a duplicate copy of the 'add_category' template, and let's
         rename this to 'edit_category.html' instead.
         Anywhere that you see 'Add Category' on this template, go ahead and replace that with 'Edit Category',
         which should be a total of three times, plus a quick update to the icon.
         The form is almost complete, but if you notice, the form's action attribute is pointing to
         a new function called 'edit_category', which we haven't created yet.
         Let's go over to the routes.py file, and we are going to create a new function.

###### __back to routes.py__
     - For the app route URL, let's call this "/edit_category", and once again, we will be using this as a
         dual-purpose for both the "GET" and "POST" methods.
         The function name will match, so that will be "edit_category".
         To start with, we will only focus on the "GET" method, which will get the template, and render it on screen for us.
         We can simply return render_template using the new file we created, "edit_category.html".
         However, we need some sort of mechanism for the app to know which specific category we intend to update.

###### __back to categories.html__
    - let's open the template for all categories, which contains
         the for-loop we built in the last video.
         If you recall, within this for-loop, we have the variable of 'category' that is used for
         each iteration of this loop, and we have targeted the 'category_name' field.
         Due to the fact that our 'Edit' and 'Delete' buttons are still within the for-loop, we
         can use that variable to identify the specific category primary key using '.id'.
         Let's go ahead and create the href url_for() method, which will be wrapped in double curly-brackets.
         This behaves in the same way that we called the navbar links, or the CSS and JavaScript
         files from within our static directory.
         In addition to calling our new 'edit_category' function, we need to pass another argument
         to specify which particular category we are attempting to update.
         Make sure you add a comma after the single-quotes, which identifies that we are calling the function with some data included.
         For the argument name, it can be whatever we'd like, and since we need to use something
         unique, it's best to use the primary key of the ID.
         I'm going to call this 'category_id', and we can now set that equal to the current 'category.id' using dot-notation again.
         Since we originally added the 'brian' category as the first record on our database, its ID will be '1'.
         Now, we can head back over to the routes.py file.

###### __back to routes.py__
    -  since we've given an argument of 'category_id' when clicking the 'Edit' button, this also needs 
         to appear in our app.route. These types of variables being passed back into our Python functions must be wrapped
         inside of angle-brackets within the URL. We know that all of our primary keys will be integers, so we can cast this as an 'int'. We also need to pass the variable directly into the function as well, so we have the
         value available to use within this function. If you have attempted to save these changes and load the page, then you're going to get an error. This is a very common error, and something that all developers should know how to understand,
         so let's save everything, and load the live preview.

###### __On the live page__
    - Once that's loaded, navigate to the Categories page, and then hover over any of the 'Edit'
         buttons for some of the categories we've created.
         If you notice in the bottom-left corner, you can see that the href for the 'Travel' card
         shows our new function of '/edit_category', and then the number '1'.(in the lower left corner of the page).
    - You can do this same thing, by using the Developer Tools and inspect the Edit button in the DOM.
         Jinja has converted the url_for() method into an actual href, and injected the respective
         ID into the argument we added of 'category_id'.
         It's the same for any of these cards, each with their own ID applied.
         However, try clicking on one of the Edit buttons, and you'll notice the Werkzeug Error.
         "Could not build url endpoint 'edit_category'. Did you forget to specify values ['category_id']?"
         The really fantastic thing with any Flask error, is that it will always tell you exactly
         which file and line number is causing the specific error.
         Normally, this can be found towards the bottom of the error lines, and you want to look for
         the code in the blue rows that matches your own code.
         As you can see here, we're calling the URL for the edit_category function, which is listed
         on the edit_category.html template, from line 7.
         Essentially what happened is once we added the primary key of ID into our app.route function,
         it will now always expect this for any link that calls this function.
         Let's go back to the edit_category template

###### __back to edit_category.html__
    - category template, and sure enough on line 7 we have the url_for method.
         All we need to do is provide the same exact argument of 'category_id' like we did on the href for the Edit button.
         Again, separate the argument with a comma after the single-quotes, and the variable
         name we assigned was 'category_id'.
         This will be set to 'category.id' as well for the value.
         Even though we added this to the URL now and saved the file, you will still get an error
         saying "'category' is undefined".
         You might be wondering where this 'category' value comes from, since this isn't part of
         a for-loop like on the categories template.
         That's the next step, so go ahead and return to your routes.py file.

###### __back to routes.py__
    - In order for this function to know which specific category to load, we need to attempt to find
         one in the database using the ID provided from the URL.
         The template is expecting a variable 'category', so let's create that new variable now.
         Using the imported Category model from the top of the file, we need to query the database,
         and this time we know a specific record we'd like to retrieve.
         There's a SQLAlchemy method called '.get_or_404()', which takes the argument of 'category_id'.
         What this does is query the database and attempts to find the specified record using the data
         provided, and if no match is found, it will trigger a 404 error page.
         Now, we can pass that variable into the rendered template, which is expecting it to be called
         'category', and that will be set to the defined 'category' variable above.
         The page should load now without any errors, however, if you notice, it doesn't show us
         the current value of our category, and the form doesn't do anything just yet.

###### __back to edit_category.html__
    - Within the edit_category template, now that we have the category retrieved from the database,
         we need to add its value into the input field.
         This is a variable, so we need to wrap it inside of double curly-brackets, and then
         we can target the 'category_name' from this variable of 'category' using dot-notation again.
         If you save those changes, and then reload the page and click on any of the Edit buttons
         now, it should pre-fill the form with the existing value from our database.

The final step now, is to add the "POST" functionality so the database actually gets updated with the requested changes.

###### __back to routes.py__
    - Back within our routes.py file, just after the 'category' variable being defined, let's
         conditionally check if the requested method is equal to "POST".
         If so, then we want to update the category_name for our category variable, and we'll set that
         to equal the form's name-attribute of 'category_name'.
         After that, we need to commit the session over to our database.
         Finally, if that's all successful, we should redirect the users back to the categories
         function, which will display all of them in the cards once again.
         Save all of your changes, and let's go back to the live preview.

###### __back to live preview__
For this demonstration, I'm going to quickly add a new test category, which we can manipulate and update all we want.
Once that's added to the database, go ahead and click the Edit button for that category.
So far so good, and the existing value is listed as 'Test'.
Let's update that to something different, such as 'Miscellaneous', and then click the button to submit the form.
Wonderful, no errors this time, and we're redirected back to the list of all categories,
which confirms that the original 'Test' card is now updated to be 'Miscellaneous'.

##### __end of stage 6__
By now, you should be fairly comfortable with Creating, Reading, and now Updating records.
We only have one more section from the CRUD functionality remaining, which is D for Deleting
items from the database, which is what we'll be doing in the next lesson.

## __Stage 7__






