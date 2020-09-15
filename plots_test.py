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

def get_average_test_Lab6():
    testing.assert_floats('get_average', 67.77, plots.get_average('data/grades_010.csv', 'Lab 6'), 0.05, True)

def get_average_test_Lab3():
    testing.assert_floats('get_average', 82.61, plots.get_average('data/grades_010.csv', 'Lab 3'), 0.05, True)

def get_average_test_None():
    assert(plots.get_average('data/grades_010.csv', 'Lab 137') == None)
    print ("get_average_test_None passed...")

def main():
    #lab_average_test()
    #lab_average_test_None()
    #get_average_test_Lab6()
    #get_average_test_Lab3()
    get_average_test_None()

if __name__ == '__main__':
    main()
