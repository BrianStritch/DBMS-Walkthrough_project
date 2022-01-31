"""
1. We can import render_template from flask to start with.

2. Then, from our main taskmanager package, let's import both 'app' and 'db'.

3. For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
    This will be used to target a function called 'home', which will just return the rendered_template
    of "base.html" that we will create shortly.

########### after writing models.py
4. we need to import these classes from models.py in order to generate our database next.

# back in stage 4 to set button function
5. If the requested method is equal to POST, then we will create a new variable called
    'category', which will be set to a new instance of the Category() model imported at the top of the file.

    Once we've grabbed the form data, we can then 'add' and 'commit' this information to the
    SQLAlchemy database variable of 'db' imported at the top of the file.
    This will use the database sessionmaker instance that we learned about in some of the previous videos.
    After the form gets submitted, and we're adding and committing the new data to our database,
    we could redirect the user back to the 'categories' page.
    We'll need to import the 'redirect' and 'url_for' classes at the top of the file from our flask import.

6. back in stage 5 - specific notes in readme

7. back in stage 6 - specific notes in readme

8. we are going to create a new function. For the app route URL, let's call this "/edit_category",
         and once again, we will be using this as a dual-purpose for both the "GET" and "POST" methods.
        The function name will match, so that will be "edit_category".
        To start with, we will only focus on the "GET" method, which will get the template, and render it on screen for us.
        We can simply return render_template using the new file we created, "edit_category.html".
9. In order for this function to know which specific category to load, we need to attempt to find
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
10. just after the 'category' variable being defined, let's
         conditionally check if the requested method is equal to "POST".
         If so, then we want to update the category_name for our category variable, and we'll set that
         to equal the form's name-attribute of 'category_name'.
         After that, we need to commit the session over to our database.
         Finally, if that's all successful, we should redirect the users back to the categories
         function, which will display all of them in the cards once again.
         Save all of your changes, and let's go back to the live preview.
"""
# 1
from flask import render_template, request, redirect, url_for
# 2
from taskmanager import app, db

# 4 
from taskmanager.models import Category, Task

# 3
@app.route("/")
def home():
    return render_template("tasks.html")

"""
Save the file, and now it's time to create the main Python file that will actually run the entire application.
"""

# back in stage 4 to set button function
@app.route("/categories")
def categories():
    # 6
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories = categories)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # 5
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

# 8
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id): 
    # 9
    category = Category.query.get_or_404(category_id)
    # 10
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category = category)
    
    

