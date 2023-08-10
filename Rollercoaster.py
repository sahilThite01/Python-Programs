print("Welcome to the Rollercoaster\n")
height = float(input("Type in ur height in cm: "))

if height >= 120:
    print("\nYou can go for the ride!\n")

    age = float(input("Please type in ur age: "))

    if age >= 18:
      print("\nPlease pay $12")

    elif 12 <= age < 18:
      print("\nPlease pay $7") 

    else:
      print("\nPlease pay $5")

else:
    print("\nSorry,You need to grow taller to ride")