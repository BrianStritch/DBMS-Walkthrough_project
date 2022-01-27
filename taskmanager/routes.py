"""
1. We can import render_template from flask to start with.

2. Then, from our main taskmanager package, let's import both 'app' and 'db'.

3. For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
    This will be used to target a function called 'home', which will just return the rendered_template
    of "base.html" that we will create shortly.
"""
# 1
from flask import render_template
# 2
from taskmanager import app, db
# 3
@app.route("/")
def home():
    return render_template("base.html")

"""
Save the file, and now it's time to create the main Python file that will actually run the entire application.
"""
