import os

from Connection import Connection
from Remove import Remove
from Add import Add
from Asign import Asign
from Release import Release
from Avalible import Avalible

clear = lambda: os.system('cls')

conn = Connection()
add = Add()
remove = Remove()
asign = Asign()
release = Release()
avalible = Avalible()

# Function create --------------------------------------
class Main():

  def Home(self):
    clear()
    print(
      """
      ~~~~~~~~~~~~~~~~~~~~~~
    | Welcome to Cab Service |
      ~~~~~~~~~~~~~~~~~~~~~~

  Add a new vehicle -----------> (a)

  Remove a vehicle ------------> (r)

  Assign a job ----------------> (j)

  Release form assigned job ---> (w)
  
  See available vehicles ------> (s)

  Exit ------------------------> (x)
      """
    )

    try:
      selectCatagory = str(input("Enter Letter : "))
    except:
      print("Please Enter Letter...!")
      self.Home()
    
    if selectCatagory.lower() in ['a', 'r', 'j', 'w', 's', 'x']:

      # If select a
      if selectCatagory.lower() == "a":
        clear()
        add.addVehical()
        self.Home()
      
      # If select r
      elif selectCatagory.lower() == "r":
        clear()
        remove.removeVehical()
        self.Home()
      
      # If select j
      elif selectCatagory.lower() == "j":
        clear()
        asign.asignVehical()
        self.Home()
      
      # If select j
      elif selectCatagory.lower() == "w":
        clear()
        release.releaseVehical()
        self.Home()
     
      # If select s
      elif selectCatagory.lower() == "s":
        clear()
        avalible.avalibleVehical()
        self.Home()

    else:
      clear()
      print("Please enter related LETTER (a, r, j, w, s, x)")
      self.Home()


if __name__ == "__main__":
  ob = Main()
  ob.Home()

