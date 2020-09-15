'''
   Assignment 5.1
   Arthur Tonoyan
'''

import plots
import testing

def lab_average_test():
    testing.assert_floats('lab_average', 80.66, plots.lab_average('data/grades_010.csv', 'Sion', 'Lobasso'), 0.05, True)

def lab_average_test_None():
    assert(plots.lab_average('data/grades_010.csv', 'Bob', 'Bobson') == None)
    print ("Lab_average_test_None passed...")

def main():
    #lab_average_test()
    lab_average_test_None()

if __name__ == '__main__':
    main()
