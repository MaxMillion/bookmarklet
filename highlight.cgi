#!/usr/bin/env python
#

import cgi, cgitb
import sqlite3
from time import strftime

print "Content-Type: text/html"
print

#grabs url,text passed in from js bookmarklet
#baked in user, cookie-issues
#could have probably used a hashcode and a database for user logins/passes
#function could also query db anytime it needed to check if a user existed or has used app before
#replaces need for cookies
#could keep track of stats

form = cgi.FieldStorage()
date = strftime("%Y-%m-%d %H:%M:%S")
url = form.getvalue('URL')
text = form.getvalue('text')
username = "testuser1"

#sqlite db used, inserts date url text
conn = sqlite3.connect("" + username + ".db")
c = conn.cursor()
c.execute("CREATE TABLE if not exists highlights (date, url, text)")
c.execute("INSERT INTO highlights VALUES (?, ?, ?)", (date, url, text))
conn.commit()
c.close()
