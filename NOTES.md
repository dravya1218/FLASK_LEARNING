# 1. Understand how Flask serves pages
FLASK IS AN LIGTHWEIGHT OPEN SOURCE WEB APPLICATION FRAMEWORK WRITTEN IN PYTHON USED TO CONNECT PYTHON WITH WEB BROWSER AND SEND HTML PAGES 

When a user visits a URL:

Browser
   ↓
Flask Route
   ↓
Python Function
   ↓
Response
   ↓
Browser

Example:

@app.route("/")
def home():
    return "Hello"

User visits:

http://127.0.0.1:5000/

Flask:

finds matching route
runs home()
sends result back
Routes

## Route means URL path.

@app.route("/")
def home():
    return "Home Page"

Meaning:

/  →  home()

If user visits:

http://127.0.0.1:5000/

Flask runs home().

Another route:

@app.route("/about")
def about():
    return "About Page"

Meaning:

/about  →  about()

# 2. Render HTML pages

Instead of returning plain text:

return "Hello"

return an HTML file.

Project:

project/
│
├── app.py
└── templates/
    └── index.html

Flask:

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

HTML:

<h1>Welcome</h1>

Now browser displays a real webpage.

# 3. Navigate routes

Different URLs go to different functions.

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

Routes:

/         → Home → runs home()
/about    → About → runs about()
/contact  → Contact → runs contact()

Navigation links:

<a href="/">Home</a>

<a href="/about">About</a>

<a href="/contact">Contact</a>

User clicks link → Flask serves another page.

What is a Request?

A request is simply:

Browser → Flask

The browser asks Flask for something.

Examples:

Open page
Submit form
Delete expense
Edit expense

All of these are requests.

GET Request

GET means:

"Give me something"

Example:

User opens:

http://127.0.0.1:5000/

Browser sends:

GET /

Flask receives it.

@app.route("/")
def home():
    return render_template("index.html")

Flask sends:

index.html

back to browser.

Mental model:

GET = Show page/data

Examples:

Homepage
About page
Expense list
Profile page
POST Request

POST means:

"Here is some data"

Example:

User fills:

Food
200
Lunch

and clicks Submit.

Browser sends:

POST /

plus form data.

Flask receives:

expense_name = Food
amount = 200
category = Lunch

Mental model:

POST = Send data

Examples:

Add expense
Login
Signup
Contact form
request

Flask stores information about current request inside:

request

Think:

request = box containing request information

Inside that box:

request.method

tells:

GET or POST?

Example:

if request.method == "GET":

means:

Did user open page?

Example:

if request.method == "POST":

means:

Did user submit form?
request.form

When user submits form:

<input name="expense_name">

Flask receives:

request.form["expense_name"]

Think:

request.form = submitted form data

Almost like a dictionary.

User enters:

Food

Flask:

request.form["expense_name"]

returns:

Food
Full Flow

HTML:

<form method="POST">

    <input
        type="text"
        name="expense_name"
    >

    <button type="submit">
        Add
    </button>

</form>

Flask:

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        expense = request.form["expense_name"]

        return f"Expense: {expense}"

    return render_template("index.html")

What happens?

Step 1

User opens:

/

Browser sends:

GET /
Step 2

Flask checks:

request.method

Result:

GET
Step 3

Flask returns:

render_template("index.html")

User sees form.

Step 4

User types:

Food
Step 5

User clicks Submit.

Browser sends:

POST /

with:

expense_name = Food
Step 6

Flask checks:

request.method

Result:

POST
Step 7

Flask reads:

request.form["expense_name"]

Result:

Food
Step 8

Now you can:

save_expense(expense)

store in:

JSON
SQLite
MySQL
PostgreSQL
One Sentence Summary
GET = user wants page/ask flask for page

POST = user sends data

request.method = tells Flask GET or POST

request.form = gives Flask submitted form values

## REDIRECT IMPORT 
 
 redirect("url name")

