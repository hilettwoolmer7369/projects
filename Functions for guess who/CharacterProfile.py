import picamera, time

#Gets a picture of the user
print ("To take your your picture type in getPicture(name)")
def getPicture(name):
   try:
      check=False
      while check == False:
         print ("smile")
         with picamera.PiCamera() as camera:
            camera.resolution = (1024,768)
            camera.start_preview()
            time.sleep(5)
            filename = "You Have been saved as {0}.jpg".format(name)
            camera.capture(filename)
            camera.stop_preview()
            correct=input("are you happy with your picture? Y/N")
            if correct.lower()== "Y":
                  check = True
         return filename
   except picamera.exc.PiCameraMMALError:
         print ("please reconect the Picamera to continue")
         filename=""
   return filename

   def getCharacteristics():
      check=False
      while check == False:
         eye_color = ""
         while not(eye_color.lower in ("blue","brown","green","hazel","pink","yellow")):
            eye_color = input("eye color?")
         hair_Color =  ""
         while not (hair_color.lower in ("black", "brown", "blonde", "ginger")):
            hair_color = input("What is your hair color?")
         Hat = ""
         while not (Hat.lower in ("yes", "no")):
           hat = input("Are you wearing a hat")
         Glasses = ""
         while not (Glasses.lower in ("yes", "no")):
            Glasses = input("Are you wearing any glasses")
         Gender = ""
         while not (Gender.lower in ("male", "female")):
            Gender = input("Are you male or female")
      













         
         
        
    
