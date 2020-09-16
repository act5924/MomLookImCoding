import plotter



def numbers_1():
    total_sum = 0
    while True:
        filename = input("Enter filename: ")
        if filename == "":
            break
        try:
            with open(filename) as file:
                sum = 0
                for number in file:
                    try:
                        sum += int(number)
                    except:
                        print (number, " is skipped")
                print("Sum of numbers:", sum)
                total_sum += sum
        except FileNotFoundError:
            print ('File Not Found')
        except ValueError:
            print ("File Contains non-numeric data")
    print ("total Sum: " + str(total_sum))        

def errors():
    try: 
        x = int("123") #ValueError
        print ('x = ' + str(x))
        y = 23/2       #ZeroDivisionError
        print ('y = ' + str(y))
        #file = open('nofile.txt')   #FileNotFoundError
        z = '537'
        z[0]           #TypeError
    except:
        print ('error is raised')
    print ('Program continues')  


def division_1():
    errors = 0
    while True:
        numerator = input("Enter a numerator: ")
        denominator = input("Enter a denominator: ")

        if numerator == "" or denominator == "":
            break
        try:
            numerator = float(numerator)
            denominator = float(denominator)

            print("result of dicision =", (numerator / denominator))
        except ValueError as ve:
            if errors > 3:
                #re-raise error
                raise ve
            errors += 1
            print ('non-numeric data type')
        except ArithmeticError as ae:
            if errors > 3:
                #re-raise error
                raise ae
            errors += 1
            print ('Division by 0')


def password():
   
    pwd = input("Enter password: ")
    if len(pwd) < 10 or len(pwd) > 20:
        #raise a ValueError
        raise ValueError('Invalid Length')
    confirmed_pwd = input("Confirm password: ")
    if pwd != confirmed_pwd:
        #raise a ValueError
        raise ValueError('Passwords Don\'t Match')
    print("Good password!")
    
    


def plot_grades(csv_file, first_name, last_name):
    with open(csv_file) as file:
        for line in file:
            fields = line.strip().split(",")
            if fields[0] == last_name and fields[1] == first_name:
                field_count = len(fields)
                plotter.init(first_name + " " + last_name, "Grade Item", "Score")
                for i in range(2, field_count):
                    try:  
                        data_point = float(fields[i])  
                        plotter.add_data_point(data_point)
                    except ValueError:
                        plotter.add_data_point(0)
                    
                plotter.plot()

def main():
    #numbers_1() # no exception handling
   
    #errors()
    #division_1() # no exception handling


    #password()

    plot_grades("data/grades_363.csv", "Deonta", "Gamons")
    input("Press enter to continue...")

if __name__ == "__main__":
    main()