USE TO REDIRECT USER TO URL 
IN RENDER_TEMPLATES IT OPENS THE HTML PAGE BUT IN REDIRECT IT REDIRECT USER TO THE URL THEN EXECUTE THE FUNCTION
IN REDIRECT WE DONT USE /ABOUT WE DO ABOUT

## HOW TO PRINT PYTHON VARIBLES IN HTMLL
IN .HTML FILE TO PRINT AN PYTHON VARIABLE WE USE {{}} INSIDE AN HTML TAG AND 
TO USE CONTROL STATEMENT
{% CONTROL STATEMENT %}
E.X
{% if %}
    {{----}}
{% elif %}
    {{----}}
{% else %}
    {{-----}}
{% endif %}
{% for e in expense %}

{% endfor %}

# 4.SOLite DATABASE
- SOLite database is an lightweight opensource database that store data in table in an onefie and doesnt need server to oprate it is builtin python so where eay to use
## SOLite connection
- To use SQLite, we first need to establish a connection to the database using sqlite3.connect().
- to use sqlite database we need to made connection with sql first
    
   import sqlite3
   conn=sqlite3.connection("filename.db")

## To access the table
- to access table or database we need to use cursor 

cursor=conn.cursor()

-cursor is an object that acts as an bridge between python and database used to execute sql commant and fetch data
## To create a table
-to create a table we first need to establish connection with sql then use cursor to perform any operation and to execute an instruction we use exectue command with cursor to perform SQLcommand

conn=sqlite3.connection()
cursor=conn.cursor()  #initalize cursor

cursor.execute('''CREATE TABLE IF NOT EXISTS expense(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,   # define columns   
                    name TEXT NOT NULL,                     
                    amount REAL NOT NULL,
                    category TEXT NOT NULL)''')

cursor.commit()
cursor.save()

-Primary Key  = "Who am I?"

Foreign Key  = "Who am I connected to?"

## SELECT
- SELECT is used to retrieve (read) data from a table.
### ALL COLUMS
cusor.execute('''SELECT * FROM expenses''')

- Meaning:
    Show all columns
    from expenses table

### SPECIFIC COLUMNS

cursor.execute('''Select specific columns
SELECT name, amount
FROM expenses''')

- Meaning:
    Show all columns of name and amount
    from expenses table

### Select one row

cursor.execute('''SELECT *
FROM expenses
WHERE id = 1''')

- Meaning:
    Show a specific row with all columns of it
    from expenses table

### RANGE OF DATA

cursor.execute('''SELECT *
FROM expenses
WHERE amount BETWEEN 100 AND 500''')

- Meaning:
    Show all columns between given range of data
    from expenses table

General structure
    SELECT columns
    FROM table
    WHERE condition

## INSERT DATA IN TABLE

cursor.execute('''INSERT INTO expenses
(name, amount, category)
VALUES ('Food', 200, 'Lunch')''')

- Meaning
    INSERT INTO expenses
            ↓
    Add a row to expenses table

    (name, amount, category)
            ↓
    Columns to fill

    VALUES(...)
            ↓
    Data to put in those columns

### INSERT DATA USEING PLACEHOLDERS

cursor.execute("""
INSERT INTO expenses
(name, amount, category)
VALUES (?, ?, ?)
""", ("Food", 200, "Lunch"))

- HOW IT WORKS
    1st ? → Food
    2nd ? → 200
    3rd ? → Lunch
- SQL converts placeholder intO this 
INSERT INTO expenses
(name, amount, category)
VALUES ('Food', 200, 'Lunch')

- Why use placeholders?

Suppose user enters:

Food
200
Lunch

You don't know these values beforehand.

So:

name = "Food"
amount = 200
category = "Lunch"

cursor.execute("""
INSERT INTO expenses
(name, amount, category)
VALUES (?, ?, ?)
""", (name, amount, category))

Now the query works for any user input.

## DELETE

cursor.execute("""
DELETE FROM expenses
WHERE id = ?
""", (2,))

- Meaning
    DELETE FROM expenses
           ↓
    Remove row from expenses table

    WHERE id = 2
           ↓
    Only row whose id is 2

