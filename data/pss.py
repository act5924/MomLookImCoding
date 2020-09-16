def guess_game():
    chance = 0
    secret = 6
    while True:
        guess = int(input('guess'))
        try:
            if (secret != guess):
                raise ValueError('Wrong')
            break
        except ValueErrpr as ve:
            chance +=1
            if chance == 3:
                raise ve
            print ('wrong guess') 
    print ('you got it')

def open_file():
    while True:
        file_name = input('enter file name')
        try:
            file = open(file_name)
            return file
        except FileNotFoundError:
            print ('Wrong File Name, TRY AGAIN...')
        
def print_chars(string):
    index = 0
    while True:
        try:
            print (string[i])
            index += 1
        except:
            return len(string)