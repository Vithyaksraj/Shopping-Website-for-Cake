#!C:\Users\91934\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type:text/html\n\r")
import cgi
form=cgi.FieldStorage()
n=form.getvalue('n')
ps=form.getvalue('e')
em=form.getvalue('p')
c=form.getvalue('pwd')

import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='admin13',database='data')
cur=db.cursor()
query="INSERT INTO d(s_name,email,phone,email_password)VALUES(%s,%s,%s,%s)"
val=(n,ps,em,c)
cur.execute(query,val)
db.commit()
db.close()






print('''
<html>
<head>
<center>
<h1>LOGIN</h2>

<body>
<form method="POST" action="index.html">
<body background="log.jpg" style="background=repeat:no-repeat;background-size:100% "></body>
<body>
<table>
<tr>
<td><h2 style="color:brown">USER NAME:</h2></td>
<td><h2><input type="text align:center"; placeholder="user name"></h2></td>
</tr>
<tr>
<td><h2 style="color:brown">PASSWORD:</h2></td>
<td><h2><input type="text" placeholder="password"></h2></td>
</tr>
<tr>
<center>
<td><style="color:green"><input type="submit" value="Login"></td>
</center>
</tr>
</table>
</center>
</body>
</head>
</html>
'''
)