--- Values for SQL placeholders are passed as a tuple(WHEN NUMBER IF VALUES ARE FIXED) OR LIST(WHEN U DONT KNOW HOW MANY VALUES ARE PASSED) where each tuple element replaces a corresponding ? placeholder. thats why we add extra , in this (2,)---

## UPDATE
- used to update dtae

###  UPDATE SPECIFIC COLUMN OF SPECIFIC ROW

cursor.execute('''UPDATE expenses
SET amount = 300
WHERE id = 1''')

- Meaning:
    UPDATE expenses
          ↓
    Modify data in expenses table

    SET amount = 300
          ↓
    Change amount to 300

    WHERE id = 1
          ↓
    Only for row whose id is 1

### UPADTE ALL COLUMNS OF A SPECIFIC ROW

cursor.execute("""
UPDATE expenses
SET name = ?, amount = ?, category = ?
WHERE id = ?
""", ("Snacks", 150, "Food", 1))

- Mapping:
    1st ? → Snacks
    2nd ? → 150
    3rd ? → Food
    4th ? → 1

WHY WHERE IS IMPORTSANT 
If we use where it target that specific row
if we dont use it will change all the column data

## CONN.COMMIT AND CONN.CLOSE
- coon.commit() use to save changes in database after exectuing an sql command
- conn.close()  use to close connection and release all resources of the database

# CONNS.ROW_FACORY
 
 conns.row_factory=sqlite3.ROW
 
- it converts database row into ROW objects
- allows user to access data by column names insted of index
- make code cleaner and easier to read

# URL_FOR
 
 url_for("view_expense")

- Automatically genrates url using route which function names it match
- Prevents hardcoded urls
- links continue working even if route paths change 

# DYNAMIC ROUTES PARAMETERS

@app.route("/update/<int:id>")

- <int:id> means flask accepts intger in url
- flask automatically store that value in variable id
/update/3
id=3

# PASSING VALUE THROUGH URLS

<a href="{{url_for('update_expense'),id= expense.id}}">

- Values can be passed through urls
- flask receives those values through route parameters
- Useful when working with specific records

# FLASK TEMPALTE VARIABLES

return rende_template(
    'index.html',mode='add'
)

- variables can be sent from python to html
- html can use those variables for conditions and displaying data

python->html
render_template()

html->python
using forms method="POST"
request.form

# Update System Logic

First, we are on view_expense.html.
All expenses are displayed in a table.
Every expense row has an Update anchor tag.
<a href="{{ url_for('update_expense', id=expense.id) }}">Update</a>
When the user clicks Update, Flask sends the user to a URL like:
/update/2
Here 2 is the ID of that particular expense.
Flask Update Route
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_expense(id):
Flask takes the ID from the URL.
That ID is passed into the function as id.
Then we use:
expense_data = get_expense_by_id(id)
This gets the old expense data from the database.
If Expense Exists

If the expense is found, Flask renders index.html again:

return render_template(
    "index.html",
    mode="update",
    expense=expense_data
)
mode="update" tells HTML this form is being used for updating.
expense=expense_data sends the old expense values to HTML.
In index.html

Because mode == "update":

Form action becomes the update route:
{{ url_for('update_expense', id=expense.id) }}
Input fields are pre-filled:
value="{{ expense.name }}"
value="{{ expense.amount }}"
Radio button is selected using checked.

So the user can see old values and change only what they want.

When User Submits
The form sends a POST request to:
/update/2
Flask gets the new form data.
Flask validates the data.
If valid, Flask runs the update database function:
update_expense_in_db(id, name, float(amount), category)
SQL updates only that row:
WHERE id = 2

Final result: only the selected expense is updated.

# WHAT I LERAN NEW 
## FLASK URL PARAMETER
### ROUTE PARAMETERS
@app,route("/update/<int:id>")
URL:
/update/5
- used when working with specific record (like that thing is needed to perform the operation)
- flask automatically store the value in a varaible (id)
- usually required 
- missing value eror will shown

### QUERY PARAMETER(REQUEST.ARGS)

/view_expense?mode=delete

