{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.19041}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 import pandas as pd\par
import pyodbc\par
# Import CSV\par
import pymysql.cursors\par
data = pd.read_csv ('file\\customer.csv')\par
df = pd.DataFrame(data, columns= ['customerid', 'firstname','lastname','companyname','billingaddress1','billingaddress2','city','state','postalcode','country','phonenumber','emailaddress'])\par
# Connect to SQL\par
connection = pymysql.connect(host='localhost',\par
database='demo',\par
user='root',\par
password='root')\par
cursor = connection.cursor()\par
\par
# Create Table\par
cursor.execute('''CREATE TABLE people_info\par
( customerid nvarchar(20), firstname nvarchar(50), lastname nvarchar(50),\par
companyname nvarchar(50), billingaddress1 nvarchar(50),\par
billingaddress2 nvarchar(50) , city nvarchar(80),\par
state nvarchar(80) , postalcode nvarchar(80),\par
country nvarchar(80) , phonenumber nvarchar(50) ,\par
emailaddress nvarchar(50) )''')\par
\par
# Insert\par
for row in df.itertuples():\par
cursor.execute('''\par
INSERT INTO demo.people_info (\par
customerid, firstname,\par
lastname,companyname,billingaddress1,\par
billingaddress2,city,state,postalcode,\par
country,phonenumber,emailaddress)\par
VALUES ('\{\}','\{\}','\{\}','\{\}','\{\}','\{\}','\{\}','\{\}','\{\}','\{\}','\{\}','\{\}')\par
'''.format(row.customerid,row.firstname,row.lastname,row.companyname,row.billingaddress1,row.billingaddress2,row.city,row.state,row.postalcode,row.country,row.phonenumber,row.emailaddress)\par
)\par
connection.commit()\par
}
 