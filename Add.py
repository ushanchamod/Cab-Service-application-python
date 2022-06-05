from Connection import Connection
import mysql.connector
import os

# clear cmd
clear = lambda: os.system('cls')

# create connection
conn = Connection()

class Add:

  # ADD VEHICAL MAIN
  def addVehical(self):
    print(
    """
           ~~~~~~~~~~~~~
          | Add Vehicle |
           ~~~~~~~~~~~~~

    Car ------------------> (c)

    Van ------------------> (v)

    3 Wheelers -----------> (w)

    Trucks ---------------> (t)

    Lorry ----------------> (l)

    Go to Home -----------> (x)
    """
    )

    # Get Input
    selected = str(input("Enter Letter : "))

    if selected.lower() in ['c', 'v', 'w', 't', 'l', 'x']:
      if selected.lower() == 'c':
        clear()
        print(
        """
         ~~~~~~~~~
        | Add Car |
         ~~~~~~~~~
        """
        )

        try:
          vehicalNumber = str(input("Enter Vehicle Number : "))
          numberOdPassangers = int(input("Enter number of passengers (3 or 4): "))
          ac = str(input("Enter AC is avalible or not avalible (y or n): "))
          if ac.lower() == "y":
            ac = 1
          elif ac.lower() == "n":
            ac = 0

          try:
            sql = ("INSERT INTO `vehicle`(`id`,`type`, `number_of_passengers`, `ac`, `in_job`) VALUES (%s, 'car', %s, %s, 0)")
            val = (vehicalNumber, numberOdPassangers, ac)
            conn.cursor.execute(sql, val)
            
            conn.mydb.commit()

            clear()
            print("One Car Added....!")
            self.addVehical()

          except:
            clear()
            print("query problem")
            self.addVehical()
        except:
          clear()
          print("Query Error...!")
          self.addVehical()
  
      # Add van
      elif selected.lower() == 'v':
        clear()
        print(
        """
         ~~~~~~~~~
        | Add Van |
         ~~~~~~~~~
        """
        )

        try:
          vehicalNumber = str(input("Enter Vehicle Number : "))
          numberOdPassangers = int(input("Enter number of passengers (6 or 8): "))
          ac = str(input("Enter AC is avalible or not avalible (y or n): "))
          if ac.lower() == "y":
            ac = 1
          elif ac.lower() == "n":
            ac = 0

          try:
            sql = ("INSERT INTO `vehicle`(`id`, `type`, `number_of_passengers`, `ac`, `in_job`) VALUES (%s, 'van', %s, %s, 0)")
            val = (vehicalNumber, numberOdPassangers, ac)
            conn.cursor.execute(sql, val)
            
            conn.mydb.commit()

            clear()
            print("One Van Added....!")
            self.addVehical()

          except:
            clear()
            print("query problem")
            self.addVehical()
        except:
          clear()
          print("Something Wrong...!")
          self.addVehical()
      
      

      # 3 Wheelers
      elif selected.lower() == 'w':
        clear()
        print(
        """
         ~~~~~~~~~~~~
        | Add 3 Weel |
         ~~~~~~~~~~~~
        """
        )
        
        try:
          vehicalNumber = str(input("Enter Vehical Number : "))

          try:
            sql = ("INSERT INTO `vehicle`(`id`, `type`, `number_of_passengers`, `ac`, `in_job`) VALUES (%s, %s, 3, 0, 0)")
            val = (vehicalNumber, "3weel")
            conn.cursor.execute(sql, val)
            conn.mydb.commit()

            clear()
            print("One 3 Weel Added....!")
            self.addVehical()

          except:
            clear()
            print("query problem")
            self.addVehical()
        except:
          clear()
          print("Query Error...!")
          self.addVehical()
      
      
      # Truck
      elif selected.lower() == 't':
        clear()
        print(
        """
         ~~~~~~~~~~~
        | Add Truck |
         ~~~~~~~~~~~
        """
        )
        
        try:
          vehicalNumber = str(input("Enter Vehical Number : "))
          vehicalSize = str(input("Enter Vehical Size [7 or 12 (ft)] : "))

          try:
            sql = ("INSERT INTO `vehicle`(`id`, `type`, `size`, `in_job`) VALUES (%s, 'truck', %s, 0)")
            val = (vehicalNumber, vehicalSize)
            conn.cursor.execute(sql, val)
            conn.mydb.commit()

            clear()
            print("One Truck Added....!")
            self.addVehical()

          except:
            clear()
            print("query problem")
            self.addVehical()
        except:
          clear()
          print("Query Error...!")
          self.addVehical()
      
      
      # lorry
      elif selected.lower() == 'l':
        clear()
        print(
        """
         ~~~~~~~~~~~
        | Add Lorry |
         ~~~~~~~~~~~
        """
        )
        
        try:
          vehicalNumber = str(input("Enter Vehical Number : "))
          vehicalSize = str(input("Enter Vehical Size [2500 and 3500 (kg)] : "))

          try:
            sql = ("INSERT INTO `vehicle`(`id`, `type`, `size`, `in_job`) VALUES (%s, 'lorry', %s, 0)")
            val = (vehicalNumber, vehicalSize)
            conn.cursor.execute(sql, val)
            conn.mydb.commit()

            clear()
            print("One Lorry Added....!")
            self.addVehical()

          except:
            clear()
            print("query problem")
            self.addVehical()
        except:
          clear()
          print("Query Error...!")
          self.addVehical()
     
    #  terminating point
      elif selected.lower() == 'x':
        clear()

    else:
      clear()
      print("wrong input. Try again......!")
      self.addVehical()
    