mode=request.args.get("mode","view->(default value)")
- used for options,filters,modes,sorting and searching
- Usually use when optional values are given and too many options are there form which one-two need to be select
- missing value return none or default value

MEMORY RULE
WHICH ITEM -> ROUTE PARAMETER
WHICH OPETION/FILTER/MODE -> QUEREY PARAMETER

## DYNAMIC FILTERING
FILTER INPUTS
- name,category,min amount,max amount
function parameters
def filter_in_expense(name=None,category=None,min_amount=None,max_amount=None):

all input/filters are optional
you ca use one or many or none

SELECT * FORM expense WHERE 1=1
- 1=1 is always TRUE
- Not a loop
- makes it easy to add multiple AND condition when needed
E.X
WHERE 1=1
AND category = ?
AND amount >= ?

## DYNAMIC QUEREY BUILDING

query="SELECT * FROM expenses WHERE 1=1"

- Add condition only when user provies
E.X
if category:
    query+="AND category = ?"

- BENIFITS:
    ONE FUNCTION HANDELS ALL FILTERS COMBINATIONS
    NO NEED TO WRITE MANY SEPRATE SQL QURIES

## VALUES LIST
query="SELECT * FROM expenses WHERE 1=1"
values=[]
if category:
    query+="AND category = ?"
    values.append(category)->(this category is from use input SQL replace this ? with acutal values like category)

conn.execute(query,values)

## LIKE OPERATOR

if name:
    query+="AND name LIKE ?"
    values.append(f"%{name}%")
###  % WILDCARD
    values.append(f"%{name}%")

IF name=tea
query="AND name LIKE '%tea%'

MEANING
%TEA%-> SATRT WITH TEA
%TEA%-> END WITH TEA
%TEA%-> CONTAIN TEA ANYWHERE

## render_template()

Used when HTML needs data from Python.

Example:

render_template(
    "index.html",
    expense=expense,
    mode="update"
)
Purpose
Shows an HTML page.
Sends Python data directly to HTML.
Common Use Cases
Update Form
User Profile
Product Details
Expense Details
Dashboard
Flow
Python
   ↓
render_template()
   ↓
HTML receives data
Memory Rule
Need to show data?
        ↓
render_template()

## redirect()

Used when user should go to another route.

Example:

redirect(url_for("expense"))
Purpose
Move user to another page.
Does not send Python objects to HTML.
Common Use Cases
After Add
After Delete
After Update Save
After Login
Flow
Python
   ↓
redirect()
   ↓
Another Route
   ↓
HTML
Memory Rule
Need to move user?
        ↓
redirect()

## Update Route
Flow
User clicks Update
        ↓
Get expense from database
        ↓
Need old data in form
        ↓
render_template()
Why?

The form needs:

Name
Amount
Category

to be pre-filled.

Example:

expense = {
    "name": "Food",
    "amount": 100
}
Delete Route
Flow
User clicks Delete
        ↓
Delete expense
        ↓
Action finished
        ↓
redirect()
Why?

No expense data needs to be shown.

Only need:

Go back to expense list

## url_for()

Used to generate URLs.

Example:

url_for("expense")

Result:

/view_expense
Passing Small Values

Example:

url_for(
    "expense",
    mode="delete"
)

Result:

/view_expense?mode=delete
Route Parameters

Example:

url_for(
    "update_expense",
    id=5
)

Result:

/update/5
What Should Be Passed to url_for()?

Good:

id=5
mode="delete"
page=2
category="Food"

These are small values.

What Should NOT Be Passed?

Bad:

expense=expense
expenses=expenses
user=user

Example:

expense = {
    "name": "Food",
    "amount": 100
}

Do NOT do:

url_for(
    "expense",
    expense=expense
)
Why?

url_for() creates URLs.

It is not designed to send Python objects.

Sending Objects to HTML

Use:

render_template(
    "index.html",
    expense=expense
)

Now HTML can use:

{{ expense.name }}
{{ expense.amount }}
url_for() vs render_template()
url_for()
Generate URL

Examples:

id
mode
page
filter
render_template()
Send data to HTML

Examples:

