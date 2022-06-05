from Connection import Connection
import mysql.connector
import os

# clear cmd
clear = lambda: os.system('cls')

# create connection
conn = Connection()

class Avalible:
  def avalibleVehical(self):
    print(
    """
     ~~~~~~~~~~~~~~~~~~
    | Avalible Vehicle |
     ~~~~~~~~~~~~~~~~~~
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

    def checkVehicalAvalibale(self, VehicleType):
      try:
        sql = "SELECT * FROM `vehicle` WHERE `in_job` = %s AND `type` = %s"
        val = (0, VehicleType)
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()
        clear()
        print("\nAVAILABLE VEHICLE LIST :-")
        print()

        for vehicle in data[:]:
          print("  Vehicle Number       : ",vehicle[0])
          print("  Vehicle name         : ",vehicle[1])
          print("  Number of Passengers : ",vehicle[2])
          print("  AC Availability       : ",vehicle[3])
          print("  Size                 : ",vehicle[4])
          print("------------------------------------")
          print()
        
      except:
        clear()
        print("Query Erorr..!")
        self.avalibleVehical()


    if whichOne.lower() == "c":
      data = checkVehicalAvalibale(self, "car")
      # print("\nAVALIBLE VEHICALE LIST :-")
      print()      
      look = str(input("Are you look more vehicle?  (y/ n) : ")) 
      if look.lower() == "y":
        clear()
        self.avalibleVehical()   
      else:
        pass

      # -------------------------------------------------------------------

    if whichOne.lower() == "v":
      data = checkVehicalAvalibale(self, "van")
      # print("\nAVALIBLE VEHICALE LIST :-")
      print()      
      look = str(input("Are you look more vehicle?  (y/ n) : ")) 
      if look.lower() == "y":
        clear()
        self.avalibleVehical()   
      else:
        pass

      # -------------------------------------------------------------------


    if whichOne.lower() == "w":
      data = checkVehicalAvalibale(self, "3weel")
      
      look = str(input("Are you look more vehicle?  (y/ n) : "))
      
      if look.lower() == "y":
        clear()
        self.avalibleVehical()
      
      else:
        pass

      # -------------------------------------------------------------------


    if whichOne.lower() == "t":
      data = checkVehicalAvalibale(self, "truck")
      
      look = str(input("Are you look more vehicle?  (y/ n) : "))
      
      if look.lower() == "y":
        clear()
        self.avalibleVehical()
      
      else:
        pass

      # -------------------------------------------------------------------

    if whichOne.lower() == "l":
      data = checkVehicalAvalibale(self, "lorry")
      
      look = str(input("Are you look more vehicle?  (y/ n) : "))
      
      if look.lower() == "y":
        clear()
        self.avalibleVehical()
      
      else:
        pass

      # -------------------------------------------------------------------

