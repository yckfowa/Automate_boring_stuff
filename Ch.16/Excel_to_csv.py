import os
import csv
import openpyxl

for excel_file in os.listdir("."):
    if not excel_file.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(excel_file)

    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]

        csv_file_name = excel_file.split('.')[0] + '_' + sheet.title + '.csv'
        csv_file_obj = open(csv_file_name, "w", newline='')
        csv_writer = csv.writer(csv_file_obj)

        for row_obj in sheet.rows:
            row_data = []
            for cell_obj in row_obj:

                row_data.append(cell_obj.value)

            csv_writer.writerow(row_data)

        csv_file_obj.close()
print("Done")
