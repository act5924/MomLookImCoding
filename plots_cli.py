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
        except IndexError:
            True



if __name__ == '__main__':
    main()
    #student_average()