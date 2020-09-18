'''
Arthur Tonoyan
Assignment 5.2
'''
import plots

def student_average():
    while True:
        lst = input('Enter the... File FirstName LastName (Enter to go back): ')
        bst = lst.split()
        if lst == '':
            return True
        try:
            if len(bst) > 3:
                raise IndexError
            if plots.plot_grades(bst[0], bst[1], bst[2]) == True:
                print ('Plot finished (window may be hidden)')
                return True
            else:
                print ('Plot failed (no such student)')
                True
        except FileNotFoundError:
            print ('No such file: ' + str(bst[0]))
            True
        except IndexError:
            print ('Usage for stu: <filename> (space) <first name> (space) <last name>')
            True

def print_average():
    while True:
        lst = input('Enter the... File GradeItem(#) (Enter to go back): ')
        bst = lst.split()
        if lst == '':
            return True
        try:
            if len(bst) > 2:
                raise IndexError
            col = int(bst[1])
            print ('Average: ' + str(plots.get_average_new(bst[0], col)))
            return True
        except FileNotFoundError:
            print ('No such file: ' + str(bst[0]))
            True
        except IndexError:
            print ('Usage for avg: <filename> (space) <Grade Item (#)>')
            True
        except ValueError:
            print ('GradeItem must be a number')
        
def class_average():
    while True:
        lst = input('Enter the... File (Enter to go bacK): ')
        try:
            if len(lst.split()) > 1:
                raise IndexError
            plots.plot_class_averages(lst)
            print ('Plot is finished (window may be hidden)')
            return True
        except FileNotFoundError:
            print ('No such file: ' + str(lst))
            True
        except IndexError:
            print ('Usage for avg: <filename> (space) <Grade Item (#)>')
            True


def quit():
    quit_quit = input('Are you sure (y/n) : ')
    if quit_quit == 'y' or quit_quit == 'Y':
        return True
    else:
        return False
    
def main():
    print ('>> ')
    while True:
        print ('Enter a command or \'quit\' to quit')
        command = input('>> ')
        command_split = command.split()
        try:
            if command_split[0] == 'quit':
                if quit() == True:
                    print ('Goodbye!')
                    break
            if command == 'stu':
                student_average()
            if command == 'avg':
                print_average()
            if command == 'cavg':
                class_average()
        except IndexError:
            True



if __name__ == '__main__':
    main()
    #print_average()