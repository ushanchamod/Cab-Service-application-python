from Connection import Connection
import mysql.connector
import os

# clear cmd
clear = lambda: os.system('cls')

# create connection
conn = Connection()

class Asign:
  def asignVehical(self):
    print(
    """
     ~~~~~~~~~~~~~~
    | Assign a job |
     ~~~~~~~~~~~~~~
    """
    )

    print(
    """
    Car -------------> (c)

    Van -------------> (v)

    3 Wheelers ------> (w)

    Trucks ----------> (t)

    Lorry -----------> (l)

    Exit ------------> (x)

    """)
    whichOne = str(input("What vehicle are you looking for? : "))

    def checkVehicalAvalibale():
      return True

    if whichOne.lower() == "c":
      try:
        sql = "SELECT `id`, `type`, `number_of_passengers`, `ac`, `in_job` FROM `vehicle` WHERE `in_job` = %s AND `type` = %s"
        val = (0, 'car')
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()
        
        print("\nAVALIBLE VEHICALE LIST :-")
        print()
        
        for vehicle in data:
          print("  Vehicle Number       : ",vehicle[0])
          print("  Vehicle name         : ",vehicle[1])
          print("  Number of Passangers : ",vehicle[2])
          print("  AC Avalibility       : ",vehicle[3])
          print("------------------------------------")
          print()
        
        select = input("Which Vehicle You Want (Wnter Vehicle ID) : ")
        try:
          sql = "UPDATE `vehicle` SET `in_job`= 1 WHERE `id` = %s"
          val = (select,)
          conn.cursor.execute(sql, val)
          data = conn.cursor.fetchall()
          conn.mydb.commit()

          if len(select) != 0: 
            print("Vehicle Successfully Asign to Job..!")

          AsignAgain = input("Are you asign more vehicle from job ? (y/ n) : ")
          print()
          if AsignAgain.lower() == "y":
            clear()
            self.asignVehical()

          else:
            pass

        except:
          print("SQL Query Erorr...!")

      except:
        clear()
        print("Query Erorr..!")
        self.asignVehical()

    # ------------------------------------------------------------------  

    elif whichOne.lower() == "v":
      try:
        sql = "SELECT `id`, `type`, `number_of_passengers`, `ac`, `in_job` FROM `vehicle` WHERE `in_job` = %s AND `type` = %s"
        val = (0, 'van')
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()
        
        print("\nAVALIBLE VEHICALE LIST :-")
        print()
        
        for vehicle in data:
          print("  Vehicle Number       : ",vehicle[0])
          print("  Vehicle name         : ",vehicle[1])
          print("  Number of Passangers : ",vehicle[2])
          print("  AC Avalibility       : ",vehicle[3])
          print("------------------------------------")
          print()
        
        select = input("Which Vehicle You Want (Wnter Vehicle ID) : ")
        try:
          sql = "UPDATE `vehicle` SET `in_job`= 1 WHERE `id` = %s"
          val = (select,)
          conn.cursor.execute(sql, val)
          data = conn.cursor.fetchall()
          conn.mydb.commit()

          if len(select) != 0: 
            print("Vehicle Successfully Asign to Job..!")

          AsignAgain = input("Are you asign more vehicle from job ? (y/ n) : ")
          print()
          if AsignAgain.lower() == "y":
            clear()
            self.asignVehical()

          else:
            pass

        except:
          print("SQL Query Erorr...!")

      except:
        clear()
        print("Query Erorr..!")
        self.asignVehical()

    # ------------------------------------------------------------------  
    
    elif whichOne.lower() == "w":
      try:
        sql = "SELECT `id`, `type`, `number_of_passengers`, `ac`, `in_job` FROM `vehicle` WHERE `in_job` = %s AND `type` = %s"
        val = (0, '3weel')
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()
        
        print("\nAVALIBLE VEHICALE LIST :-")
        print()
        
        for vehicle in data:
          print("  Vehicle Number       : ",vehicle[0])
          print("  Vehicle name         : ",vehicle[1])
          print("  Number of Passangers : ",vehicle[2])
          print("------------------------------------")
          print()
        
        select = input("Which Vehicle You Want (Wnter Vehicle ID) : ")
        try:
          sql = "UPDATE `vehicle` SET `in_job`= 1 WHERE `id` = %s"
          val = (select,)
          conn.cursor.execute(sql, val)
          data = conn.cursor.fetchall()
          conn.mydb.commit()

          if len(select) != 0: 
            print("Vehicle Successfully Asign to Job..!")
          AsignAgain = input("Are you asign more vehicle from job ? (y/ n) : ")
          print()
          if AsignAgain.lower() == "y":
            clear()
            self.asignVehical()

          else:
            pass

        except:
          print("SQL Query Erorr...!")

      except:
        clear()
        print("Query Erorr..!")
        self.asignVehical()

    # ------------------------------------------------------------------  
    
    elif whichOne.lower() == "t":
      try:
        sql = "SELECT `id`, `type`,`size`, `in_job` FROM `vehicle` WHERE `in_job` = %s AND `type` = %s"
        val = (0, 'truck')
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()
        
        print("\nAVALIBLE VEHICALE LIST :-")
        print()
        
        for vehicle in data:
          print("  Vehicle Number       : ",vehicle[0])
          print("  Vehicle name         : ",vehicle[1])
          print("  Size                 : ",vehicle[2], "ft")
          print("------------------------------------")
          print()
        
        select = input("Which Vehicle You Want (Wnter Vehicle ID) : ")
        try:
          sql = "UPDATE `vehicle` SET `in_job`= 1 WHERE `id` = %s"
          val = (select,)
          conn.cursor.execute(sql, val)
          data = conn.cursor.fetchall()
          conn.mydb.commit()

          if len(select) != 0: 
            print("Vehicle Successfully Asign to Job..!")
          AsignAgain = input("Are you asign more vehicle from job ? (y/ n) : ")
          print()
          if AsignAgain.lower() == "y":
            clear()
            self.asignVehical()

          else:
            pass

        except:
          print("SQL Query Erorr...!")

      except:
        clear()
        print("Query Erorr..!")
        self.asignVehical()

    # ------------------------------------------------------------------  
    
    elif whichOne.lower() == "l":
      try:
        sql = "SELECT `id`, `type`,`size`, `in_job` FROM `vehicle` WHERE `in_job` = %s AND `type` = %s"
        val = (0, 'lorry')
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()
        
        print("\nAVALIBLE VEHICALE LIST :-")
        print()
        
        for vehicle in data:
          print("  Vehicle Number       : ",vehicle[0])
          print("  Vehicle name         : ",vehicle[1])
          print("  Size                 : ",vehicle[2], "kg")
          print("------------------------------------")
          print()
        
        select = input("Which Vehicle You Want (Wnter Vehicle ID) : ")
        try:
          sql = "UPDATE `vehicle` SET `in_job`= 1 WHERE `id` = %s"
          val = (select,)
          conn.cursor.execute(sql, val)
          data = conn.cursor.fetchall()
          conn.mydb.commit()

          if len(select) != 0: 
            print("Vehicle Successfully Asign to Job..!")
          AsignAgain = input("Are you asign more vehicle from job ? (y/ n) : ")
          print()
          if AsignAgain.lower() == "y":
            clear()
            self.asignVehical()

          else:
            pass

        except:
          print("SQL Query Erorr...!")

      except:
        clear()
        print("Query Erorr..!")
        self.asignVehical()

    # ------------------------------------------------------------------ 
    
    elif whichOne.lower() == "x":
      pass

    else:
      clear()
      print("Wrong Input...!")
      self.asignVehical()

    

