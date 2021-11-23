# imports
import mysql.connector
from mysql.connector import Error, errorcode

class SqlManager:
    # attributes
    config = {}
    sqlConnection = None

    # constructor
    def __init__(self, config):
        self.config = config

    # methods
    def connect(self):
        try:
            self.sqlConnection = mysql.connector.connect(**self.config)
            print("Sql: connection successed")
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Sql Error: username or password invalid")
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Sql error: database does not exist")
            else:
                print("Sql error: " + error)
        else:
            self.sqlConnection.close()
    
    def createLaptop(self):
        # rfid_tag,first_name,name,student,club_adherant,mail
        try:
            mySql_Create_Table_Query =  """CREATE TABLE Laptop ( 
                                        RFID_tag varchar(250) NOT NULL,
                                        Prenom varchar(250) NOT NULL,
                                        Nom varchar(250) NOT NULL,
                                        Status_student boolean NOT NULL,
                                        Club_adherant boolean NOT NULL,
                                        Mail varchar(250) NOT NULL,
                                        PRIMARY KEY (Id)) """
            cursor = self.sqlConnection.cursor()
            result = cursor.execute(mySql_Create_Table_Query)
            print("Sql: Laptop Table created with success")
        except mysql.connector.Error as error:
            print("Sql error: failed to create table in MySQL: {}".format(error))
    
    def close(self):
        self.sqlConnection.close()
        