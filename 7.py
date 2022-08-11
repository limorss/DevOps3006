number_boom = 7
max = 100
number_boom_str = f"{number_boom}"
numbers = list(range(max))
for number in numbers:
    if number % number_boom == 0 or number_boom_str in str(number):
        continue
    print(number)


# =>
for number in numbers:
    if number % number_boom != 0 and not number_boom_str in str(number):
        print(number)
else:
    print("loop finished successfully")



a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("blabla")
