# Question no 2 (Take the user age and check if they can give vote or not)
age = int(input("Enter your age: "))

if(age>=18):
    nationality = input("Do you have a nationality of 'Pakistani'? ")
    if(nationality.lower() == "Yes".lower()):
        print("You are eligible to vote")
    else:
        print("Please obtain a valid ID to vote")
else:
    print("You are minor to vote")