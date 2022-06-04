import mysql.connector
import os

# clear cmd
clear = lambda: os.system('cls')

class Connection:
  try:
    db_host = 'localhost'
    db_user = 'root'
    db_password = ''
    db_name = 'vehicle_db'

    # open database connection
    mydb = mysql.connector.connect(host = db_host, user = db_user, password = db_password, database = db_name)

    # create cursor
    cursor = mydb.cursor()
  
  except:
    clear()
    print(
      """
    + + + + + + + + + + + + + + + + + + +  + +
    +                                        +
    +               Error....!               +
    +                                        +
    +       DATABASE CONNECTION ERROR        +
    +                                        +
    +  01. Check if server is started.       +
    +                                        +
    +  02. Check MySQL is working or not.    +
    +      If not, fix it and try again      +
    +                                        +
    + + + + + + + + + + + + + + + + + + +  + + 
    """
      )

    exit()
    