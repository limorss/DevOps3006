'''
:parameter name
:return adsdasda
'''
def greet_name(name, exclude_name = "michael", greeting_word = "hello"):
    if name != exclude_name:
        print(f"{greeting_word} {name}")

greet_name("limor")
greet_name("moshe", "moshe")
greet_name("moshe", "limor", "good morning")

def multiply(x, y):
    """

    :param x:
    :type x:
    :param y:
    :type y:
    :return:
    :rtype:
    """
    result1 = x * y
    result2 = x / y
    return result1, result2

x = multiply(10, 4)

#user_name = input("enter your name: ")
#greet_name((user_name))

#user_age = int(input("enter your age: "))
r = multiply(4, 2)
print(r[0])
print(r[1])


