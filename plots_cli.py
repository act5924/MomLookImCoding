'''
Arthur Tonoyan
Assignment 5.2
'''



def quit():
    quit_quit = input('Are you sure (y/n) : ')
    if quit_quit == 'y' or quit_quit == 'Y':
        return True
    else:
        return False
    
def main():
    print ('>> ')
    print ('Enter a command or \'quit\' to quit')
    command = input('>> ')
    command_split = command.split()
    while True:
        try:
            if command_split[0] == 'quit':
                if quit() == True:
                    print ('Goodbye!')
                    break
                else:
                    raise IndexError
        except IndexError:
            print ('Enter a command or \'quit\' to quit')
            command = input('>> ')
            command_split = command.split()


main()
