# Question no 4 (Take month number & Print the number of days in that month)
month_number = int(input("Enter the month number: "))

numbers = 1,3,5,7,8,10,12
numbers2 = 4,6,9,11
numbers3 = 2

if(month_number in numbers):
    print("The month" , month_number , "have 31 Days")
elif(month_number in numbers2):
    print("The month" , month_number , "have 30 Days")
elif(month_number == numbers3):
    print("The month" , month_number , "have 28 Days")
else:
    print("Invalid month number")