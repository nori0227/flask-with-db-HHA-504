#importing packages
import sqlite3 # note, sqlite3 comes with python3

# Connecting to sqlite
# connection object
connect = sqlite3.connect('./patients.db')
 
# db object
db = connect.cursor() 
db.execute("DROP TABLE IF EXISTS patient_table")

connect.commit()

# // commit () --> This method commits the current transaction. If we don't call this method, 
# anything we did since the last call to commit() is not visible from other database connections.

# Creating table, 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            gender CHAR(25) NOT NULL,
            ethnicity CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() # commit the changes


## note, you may see a .db-journal file, that is a temporary file that is created when you create a database.
## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, ethnicity) values('12345', 'John', 'Smith', '01/01/2000', 'F', 'White')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, ethnicity) values('23456', 'Jane', 'Doe', '02/02/2001', 'F', 'Indian American')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, ethnicity) values('34567', 'Mary', 'Smith', '03/03/2002', 'F', 'African American')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, ethnicity) values('45678', 'Bob', 'Smith', '04/04/2003', 'M', 'Indian American')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, ethnicity) values('56789', 'Jane', 'Doe', '05/05/2004', 'F', 'Indian American')")


connect.commit()



