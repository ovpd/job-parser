import xlwt

book = xlwt.Workbook(encoding="utf-8")

# Add a sheet to the workbook
sheet1 = book.add_sheet("Python Sheet 1")

# Write to the sheet of the workbook
sheet1.write(0, 0, "zero zero")
sheet1.write(0, 2, "zero two")
sheet1.write(1, 0, "one zero")
sheet1.write(1, 2, "one two")
# Save the workbook
book.save("hello.xls")
