import xlsxwriter 

outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

names = ["a","b","c"]
values = [70,40,30]

outSheet.write ("A1" , "Names")
outSheet.write ("B1" , "Scores")

outSheet.write("A2", names[0])
outSheet.write("A3", names[1])
outSheet.write("A4", names[2])

outSheet.write("B2", values[0])
outSheet.write("B3", values[1])
outSheet.write("B4", values[2])


outWorkbook.close()
