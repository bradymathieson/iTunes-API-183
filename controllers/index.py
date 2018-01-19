from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/')
def index():
    data = {}

    data['terms'] = get_terms()

    return render_template('index.html', **data)

'''
You should add more files in the /controllers directory to "create pages" (each 
function preceded by '@app.route' represents a page) on your website.

	-	There should be one function per file, preceded by @app.route.
	-	Files and functions should be named in correspondence to where the page is directing
		to. For example, a page that lists all the schools from a particular term should be
		named schools.py, with the function named schools.
	-	Use this page as an example (copy-and-paste to start) of how to create more pages
		for your website. Make sure to include lines 1-3 of this file on each corresponding
		page.
	- 	Note some functions will need to have arguments (whereas index does not).
	-	Make sure to update the views.py file in the parent folder as you create more pages.
'''