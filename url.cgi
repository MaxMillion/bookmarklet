#!/usr/bin/env python
#

import cgi, cgitb
cgitb.enable()
import sqlite3
import time
from time import *

print 'Content-Type: text/html\n'

form = cgi.FieldStorage()
date = form.getvalue('mydate')
url = form.getvalue('myurl')

#bootstrap-twitter formatting header stuff, includes navbar
print '''
<head>
<script src="http://code.jquery.com/jquery-latest.js"></script>
<script src="/js/bootstrap.min.js"></script>
<link href="/css/bootstrap.min.css" rel="stylesheet">


  <div class="navbar navbar-inverse">
    <div class="navbar-inner">
    <a class="brand" href="/">MyText Search</a>
    <ul class="nav">
    </ul>
    </div>
    </div>
</head>
'''

#two search boxes
print '''
  <div class="container">    
    <form action="date.cgi">
    <legend>Search by Date</legend>
    <input type="text" class="input-xlarge" name="mydate">
    <button type="submit" class="btn btn-primary">Submit</button>
    </form>  
    
    <form action="url.cgi">
    <legend>Search by URL</legend>
    <input type="text" class="input-xlarge" name="myurl">
    <button type="submit" class="btn btn-primary">Submit</button>
    </form> 
   </div>
'''

print '''<h2>Info dump:</h2>'''

# connect to db
# sqlite spits out tuples, lists are nice to work with so we mapped them to lists
# list of lists, each list is an entry in the db
username = "testuser1"
conn = sqlite3.connect("" + username + ".db")
c = conn.cursor()
highlist = []
for row in c.execute("SELECT * FROM highlights"):
    highlist.append(row)
c.close()
highlist = map(list, highlist)

#sorts based off of url
#should probably strip off any whitespace on the ends of the user entries
#should use regex so that the user won't have to make strict matches
#could probably make a cool search engine algorithm
for i in range(0, len(highlist) - 1):
    print '''<br>'''
    #The url is always in the "1" slot in each entry since we recorded it into the db that way
    if highlist[i][1] == url:
        #iterates through each entry and prints it out
        for j in range(0, 3):
            print highlist[i][j]
