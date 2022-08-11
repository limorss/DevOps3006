def save_name(names_file):
    my_file = open(names_file, "a") # add in the end
    current_name = input("Enter your name: ")
    my_file.write(current_name + "\n")
    my_file.close()
def haim(avi):
    print(avi)
def show_names(names_file, blabla):
    my_file = open(names_file, "r")  # add in the end
    for name in my_file.readlines():
        print(name, end='')
    my_file.close()
    print(blabla)


def moshe(david):
    print(david)


for i in range(5):
    save_name("names.txt")

show_names("names.txt")
