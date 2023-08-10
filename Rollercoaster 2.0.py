print("Welcome to the Rollercoaster")

height=float(input("Type ur height in cm: "))

if height >= 120:
  print("You can go for the ride")

  age=int(input("Type in ur age: "))

  if age >= 18:
    a=int("12")
  elif 12 <= age < 18:
    a=int("7")
  else:
    a=int("5")

  photo=input("Want photos?(Y/N) ")

  if photo == "Y":
    print(f"Please pay ${a + 3}")
  #else:
    #print(f"Please pay ${a}")
    
  print(f"Please pay ${a}")

else:
  print("Sorry, you need to grow taller before you ride")




  