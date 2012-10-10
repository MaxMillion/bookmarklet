var URL = window.location;
var selection = window.getSelection();
window.location.href = "http://localhost/cgi-bin/highlight.cgi?URL=" + URL + "&text=" + escape(selection);
