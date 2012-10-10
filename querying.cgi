#!/usr/bin/env python
#

import cgi, cgitb 
import sqlite3

print "Content-Type: text/html"
print


#bootstrap-twitter formatting header stuff, includes navbar
print '''
<head>
<script src="http://code.jquery.com/jquery-latest.js"></script>
<script src="/js/bootstrap.min.js"></script>
<link href="/css/bootstrap.min.css" rel="stylesheet">


  <div class="navbar navbar-inverse">
    <div class="navbar-inner">
    <a class="brand" href="#">MyText Search</a>
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

#dumps everything in the db, formatted nicer thanks to the lists
for entry in highlist:
    for item in entry:
        print item
        print '''<br>'''
        
    print '''<br>'''
