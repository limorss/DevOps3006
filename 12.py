my_file = open('read_this.txt')
print(list(my_file.readlines()))
my_file.seek(0) # Go to the first letter, otherwise won't print anything
my_file.seek(1) # Go to the first letter, otherwise won't print anything
for line in my_file.readlines():
    print(line, end='') # No additional \n in print
    #print(line.strip()) # same remove space in the beginning from the end space, tabs, \n