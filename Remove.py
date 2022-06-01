from Connection import Connection
import mysql.connector
import os

# clear cmd
clear = lambda: os.system('cls')

# create connection
conn = Connection()

class Remove:
  
  # create connection

  def removeVehical(self):
    print(
    """
     ~~~~~~~~~~~~~~~~
    | Remove Vehicle |
     ~~~~~~~~~~~~~~~~
    """
    )

    selectNumber = input("Enter Vehicle Number : ")
    print()

    try:
      sql = "SELECT `id`, `type`, `number_of_passengers`, `ac`, `size`, `in_job` FROM `vehicle` WHERE `id` = %s"
      val = (selectNumber,)
      conn.cursor.execute(sql, val)
      data = conn.cursor.fetchall()
      conn.mydb.commit()

      if len(data) == 0:
        clear()
        print("You Serch vehicle not in the data base. check vehicle number...!")
        print()
        self.removeVehical()
      else:
        print("Vehicle Number       : ",data[0][0])
        print("Vehicle name         : ",data[0][1])
        print("Number of Passangers : ",data[0][2])
        print("AC Avalibility       : ",data[0][3])
        print("Size                 : ",data[0][4])
        print("Asign Job            : ",data[0][5])
        
        if data[0][5] == 0:
          confirmRemove = str(input("\nAre you Sure REMOVE Vehicle From System? (y / n) : "))
          print()
          if confirmRemove.lower() == "y":
            try:
              sql = "DELETE FROM `vehicle` WHERE `id` = %s"
              val = (selectNumber,)
              conn.cursor.execute(sql, val)
              conn.mydb.commit()

              print("Remove vehicle successfully...!")
              print()

              delAgain = input("Are you delete more vehicle from system? (y/ n) : ")
              print()
              if delAgain.lower() == "y":
                clear()
                self.removeVehical()
              else:
                pass

            except:
              clear()
              print("`DELETE sql query is wrong...!` ")
              print()
              self.removeVehical()
          else:
            clear()
            pass

        elif data[0][5] == 1:
          clear()
          print("Can't delete....! ")
          print("Vehicle in hire...! ")
          self.removeVehical()

    except:
      print("Data Query Error....! ")
      print()
    