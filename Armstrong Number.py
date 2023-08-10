numb = int(input("Type in the number: "))

a=numb
sum=0
while a!=0:
    l=a%10
    l3=l**3
    sum+=l3
    a=a//10
    
if numb==sum:
    print("This is an armstrong number.")
else:
    print("It's not an armstrong number.")