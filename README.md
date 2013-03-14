This is an application that uses a combination of bookmarklets and cgi scripts to capture highlighted text on a webpage and save it for later querying.

## Requirements
* Apache Web Server, any version
* Chrome, Opera, or Firefox
* Sqlite3
* Python 2.7.x

## Installation
The first JavaScript bookmarklet saves highlighted text from a web page and sends it to a local sqlite3 database. The second bookmarklet accesses the cgi scripts of localhost that are designed to search and display any results saved to the database. To install both bookmarklets, create a new bookmark and do this:

```
javascript: <script>
```
Bootstrap-twitter is used as an interface for the local webserver's index.html that acts as a primitive search engine to the database. Text is searchable by Date and URL. Installation of cgi scripts and server backend depends on the web server and version, but in general every web server will have a central location for scripts and html to place these files in, respectively.
