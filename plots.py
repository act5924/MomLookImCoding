'''
   Assignment 5.1
   Arthur Tonoyan
'''

def lab_average(filename, first, last):
    with open(filename) as file:
        header_fields = next(file).split(',')
        total_grade = 0
        count = 0
        for line in file:
            fields = line.split(',')
            col = 2
            if fields[0] == last and fields[1] == first:
                for i in range(8):
                    #print (total_grade)
                    #print (fields[col])
                    total_grade += float((fields[col]))
                    col += 1
                return total_grade/8
        return None

def get_average(filename, grade_item):
    with open(filename) as file:
        header_fields = next(file).split(',')
        col = int(grade_item[-1]) + 1
        total_grade = 0
        count = 0
        for line in file:
            fields = line.split(',')
            total_grade += int(fields[col])
            count += 1
        return total_grade/count
