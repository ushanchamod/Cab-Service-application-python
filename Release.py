from Connection import Connection
import mysql.connector
import os

# clear cmd
clear = lambda: os.system('cls')

# create connection
conn = Connection()


class Release:
  def releaseVehical(self):
    print(
    """
     ~~~~~~~~~~~~~~~~~~
    | Release form job |
     ~~~~~~~~~~~~~~~~~~
    """
    )

    try:
      sql = "SELECT * FROM `vehicle` WHERE `in_job` = %s"
      val = (1,)
      conn.cursor.execute(sql, val)
      data = conn.cursor.fetchall()
      conn.mydb.commit()

      print("\nThis is job assign vehicles :-")
      print()

      for vehicle in data:
        print("  Vehicle Number       : ",vehicle[0])
        print("  Vehicle name         : ",vehicle[1])
        print("  Number of Passengers : ",vehicle[2])
        print("  AC Availability      : ",vehicle[3])
        print("  Size                 : ",vehicle[4])
        print("------------------------------------")
        print()
      
      select = input("Which Vehicle You Want Release (Enter Vehicle ID) : ")
      try:
        sql = "UPDATE `vehicle` SET `in_job`= 0 WHERE `id` = %s"
        val = (select,)
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()

        if len(select) != 0: 
          print("Vehicle Successfully Release From Job..!")

        AsignAgain = input("Are you release more vehicle from job ? (y/ n) : ")
        print()
        if AsignAgain.lower() == "y":
          clear()
          self.asignVehical()

        else:
          pass

      except:
        print("SQL Query Error...!")
    except:
      clear()
      print("Query Error..!")
      self.releaseVehical()