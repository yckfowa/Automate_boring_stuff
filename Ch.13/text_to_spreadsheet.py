import openpyxl

f = open('test.txt', 'r')
x = f.readlines()

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(len(x)):
    for j in range(len(x[i].split())):
        rw = i+1
        col = j+1
        sheet.cell(row=rw, column=col).value = x[i].split()[j]

wb.save("123.xlsx") # create new .xlsx file
f.close()

print("Completed")