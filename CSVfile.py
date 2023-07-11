import csv

def temp_sensor():
    x=100
    return x

f = open("CSV.csv","w",newline="") 
c= csv.writer(f)

c.writerow([temp_sensor()])

f.close()