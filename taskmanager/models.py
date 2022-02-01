"""
1. Since we will be defining the database, we obviously need to import db from the main taskmanager package.
    For the purposes of these videos, we will be creating two separate tables, which will
    be represented by class-based models using SQLAlchemy's ORM.

2. The first table will be for various categories, so let's call this class 'Category', which
    will use the declarative base from SQLAlchemy's model.

3. The second table will be for each task created, so we'll call this class 'Task', also using the default db.Model.

4. We want each of these tables to have a unique ID, acting as our primary key, so let's create
    a new column variable of 'id' for both of these tables.
    These will be columns on our tables, and each will be Integers, with primary_key set to
    True, which will auto-increment each new record added to the database.

note:   If you recall from the last few lessons, we had to specifically import each column type at the top of the file.
        However, with Flask-SQLAlchemy, the 'db' variable contains each of those already, and we can
        simply use dot-notation to specify the data-type for our columns.

5. For each model, we also need to create a function called __repr__ that takes itself as the argument,
    similar to the 'this' keyword in JavaScript. This is a standard Python function meaning 'represent’,
    which means to represent the class objects as a string.

    Another function that you might see out there, is the __str__ function that behaves quite
    similar, and either should be suitable to use.

    For now, let's just return self for those, but we'll come back to these momentarily.

6. Within our Category table, let's add a new column of 'category_name', which will be set to a standard db.Column().
    This will be the type of 'string', with a maximum character count of 25, but you can
    make these larger or smaller if needed.
    We also want to make sure each new Category being added to the database is unique, so we'll set that to True.
    Then, we also need to make sure it's not empty or blank, so by setting nullable=False this
    enforces that it's a required field.

    Now that we have a category_name, we can simply return self.category_name in our function.

7. For our Task table, we'll add a new column of 'task_name', which will also be a standard db.Column().
    This will also be the type of 'string', with a maximum character count of 50, which should
    also be unique for each record, and required, so nullable=False.
    Then, we'll create a new column for 'task_description', and this time we'll use db.Text instead of
    string, which allows longer strings to be used, similar to textareas versus inputs.
    Next, we'll create a new column for 'is_urgent', but this will be a Boolean field, with a default
    set to False, and nullable=False.

    Then, the next column will be 'due_date', and this data-type will be db.Date with nullable=False,
    but if you need to include time on your database, then db.DateTime or db.Time are suitable.

    The final column we need for our tasks is a foreign key pointing to the specific category, which will be our category_id.
        This will use db.Integer of course, and for the data-type we need to use db.ForeignKey
        so our database recognizes the relationship between our tables, which will also be nullable=False.
        The value of this foreign key will point to the ID from our Category class, and therefore
        we need to use lowercase 'category.id' in quotes.
        In addition to this, we are going to apply something called ondelete="CASCADE" for this foreign key.


note: By the way, you can see a full list of column and data types from the SQLAlchemy docs, which
        include Integer, Float, Text, String, Date, Boolean, etc.

        Since each of our tasks need a category selected, this is what's known as a one-to-many relationship.
        One category can be applied to many different tasks, but one task cannot have many categories.
        If we were to apply many categories to a single task, this would be known as a many-to-many relationship.

8. In order to properly link our foreign key and cascade deletion, we need to add one more field to the Category table.
        We'll call this variable 'tasks' plural, not to be confused with the main Task class, and
        for this one, we need to use db.relationship instead of db.Column.
        Since we aren't using db.Column, this will not be visible on the database itself like
        the other columns, as it's just to reference the one-to-many relationship.
        To link them, we need to specify which table is being targeted, which is "Task" in quotes.
        Then, we need to use something called 'backref' which establishes a bidirectional relationship
        in this one-to-many connection, meaning it sort of reverses and becomes many-to-one.
        It needs to back-reference itself, but in quotes and lowercase, so backref="category".
        Also, it needs to have the 'cascade' parameter set to 'all, delete' which means it will find
        all related tasks and delete them.
        The last parameter here is lazy=True, which means that when we query the database for
        categories, it can simultaneously identify any task linked to the categories.
        The final thing that we need to do with our class-based models, is to return some sort of string for the Task class.
        We could simply return self.task_name, but instead, let's utilize some of Python's formatting to include different columns.
        We'll use placeholders of {0}, {1}, and {2}, and then the Python .format() method to specify
        that these equate to self.id, self.task_name, and self.is_urgent.

9.  return back to our routes.py file now.

10. return back in stage 4 : 
"""

# 1
from taskmanager import db


# 2
class Category(db.Model):
    # 4 schema for the category model
    id = db.Column(db.Integer, primary_key=True)
    # 6 
    category_name = db.Column(
        db.String(25),unique = True, nullable = False
        ) # the 25 sets the max length of the charachters the string is allowed have
    # 8
    tasks = db.relationship("Task", backref = "category", cascade="all, delete", lazy=True)
    
    # 5
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


# 3
class Task(db.Model):
    # 4 schema for the category model    
    id = db.Column(db.Integer, primary_key=True)
    # 7
    task_name = db.Column(db.String(50), unique = True, nullable = False)
    task_description = db.Column(db.Text, nullable = False)
    is_urgent = db.Column(db.Boolean, default = False, nullable = False)
    due_date = db.Column(db.Date, nullable = False)
    categoty_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete = "CASCADE"), nullable = False)
    # 5
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent 
        )

    # 9  ---- return back to our routes.py file now.

# 3
class Tasks(db.Model): # this is a copy of the above as mispelling in category_id
    # 4 schema for the category model    
    id = db.Column(db.Integer, primary_key=True)
    # 7
    task_name = db.Column(db.String(50), unique = True, nullable = False)
    task_description = db.Column(db.Text, nullable = False)
    is_urgent = db.Column(db.Boolean, default = False, nullable = False)
    due_date = db.Column(db.Date, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete = "CASCADE"), nullable = False)
    # 5
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent 
        )

    # 9  ---- return back to our routes.py file now.
