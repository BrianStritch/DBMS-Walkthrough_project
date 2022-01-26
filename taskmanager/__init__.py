# We will start by importing the following: # noqa
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""
In order to actually use any of our hidden environment variables,
we need to import the 'env' package.

However, since we are not pushing the env.py file to GitHub, this
file will not be visible once deployed to Heroku, and will throw an error.

This is why we need to only import 'env' if the OS can find an existing
file path for the env.py file itself.
"""

if os.path.exists("env.py"):
    import env # noqa

"""
1. Now we can create an instance of the imported Flask() class, and that will be stored in
a variable called 'app', which takes the default Flask __name__ module.

2. Then, we need to specify two app configuration variables, 
and these will both come from our environment variables.
app.config SECRET_KEY and app.config SQLALCHEMY_DATABASE_URI, 
both wrapped in square brackets and quotes. Each of these will be set to get their 
respective environment variable, which is SECRET_KEY,
and the short and sweet DB_URL for the database location which we'll set up later.

3. Then, we need to create an instance of the imported SQLAlchemy() class, which will be
assigned to a variable of 'db', and set to the instance of our Flask 'app'.

4.Finally, from our taskmanager package, we will be importing a file called 'routes' 
which we'll create momentarily.

The reason this is being imported last, is because the 'routes' file, that we're about
to create, will rely on using both the 'app' and 'db' variables defined above.
If we try to import routes before 'app' and 'db' are defined, then we'll get circular-import
errors, meaning those variables aren't yet available to use, as they're defined after the routes.
These linting warnings are technically not accurate, so to stop the warnings, we can
add a comment at the end of each line, # noqa for 'No Quality Assurance'.
"""
# 1
app = Flask(__name__)
# 2
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
# 3
db = SQLAlchemy(app)
# 4
from taskmanager import routes # noqa
