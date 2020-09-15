'''
   Assignment 5.1
   Arthur Tonoyan
'''

import plots
import testing

def lab_average_test():
    testing.assert_floats('lab_average', 80.66, plots.lab_average('data/grades_010.csv'))

def main():
    lab_average_test()

if __name__ == '__main__':
    main()
