number = int(input("Enter a number: "))

# (Number is even or odd)
if(number%2 == 0):
    print("Number is even =" , number)
else:
    print("Number is odd =" , number)
    
# (Number is Positive , Negative or Zero )   
if(number==0):
    print("Number is zero")
elif(number>0):
    print("Number is positive")
else:
    print("Number is negative")
  
# (Number  is divisible by both 2 and 3 or anyone of them or not divisible by both )    
if(number%2==0 and number%3==0):
    print("Number is divisible by both 2 and 3")
elif(number%2==0 or number%3==0):
    print("Number is divisible by either 2 or 3")
else:
    print("Number is not divisible by 2 and 3")