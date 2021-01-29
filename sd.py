import csv
import math

with open("data.csv",newline='') as csvfile:
    reader = csv.reader(csvfile)
    fileData = list(reader)


data = fileData[0]
sum = 0
for number in data:
    sum += int(number)

mean = sum/(len(data))

sl = []
for number1 in data:
    sub = int(number1)-mean
    sub = sub**2
    sl.append(sub)

sum2=0
for number2 in sl:
    sum2+=number2

sdsquare = sum2/(len(data)-1)

sd = math.sqrt(sdsquare)

print(sd)