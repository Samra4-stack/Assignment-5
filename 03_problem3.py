# Question no 3 ()
age = int(input("Enter your age:"))

if(age >= 0 and age <= 12):
    you_are = "Child"
elif(age >= 13 and age <= 19):
    you_are =" Teenager"
elif(age >= 20 and age <= 59):
    you_are = "Adult"
elif(age >= 60 ):
    you_are = "Senior Citizen" 
else:
    print("Invalid Age")
print( "you_are", you_are , age) 