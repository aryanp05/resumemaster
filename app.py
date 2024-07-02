from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from CR_format_data import format_resume
from cs50 import SQL
from functools import wraps

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///resume.db")

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

@app.route('/', methods=['POST', 'GET'])
def index():
    
        #print(f"{person_name}\n {contactInfoList}\n {educationInfo}\n, {experienceInfo}\n, {projectInfo}\n, {skillsInfo}\n")
        #print(contactInfoList)
        #print(person_name, contactInfoList, educationInfo, experienceCounter, projectCounter, skillsCounter)
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash(f"Please type in a username")
            return render_template("login.html")
            #return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash(f"Please type in a password")
            return render_template("login.html")
            #return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            flash(f"invalid username and/or password")
            return render_template("login.html")
            #return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == 'GET':
        return render_template("register.html")
    
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash(f"must provide username")
            return render_template("register.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash(f"must provide password")
            return render_template("register.html")

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            flash(f"must provide confirmation")
            return render_template("register.html")

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            flash(f"passwords do not match")
            return render_template("register.html")
        
         # Check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 0:
            flash(f"username already exists")
            return render_template("register.html")
        
        # Insert new user into the database
        db.execute("INSERT INTO users (username, password) VALUES(?, ?)",
                   request.form.get("username"), generate_password_hash(request.form.get("password")))
    
        # Retrieve the newly created user's ID
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Store the user ID in the session
        session["user_id"] = rows[0]["id"]

        # Redirect to the homepage
        return redirect("/")

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        person_name = request.form['person_name']
        contactInfoList = request.form.getlist('contact_info')

        educationInfo = []
        experienceInfo = []
        projectInfo = []
        skillsInfo = []

        for key in request.form:
            if key.startswith('education'):
                tempEd = request.form.getlist(key)
                educationInfo.append(tempEd)
            elif key.startswith('experience'):
                tempEx = request.form.getlist(key)
                experienceInfo.append(tempEx)
            elif key.startswith('project'):
                tempPr = request.form.getlist(key)
                projectInfo.append(tempPr)
            elif key.startswith('skills'):
                tempSk = request.form.getlist(key)
                skillsInfo.append(tempSk)
        print(educationInfo)
        format_resume(person_name, contactInfoList, educationInfo, experienceInfo, projectInfo, skillsInfo)

        return render_template("create.html", person_name=person_name, contactInfoList=contactInfoList, educationInfo=educationInfo)
    else:
        # Redirect user to login form
        return render_template("create.html", person_name="", contactInfoList=[""], educationInfo=[["","","","",""]])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=800)

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=8000)
#     #app.run(debug=True)
    

#  test test test test test test test