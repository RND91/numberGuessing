
import random

count = 0
if count<6:   
    for i in range(1,6):
       
        entry=int(input("Enter your number: "))
        digit = random.randint(1,5)
       
        if entry<digit:
            count = count+1
            print("very small number")
            
       
        if entry>digit:
            count = count+1
            print("very large number")
            
        if entry==digit:
            count=count+1
            print("awesome")
            break
            
        if count==5 and entry!=digit:
            print("You lose")
           

       
