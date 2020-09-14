import plotter

def forloop(filename):
    input_file = open(filename)

    for line in input_file:
        stripped = line.strip()
        print (stripped)

    input_file.close()

def wordsearch(filename):
    word = input("enter a word: ")
    input_file = open(filename)
    for line in input_file:
        if line.strip() == word:
        #+ '\n'
            print ("Word Found,\n" + 'User searched for: ' + str(word))
            input_file.close()
            return
    print ("Word not Found,\n" + 'User searched for: ' + str(word))
    input_file.close()

def longest_word(filename):
    input_file = open(filename)
    for line in input_file:
        words = line.split()
        longest_word = ""
        for word in words:
            if len(longest_word) < len(word):
                longest_word = word
        print (longest_word)
    input_file.close()

def print_names(filename):
    file = open(filename)
    next(file)
    for line in file:
        fields = line.split(',')
        print (fields[0], fields[1])
    file.close()

def write_files(filename):
    file = open(filename, "w")
    file.write("Hi there.\n")
    file.write("Good bye.\n")
    file.write("This is the end")

def promp_write(filename):
    with open(filename, 'w') as file:
        user_input = input("Write Something: ")
        while user_input != '':
            file.write(user_input)
            file.write('\n')
            user_input = input("Write Something: ")
    #file.close()

def class_avg(filename, column):
    with open(filename) as file:
        header_fields = next(file).split(',')
        print ("average of", header_fields[column])
        total_sum = 0
        count = 0
        for line in file:
            fields = line.split(',')
            total_sum += float(fields[column])
            count += 1
        average = total_sum/count
        return average
    
def plotting():
    # init with title and axis labels
    plotter.init("My Graph", "X-Axis", "Y-Axis")
    # first series is started by init()
    plotter.add_data_point(100)
    plotter.add_data_point(25)
    plotter.add_data_point(37)
    # add second series
    plotter.new_series()
    plotter.add_data_point(75)
    plotter.add_data_point(65)
    plotter.add_data_point(100)
    # draw the plot!
    plotter.plot()
    input('Enter to quit: ')

def plot_grade(filename, column):
    with open(filename) as file:
        header_fields = next(file).split(',')
        plotter.init(header_fields[column], "Students", "Score/Grade")
        for line in file:
            fields = line.split(',')
            plotter.add_data_point(float(fields[column]))
        plotter.plot()
        input('Enter to quit: ')

def main():
    filename = input('enter file name: ')
    #forloop(filename)
    #wordsearch(filename)
    #longest_word(filename)
    #print_names(filename)
    #write_files(filename)
    #promp_write(filename)
    #print (class_avg(filename, 3))
    #plotting()
    plot_grade(filename, 2)

if __name__ == "__main__":
    main()