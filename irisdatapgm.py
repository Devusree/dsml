import csv
with open('D:\mca07\iris.data','rb') as csvfile:
lines=csv.read(csvfile)
forrow in lines
print ','.join(row)