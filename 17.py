from aritmetics import addition, sub
from get_data import get_number

import datetime
from time import sleep

def dec(function_to_run):
    def wrapper():
        print(datetime.datetime.now())
        print("moshe!")
        function_to_run()
        print(datetime.datetime.now())
    return wrapper

def logger_dec(function_to_run):
    def wrapper(*args, **kwargs):
        print_format_str = None
        for key, val in kwargs.items():
            print_format_str = print(f"Key: {str(key)}, Value: {val}")
        print("-------------------------------------------------------------------")
        print(f"{datetime.datetime.now()}, Start function: {function_to_run.__name__}\nParameters: {args}\n{print_format_str}")
        ret_value = function_to_run(*args, **kwargs)
        print(f"{datetime.datetime.now()}, Ended function: {function_to_run.__name__}, Return value: {ret_value}")
        print("-------------------------------------------------------------------")
    return wrapper



@dec
def print_something():
    print("something")

@dec
def print_another():
    print("in print another function")

#print_something()

@logger_dec
def duplicate_word(word):
    return word*2


@logger_dec
def add_words(word1, word2):
    return word1 + word2

#print_another()

def dict_swapper(function_name):
    def wrapper(my_dict):
        new_dict = {}
        for k, v in my_dict.items:
            new_dict[v] = k
        function_name(new_dict)
    return wrapper

duplicate_word("boker")
add_words("hello", "world")
my_args = {"first": "limor", "last": "shevah"}














