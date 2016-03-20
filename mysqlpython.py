import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","sharang","users" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

name = raw_input("enter name")
email=raw_input("enter email address")
username=raw_input("enter username")
password=raw_input("enter password")


#create = "CREATE TABLE details (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20),email VARCHAR(30),username VARCHAR(30), password VARCHAR(30))"

#cursor.execute(create)

insert= "INSERT INTO details(name,email,username,password) VALUES('"+name+"',"+"'"+email+"',"+"'"+username+"',"+"'"+password+"')"

try:
   # Execute the SQL command
   cursor.execute(insert)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

data = "select * from details"
cursor.execute(data)

# disconnect from server
db.close()
