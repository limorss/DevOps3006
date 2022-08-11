string_to_print = "hello world"
print(string_to_print)
print(string_to_print)
print(string_to_print)
print(string_to_print)
print(string_to_print)
print(string_to_print)

print((string_to_print + "\n") * 5)

print(list(range(1, 3)))
print(list(range(17, 2, -3))) # => [17, 14, 11, 8, 5]
print(list(range(17, 2, 3))) # => []

for i in range(8): # means 0, 1, 2 , 3, 4, 5, 6, 7 (t times)
    #print(string_to_print)
    print(i)

names = ["chanan", "tom", "zack","aharon"]

for name in names:
    print(name)

for name in names:
    print(name, end='')

for i in range(len(names)):
    print(names[i])

a = 0
while a < 5:
    print(a)
    a = a + 1

break_on_name = "zack"
for name in names:
    if break_on_name == name:
        continue
    else:
        pass
    print(name)

