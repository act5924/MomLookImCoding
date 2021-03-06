'''
   Assignment 5.1
   Arthur Tonoyan
'''
import plotter
import csv
import re

def lab_average(filename, first, last):
    with open(filename) as file:
        lines = csv.reader(file)
        next(lines)
        total_grade = 0
        count = 0
        for line in lines:
            col = 3
            if re.findall(first and last, line[0]):
                for i in range(10):
                    #print (total_grade)
                    #print (line[col])
                    total_grade += float((line[col]))
                    col += 1
                return total_grade/10
        return None


def getcol(grade_item):
    if grade_item == 'Lab 1':
        return 2
    if grade_item == 'Lab 2':
        return 3
    if grade_item == 'Lab 3':
        return 4
    if grade_item == 'Lab 4':
        return 5
    if grade_item == 'Lab 5':
        return 6
    if grade_item == 'Lab 6':
        return 7
    if grade_item == 'Lab 7':
        return 8
    if grade_item == 'Lab 8':
        return 9
    if grade_item == 'Lab 9':
        return 10
    if grade_item == 'Lab 10':
        return 11
    else:
        return None


def get_average(filename, grade_item):
    with open(filename) as file:
        lines = csv.reader(file)
        next(lines)
        col = getcol(grade_item) + 1
        if col == None:
            return None
        total_grade = 0
        count = 0
        for line in lines:
            if line[col] == '':
                line[col] = 0
            total_grade += float(line[col])
            count += 1
        return total_grade/count

def get_average_new(filename, col):
    with open(filename) as file:
        lines = csv.reader(file)
        next(lines)
        total_grade = 0
        count = 0
        for line in lines:
            if line[col] == '':
                line[col] = 0
            total_grade += float(line[col])
            count += 1
        return total_grade/count

def plot_grades(filename, first, last):
    with open(filename) as file:
        lines = csv.reader(file)
        next(lines)
        plotter.init(str(first) + ' ' + str(last), "Labs", "Score")
        for line in lines:
            col = 3
            if re.findall(first and last, line[0]):
                for i in range(len(line) - 3):
                    plotter.add_data_point(float(line[col]))
                    col += 1
                plotter.plot()
                var = input('Enter to continue: ')
                return True
        
        return False
    
def plot_class_averages(filename):
    with open(filename) as file:
        header_fields = next(file).split(',')
        plotter.init("Class Average(" + str(filename) + ')', "Labs", "Score")
        col = 3
        for i in range(27):
            plotter.add_data_point(float(get_average_new(filename, col)))
            col += 1
        plotter.plot()
        var = input('Enter to continue: ')

def main():
    plot_grades('data/full_grades_010.csv', 'Sion', 'Lobasso')
    plot_class_averages('data/full_grades_010.csv')
    plot_class_averages('data/full_grades_999.csv')
    #print (lab_average('data/grades_010.csv', 'Sion', 'Lobasso'))

if __name__ == '__main__':
    main()
