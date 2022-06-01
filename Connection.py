import mysql.connector

class Connection:
  db_host = 'localhost'
  db_user = 'root'
  db_password = ''
  db_name = 'vehicle_db'

  # open database connection
  mydb = mysql.connector.connect(host = db_host, user = db_user, password = db_password, database = db_name)

  # create cursor
  cursor = mydb.cursor()