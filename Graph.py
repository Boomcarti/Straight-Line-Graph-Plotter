import math
function = input("Enter a function f(x):\n")
for y in range(10,-11,-1):
    for x in range(-10,11,1):
        func = round(eval(function))
        if x == 0 and y == 0 and y!= func:
            print("+", end="")
        elif y == 0 and y!= func:
            print("-", end="")
        elif x ==0 and y!=func:
            print("|", end="")
        elif y == func:
            print("o", end="")
        else:
            print(" ", end="")
    print("")
    
        
            
