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
    #else:
        #return None


def get_average(filename, grade_item):
    with open(filename) as file:
        header_fields = next(file).split(',')
        col = getcol(grade_item)
        #if col == None:
            #return None
        total_grade = 0
        count = 0
        for line in file:
            fields = line.split(',')
            if fields[col] == '':
                fields[col] = 0
            total_grade += float(fields[col])
            count += 1
        return total_grade/count
