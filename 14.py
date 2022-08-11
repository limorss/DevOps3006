import ast
my_file = open("config.json")
a = "haim"
c = dict(ast.literal_eval(my_file.read()))
# configuration = dict(ast.literal_eval(my_file.read()))
print(c["name"])



with open("names.txt") as my_file:
    for name in my_file.readlines():
        print(name.strip())
