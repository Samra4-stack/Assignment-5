# Question no 5 (Check if the year is leap or not)

year = int(input("Enter the Year: "))

if( len(str(year))>4 or len(str(year))<4 or (year < 0)):
    print( year , "Invalid Year")
elif(year%4 == 0):
    print(year, "is  a  leap year")
elif(year%4 > 0 ):
    print(year, "is not a leap year")
else:
    print(year, " ") 