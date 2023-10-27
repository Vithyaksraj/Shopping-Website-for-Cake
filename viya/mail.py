#!C:\Users\91934\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type:text/html\n\r")


print('''
<head>
    <style>
       body{
background-image: url('mail.jpg');
backgorund-repeat: no-repeat;
background-attachment: scroll;
background-size: 100% 100%;
}
mark{
background-color:blue;
color:white;
}
</style><center>
<u><h1 style="font-size:50px;font-family:georgia;">CONFIRMATION</h1></u>
<br><br>''')

import cgi
form= cgi.FieldStorage()


name=form.getvalue('nm')
b=form.getvalue('ad')
c=form.getvalue('pn')
email=form.getvalue("em")
e=form.getvalue('pay')



print("<center><h1>Dear Customer<b>",name,"</b>&nbsp&nbsp&nbsp<br>Order Taken</h1>",b,"<br> <h2>Thank You ,Kindly Check Your Email",email,"<br><br><br>")
pay=0
if e=='1':
    pay='Gpay'
    print("Payment done through",pay,'<br>')

elif e=='2':
   pay='Phonepe'
   print("Payment done through",pay,'<br>')

elif e=='3':
   pay='paytm'
   print("Payment done through",pay,'<br>')
elif e=='4':
   pay=UPI
   print("Payment done through",pay,'<br>')

else:
   pay='COD'
   print("<h1>Payment done through",pay,'<br>')

print('''
<body>
<center>

<a href="index.html"><button type='submit'  style="background-color:green;color:white;text-align:right;font-size:30;"> EXIT</button></a>
</form>
</body>
''')
import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password="admin13",database='f')
cur=db.cursor()
query="INSERT INTO order_d(name ,address ,email ,p_num,payment) VALUES(%s,%s,%s,%s,%s)"
cur.execute(query,(name,b,email,c,e))
db.commit()

import smtplib

sender="vithyaksraj1311@gmail.com"
password="jqspbvczthikaflo"
receiver="vithyaksraj1311@gmail.com"

connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(sender,password)
msg='Dear Customer your Order has been confirmed and  Delivered to your location within 30 minutes.'+str(cur)
connection.sendmail(sender,receiver,msg)


