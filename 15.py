#a = int(input("enter number: "))
#b = int(input("enter number: "))
#result = a / b
#print(result)


import requests
print("moshe")
try:
    #response = requests.get("htgf://github.com")
    f = int(input("enter number: "))
    r = 5 / 0
except ZeroDivisionError:
    print("Could not divide by zero")
except ValueError:
    print("Enter a legal number")
except Exception as e:
    print("something went wrong, her is more")
    print(e.args)

print("haim")
