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