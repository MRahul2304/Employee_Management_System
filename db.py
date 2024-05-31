import mysql.connector
from mysql.connector import errorcode

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connect_to_server()
        self.create_table()

    def connect_to_server(self):
        try:
            # First, connect to the MySQL server without specifying a database
            self.con = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            self.cur = self.con.cursor()
            
            # Create the database if it does not exist
            self.cur.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            self.con.commit()

            # Now connect to the specified database
            self.con.database = self.database
            self.cur = self.con.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print(f"Database {self.database} does not exist")
            else:
                print(err)

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS EMPLOYEE (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            Age VARCHAR(255),
            DOJ VARCHAR(255),
            Email VARCHAR(255),
            Gender VARCHAR(255),
            Contact VARCHAR(255),
            Address VARCHAR(255)
        )"""
        self.cur.execute(sql)
        self.con.commit()

    #Insert Data in DB
    def insert(self, name, age, doj, email, gender, contact, address):
        try:
            # Reconnect to the database
            if not self.con.is_connected():
                self.connect_to_server()

            self.cur = self.con.cursor()
            
            # Insert data into the EMPLOYEE table
            sql = "INSERT INTO EMPLOYEE (Name, Age, DOJ, Email, Gender, Contact, Address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (name, age, doj, email, gender, contact, address)
            self.cur.execute(sql, values)
            self.con.commit()
            
        except mysql.connector.Error as err:
            print(err)
        finally:
            self.cur.close()
            self.con.close()

    #Fetch All Data from DB
    def fetch(self):
        try:
            # Reconnect to the database
            if not self.con.is_connected():
                self.connect_to_server()

            self.cur = self.con.cursor()

            self.cur.execute("select * from employee")
            row =self.cur.fetchall()
            return row
        
        except mysql.connector.Error as err:
            print(err)
        finally:
            self.cur.close()
            self.con.close()

    #Delete Data
    def delete(self, id):
        try:
            # Reconnect to the database
            if not self.con.is_connected():
                self.connect_to_server()

            self.cur = self.con.cursor()

            sql = "DELETE FROM EMPLOYEE WHERE id = %s"
            self.cur.execute(sql, (id,))
            self.con.commit()
            
        except mysql.connector.Error as err:
            print(err)
        finally:
            self.cur.close()
            self.con.close()

    #Delete All Data
    def delete_all(self):
        try:
            if not self.con.is_connected():
                self.connect_to_server()

            self.cur = self.con.cursor()
            self.cur.execute("TRUNCATE TABLE employee")
            self.con.commit()
        except mysql.connector.Error as err:
            print(err)
        finally:
            self.cur.close()
            self.con.close()


    #Update recode in DB
    def update(self, id, name, age, doj, email, gender, contact, address):
        try:
            # Reconnect to the database
            if not self.con.is_connected():
                self.connect_to_server()

            self.cur = self.con.cursor()
            
            # Insert data into the EMPLOYEE table
            sql = "UpDATE EMPLOYEE  SET Name = %s, Age = %s, DOJ = %s, Email = %s, Gender = %s, Contact = %s, Address = %s where id =%s"
            values = (name, age, doj, email, gender, contact, address , id)
            self.cur.execute(sql, values)
            self.con.commit()
             
        except mysql.connector.Error as err:
            print(err)
        finally:
            self.cur.close()
            self.con.close()



