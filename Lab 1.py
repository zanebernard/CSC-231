input_file = open('ATale2.txt', 'r')
line = input_file.readline()
while line != '':
    print(line)
    line = input_file.readline()
