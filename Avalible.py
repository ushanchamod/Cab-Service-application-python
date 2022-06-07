from Connection import Connection
import mysql.connector
import os

# clear cmd
clear = lambda: os.system('cls')

# create connection
conn = Connection()

class Avalible():
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
    whichOne = str(input("What vehicle are you looking for? : ")).lower()

    def getQueryValue(vehicleType):
      if whichOne in ['c', 'v', 'w', 't', 'l']:

        if vehicleType == "c":

          howManyPassengers = int(input("Maximum number of passengers(3 or 4) : "))
          acAvailability = input("Should the vehicle have AC?(y or n) : ").lower()
          
          if (howManyPassengers == 3 or howManyPassengers == 4):
            if acAvailability == 'y':
              val = (0, 'car', howManyPassengers, 1)
            else:
              val = (0, 'car', howManyPassengers, 0)
          else:
            clear()
            print("Number of passengers wrong...!")
            self.asignVehical()
          
          return val
            
          
        elif vehicleType == "v":
          howManyPassengers = int(input("Maximum number of passengers(6 or 8) : "))
          acAvailability = input("Should the vehicle have AC?(y or n) : ").lower()
          
          if (howManyPassengers == 6 or howManyPassengers == 8):
            if acAvailability == 'y':
              val = (0, 'van', howManyPassengers, 1)
            else:
              val = (0, 'van', howManyPassengers, 0)
          else:
            clear()
            print("Number of passengers wrong...!")
            self.asignVehical()

          return val


        elif vehicleType == "w":
          val = (0, '3weel')

        elif vehicleType == "t":
          size = str(input("Size(7 or 12 ft) : "))
          
          if (size == '7' or size == '12'):
            if size == '7':
              val = (0, 'truck', 7)
            elif size == '12':
              val = (0, 'truck', 12)
          else:
            clear()
            print("Size is wrong...!")
            self.asignVehical()
          
          return val


        elif vehicleType == "l":
          size = str(input("Size(2500 or 3500 Kg) : "))
          
          if (size == '2500' or size == '3500'):
            if size == '2500':
              val = (0, 'lorry', 2500)
            elif size == '3500':
              val = (0, 'lorry', 3500)
          else:
            clear()
            print("Size is wrong...!")
            self.asignVehical()
          
          return val

      else:
        clear()
        print("Invalid Input Letter...!")
        self.avalibleVehical()

    if whichOne == "x":
      pass

    else:
      # For Car and Van
      if whichOne == 'c' or whichOne == 'v':
        val = getQueryValue(whichOne)
        sql = "SELECT `id`, `type`, `number_of_passengers`, `ac` FROM `vehicle` WHERE `in_job` = %s AND `type` = %s AND `number_of_passengers` = %s AND `ac` = %s"
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()

        if len(data) >= 1:
          clear()
          print("AVALIBLE VEHICLE")
          for vehicle in data:
            print()
            print("  Vehicle Number       : ",vehicle[0])
            print("  Vehicle name         : ",vehicle[1])
            print("  Number of Passengers : ",vehicle[2])
            print("  AC Availability      : ",vehicle[3])
            print("------------------------------------")
            print()

          vehicleID = data[0][0]

          needUpdate = str(input("Do you need see more avalible vehicle(y or n) : ")).lower()

          if needUpdate == 'y':
            clear()
            self.avalibleVehical()

        else:
          clear()
          print("Not avalible vehicle...!")
          self.avalibleVehical()

      # For weel
      elif whichOne == 'w':
        val = getQueryValue(whichOne)
        sql = "SELECT `id`, `type`, `number_of_passengers` FROM `vehicle` WHERE `in_job` = %s AND `type` = %s"
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()

        if len(data) >= 1:
          clear()
          print("AVALIBLE VEHICLE")
          for vehicle in data:
            print()
            print("  Vehicle Number       : ",data[0][0])
            print("  Vehicle name         : ",data[0][1])
            print("------------------------------------")
            print()

          vehicleID = data[0][0]

          needUpdate = str(input("Do you need see more avalible vehicle(y or n) : ")).lower()

          if needUpdate == 'y':
            clear()
            self.avalibleVehical()

        else:
          clear()
          print("Not avalible vehicle...!")
          self.avalibleVehical()
      
      # Lorry or Trucks
      elif whichOne == 'l' or whichOne == 't':
        val = getQueryValue(whichOne)
        sql = "SELECT `id`, `type`,`size`, `in_job` FROM `vehicle` WHERE `in_job` = %s AND `type` = %s AND `size` = %s"
        conn.cursor.execute(sql, val)
        data = conn.cursor.fetchall()
        conn.mydb.commit()

        if len(data) >= 1:
          clear()

          print("AVALIBLE VEHICLE")
          for vehicle in data:
            print()
            print("  Vehicle Number       : ",data[0][0])
            print("  Vehicle name         : ",data[0][1])
            print("  size                 : ",data[0][2])
            print("------------------------------------")
            print()
          
          vehicleID = data[0][0]

          needUpdate = str(input("Do you need see more avalible vehicle(y or n) : ")).lower()

          if needUpdate == 'y':
            clear()
            self.avalibleVehical() 

        else:
          clear()
          print("Not avalible vehicle...!")
          self.avalibleVehical()