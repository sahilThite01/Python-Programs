i=0
while i in range(0,1):
    calci = input("Type in the format ➜ (number) (operation) (number)\n{Operations allowed ➜ '+' '-' 'x' '/'}  ➜  : ").split()

    
    a=int(calci[0])
    op=calci[1]
    b=int(calci[2])

    def maths(a,op,b):
        if op == "+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "x":
            print(a*b)
        elif op == "/":
            print(a/b)
    
    maths(a,op,b)
    print("")
    