expense
expenses
user
products
Final Memory Rule
Need to show data?
        ↓
render_template()

Need to move user?
        ↓
redirect()

Need to generate a URL?
        ↓
url_for()
Small values
(id, mode, page)
        ↓
url_for()

Objects and data
(expense, expenses, user)
        ↓
render_template()

# SUM()
- purpos
 Add values from a cloumn
 gives total sum of values in a column
e.x
Name	Amount
Pizza	100
Burger	150
Bus	50
Train	200

cursor.execute("SELECT SUM(AMOUNT) AS total FROM expenses)
Calculation
100 + 150 + 50 + 200
result
500

Memory Rule
SUM()
↓
Add values of particular column

# COUNT()
- Purpose
    count rows of the table
e.x
    Name
Pizza
Burger
Bus
Train

cursor.execute("SELECT COUNT(*) AS count FROM EXPENSES)

- Calculation
    1 2 3 4
- Result
    4

Memory Rule
COUNT()
↓
Count rows

## COUNT()+WHERE()/GROUP BY()
Name	Amount  CATEGORY
Pizza	100     food
Burger	150     food
Bus	    50      travel
Train	200     travel

cursor.execute("SELECT COUNT(category) FROM expenses WHERE category = food")

result
    2
useing where we get specific data 

WHERE
↓
Count one specific thing

cursor.execute("SELECT COUNT(category) AS count FROM expenses WHERE GROUP BY category")

result
    food -> 2
    travel -> 2

GROUP BY
↓
Count every group separately

# GROUP BY
-Purspose
 split rows into groups

e.x
Name	Amount  CATEGORY
Pizza	100     food
Burger	150     food
Bus	    50      travel
Train	200     travel

cursor.execute("SELECT COUNT(category) AS count FROM expenses WHERE GROUP BY category")

result
    food -> 2
    travel -> 2

GROUP BY
↓
Count every group separately

# Delete Confirmation Without JavaScript
Problem
Click Delete
↓
Expense deleted immediately

Risk:

Accidental deletion
Wrong click
No confirmation
Solution
Delete Mode
↓
Click Delete
↓
Delete Confirmation Page
↓
Delete / Cancel
↓
Delete Expense
Important Rule
GET
↓
Show confirmation page

POST
↓
Delete data

# Reusing Existing Template

Instead of creating:

confirm_delete.html

we reused:

index.html

using:

mode = delete_confirm
Benefit
Less files
Less code duplication
Reusable UI

# Readonly vs Disabled
Readonly
readonly

User cannot edit.

Value is still submitted.

Disabled
disabled

User cannot edit.

Value is NOT submitted.

Important
Disabled fields are not sent in form data.

This caused:

KeyError: Category

# Form Action Can Change Dynamically

Example:

{% if mode=='update' %}
    update route

{% elif mode=='delete_confirm' %}
    delete route

{% else %}
    home route
{% endif %}
Concept
Same form
↓
Different action
↓
Based on mode

# Debugging Template Logic

Problem:

Delete route not working

Reason:

Wrong mode name

Example:

delete_confirm

vs

delete_onfirm
Lesson
One typo in Jinja condition
↓
Entire branch fails

# Active Navbar Concept

Navbar link:

url_for(..., mode="delete")

Creates:

/view_expense?mode=delete

Flask:

mode = request.args.get("mode")

Template:

{% if mode=='delete' %}
    class="active"
{% endif %}
Flow
User Click
↓
URL contains mode
↓
Flask reads mode
↓
Template receives mode
↓
Active class added

# Dynamic CSS Classes

Example:

class="{% if mode=='delete' %}active{% endif %}"
Generated HTML

If mode is delete:

class="active"

Otherwise:

class=""
Lesson
Class is generated during template rendering.

# Cleaner URLs
Current:

/update/1?mode=update

Better:

/update/1

Current:

/delete_confirm/1?mode=delete_confirm

Better:

/delete_confirm/1
Lesson

Routes already indicate the mode.

/update
↓
Update mode

/delete_confirm
↓
Delete confirmation mode

No need for extra query parameters.


