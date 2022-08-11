"""
    Student Name: Limor Segal Shevah
    Assignment: No. 2
"""
# Ex. A
x = 3
y = 4
if x > y:
    print("BIG")
else:
    print("small")

# Ex. B
max_iterations = 5
for i in range(max_iterations):
    print(f"Iteration no. {i + 1}")

# Ex. C
z = 1
if 1 == z:
    print("summer")
elif 2 == z:
    print("winter")
elif 3 == z:
    print("fall")
else:
    print("spring")

# For me, another option with dictionary (ignore)
seasons_dict = {1: "summer", 2: "winter", 3: "fall", 4: "spring"}
num_of_seasons = 4


def get_season_by_num(season_num):
    if season_num in range(1, num_of_seasons + 1):
        print(seasons_dict[season_num])


get_season_by_num(3)

# Ex. D
# 1. 10 times the loop will run
# 2. 10 is the last number that will be printed

# Ex. E
shekels_dollar_currency = 3.46
personal_data_dict = {'age': 45, 'last_name_fl': 'S', 'flew_abroad': True, 'apartment_number': 1}
print(f"Current shekels-dollar currency: {shekels_dollar_currency}")
print(f"Age: {personal_data_dict['age']}")
print(f"Last name (first character): {personal_data_dict['last_name_fl']}")
print(f"Flew abroad: {personal_data_dict['flew_abroad']}")
print(f"Apartment number: {personal_data_dict['apartment_number']}")

print(personal_data_dict['age'] + shekels_dollar_currency)
# Result: 48.46

# Ex. F
# 1.
phone_number = "phone number"
data = input(f"Please enter your {phone_number}:")
# 2.
print(f"{phone_number} {data}")


def print_hello():  # Ex. G.1
    print("hello")


print_hello()


def calculate(a, b):  # Ex. G.2
    print(f"Result of add: {a + b}")


calculate(5, 3.2)


def get_name(name):  # Ex. H.1
    print(name)


get_name("Limor")


def divide_by_two(number):  # Ex. H.2
    print(number/2)


divide_by_two(10)
divide_by_two(11)


def get_sum(num1, num2):  # Ex. L.1
    return num1 + num2


res1 = get_sum(1, 3.5)
print(res1)


def concat_strings_with_char(str1, str2):  # Ex. L.2
    char = ' '
    return f"{str1}{char}{str2}"


res2 = concat_strings_with_char("shabbat", "shalom")
print(res2)


# Ex. K (Challenge)
def pyramid(size):
    for row in range(size):
        for col in range(row + 1):
            print('#', end='')
        print('\n')


pyramid(7)


# Ex. L  (Challenge)
def draw_x(size):
    hashtag = '#'
    for row in range(size):
        for col in range(size):
            if row == col:
                print(hashtag, end='')
            elif col == size-row-1:
                print(hashtag, end='')
            else:
                print(" ", end='')
        print('')


draw_x(7)


# Ex. M.1 + M.2
def get_number():
    return input("Please enter a number:")


def sum_number_digits(int_number):
    int_num_str = str(int_number)
    sum_digit = 0
    for digit_str in int_num_str:
        sum_digit += int(digit_str)
    return sum_digit


num = get_number()
sum_of_num_digits = sum_number_digits(num)
print(sum_of_num_digits)
