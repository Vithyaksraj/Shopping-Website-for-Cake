#!C:\Users\91934\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type:text/html\n\r")
import cgi
form= cgi.FieldStorage()
m=0
a=form.getvalue('one')
b=form.getvalue('two')
c=form.getvalue('three')
d=form.getvalue("four")
e=form.getvalue('five')
f=form.getvalue('six')
g=form.getvalue('seven')
h=form.getvalue('eight')
print('cb',a)

