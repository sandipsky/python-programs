#program to check if date is valid
import re 

pattern = '(0[1-9]|[12][0-9]|3[01])[-/.](0[1-9]|1[012])[-/.](18|19|20)([0-9]{2})'

date = str(input("Enter a date in DD/MM/YY : "))

result = re.match(pattern, date)
if result:
    if (date[3:5] == '04' or date[3:5] == '06' or date[3:5] == '11' or date[3:5] == '09') and int(date[0:2])>30:
        print("Not valid Date! September, April, June and November has only upto 30 days")
    elif (date[3:5] == '02'):
        if int(date[6:10]) % 4 == 0 and int(date[0:2])<=29:
            print("Date is valid")
        else:
            print("Not valid Date! Febuary has only upto 28 days")
    else:
        print("Date is valid")

else:
    print("Not Valid Date!")

