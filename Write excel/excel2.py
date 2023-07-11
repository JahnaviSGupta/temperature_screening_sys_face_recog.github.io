import xlsxwriter 
import datetime

now = datetime.datetime.now()
time=(now.strftime("%H:%M:%S"))
date=(now.strftime("%d-%m-%y"))

outWorkbook = xlsxwriter.Workbook("out2.xlsx")
outSheet = outWorkbook.add_worksheet()

names = ["a","b","c"]
temp = [70,40,30]



outSheet.write ("A1" , "Names")
outSheet.write ("B1" , "Temperature")
outSheet.write ("C1" , "Time")
outSheet.write ("D1" , "Date")

outSheet.write(1 , 2 ,time)
outSheet.write(1 , 3 ,date)

for item in range(len(names)):
    outSheet.write(item+1 , 0 ,names[item]) 
    outSheet.write(item+1 , 1 ,temp [item]) 
    outSheet.write(item+1 , 2 ,time) 
    outSheet.write(item+1 , 3 ,date) 




outWorkbook.close()
