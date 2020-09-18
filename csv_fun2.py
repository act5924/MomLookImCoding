import csv
import re

with open('data/full_grades_010.csv') as file:
    records = csv.reader(file)
    row0 = next(records)
    print(row0)
    row1 = next(records)
    print (row1)

def reg_ex():
    #if re.findall("[R-T][a-Za-Z]*,[a-zA-Z]+","Steve,Johns"):
    if re.findall("\d{5}","abcde"):
        print ('match')
    else:
        print ('no match')

def opener(filename):
    try:
        with open(filename) as file:
            return True
    except:
        return False

def name_address(filename):
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            print ('name = ' + row[0] + ', address = ' + row[1])

def average(filename, column):
    with open(filename) as file:
        rows = csv.reader(file)
        sum = 0
        count = 0
        next(rows)
        for row in rows:
            sum += float(row[column])
            count += 1
        print ('average = ' + str(sum/count))
        

def average(filename, column):
    with open(filename) as file:
        rows = csv.reader(file)
        sum = 0
        count = 0
        next(rows)
        for row in rows:
            address = row[1]
            if re.findall("[789][0-9]{4}",address):
                print("name = " + str(row[0], ", address = ", + str(row[1])))

#name_address('data/full_grades_010.csv')
#average('data/full_grades_010.csv', 3)
reg_ex()