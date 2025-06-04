
print("FAN SIMULATION")

action = ''
operating = False

while True:
     option = input("> ").lower()
     if option == "help":
         print("""
ON- mean fans is on and blowing
OFF- means fan in off
STATUS- states the status of the fan
Speed- used to changes speed of fan
UNPLUG- means fan is unoperational""")

     elif option =="on":
         if operating:
             print("fan is already on")
         else:
             operating= True
             setting = input("select a speed for the fan, (Low, Medium or High): ").upper()
             print(f"fan is on and blowing at {setting} speed ")

     elif option == "status":
         if operating:
             print(f"fan is on and at {setting} speed")
         else:
             if not operating:
                 print("fan is off")

     elif option == "speed":
         if operating:
             print(f"current speed is {setting}")
             setting = input("enter prefered speed (Low, MEdium or High): ").upper()
             print(f"speed has been set to {setting} speed")
         if not operating:
             print("fan is not on, type 'help' for more")


     elif option == "off":
         if not operating:
             print("fan is already turned off")
         else:
             operating= False
             print("fan is turned off...")

     elif option == "unplug":
         print("Fan is unoperational, its time to wake up")
         break
     else:
         print("sorry i didnt understand that, type 'help' for more info")
