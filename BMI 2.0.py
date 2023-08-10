# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight/height**2

if bmi < 18.5:
    a="are underweight"
elif bmi < 25:
    a="have a normal weight"
elif bmi < 30:
    a="are slightly overweight"
elif bmi < 35:
    a="are obese"
else:
    a="are clinically obese"

print(f"Your BMI is {round(bmi)}, you {a}.")