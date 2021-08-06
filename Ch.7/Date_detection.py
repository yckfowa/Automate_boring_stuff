# Clean solution found on reddit thread 
import re

dateRegex = re.compile(r'([0-3]\d)\/([0-1][0-9])\/([1-2]\d{3})')

inputDate = dateRegex.search(input("Please enter a date: "))
day, month, year = [0,0,0]

def check_valid_date(day,month,year):
    monthToDays ={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if year < 1000 or year > 2999:
        return False
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        monthToDays[2] = 29                                     
    if month not in monthToDays.keys():                 
       return False
    if day > monthToDays[month] or day == 0:
       return False
    return True

while inputDate != None:
    day,month,year = int(inputDate.group(1)),int(inputDate.group(2)),int(inputDate.group(3))
    if check_valid_date(day,month,year):
        print('The Date is Valid')
        break
    else:
        print('Valid format, invalid date')
        break
else:
    print('Please input a valid date format; ie. DD/MM/YYYY')
    inputDate = dateRegex.search(input())

