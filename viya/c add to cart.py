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

if a=="chocolate cake":
    m+=1
else:
    pass
 
if b=="chocolate cake":
    m+=1
else:
    pass

if c=="kitkat cake":
    m+=1
else:
   pass

if d=="peanut butter cake":
    m+=1
else:
   pass

if e=="panda style cake":
    m+=1
else:
   pass
if f=="white forest cake":
    m+=1
else:
   pass
if g=="princess cake":
    m+=1
else:
   pass
if g=="Unicorn cake":
    m+=1
else:
   pass
if g=="Black forest cake":
    m+=1
else:
   pass

print("<center><h1 style='color:green;'>Result<br><br>mark obtained",m,"</h1>")
print('''
<head>
    <style>
       body{
background-image: url('mark.jpg');
backgorund-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}
</style>
<body>
<form method="POST" action="home.html">
<br><h1 style="color:red" >To goto Next chapter Click</h1>
<input type="submit" value="Next" style="font-size:30px;font-family:calibiri;background-color:green;color:white">
<br><br>
<a href="tamil1.html"style="color:red;font-size:18">Back to home</a>
</center>
</form>
</body>
''')




mark=m
import smtplib
import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password="admin13",database='learn')
cur=db.cursor()
cur.execute("SELECT p_email FROM students")
a=(cur.fetchall())
#for x in a:
#parent=x



db=mysql.connector.connect(host='localhost',user='root',password="admin13",database='learn')
std=db.cursor()
std.execute("SELECT s_name FROM students")
b=(std.fetchall())
#for y in b:
 # s_n=y



sender="vithyaksraj1311@gmail.com"
password="jqspbvczthikaflo"
receiver="vithyaq1311@gmail.com"

connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(sender,password)
msg="login and completed chapter 1 /n scored mark in the assesment"+str(mark)

connection.sendmail(sender,receiver,msg)
