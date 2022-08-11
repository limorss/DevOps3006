"""
    Student Name: Limor Segal Shevah
    Assignment: No. 3
"""
# Ex. 1 + 2
try:
    a = 1/0;
except ZeroDivisionError:
    print(f"Zero division error occurred!")
except BaseException as e:
    print(f"Base Exception occurred, see more details here: {e.args}")


# Ex. 3 Code is valid can be with try & finally
try:
    x = 1
finally:
    print("finally")

# Ex. 4 All exception types can be caught with Except:

# Ex. 5 We do not have specific error handling, it is too general and bad coding. With specific exception we can also
# act differently if we need (exit program, display warning, other) and supply more information.

# Ex. 6
# except IOError - It is an error raised when an input/output operation fails,
#                  such as the print statement or the open() function when trying to open a file that does not exist.
#                  It is also raised for operating system-related errors.
# except ZeroDivisionError - Handle dividing  a number in zero error

# Ex. 7 + 8
file = open("words.txt", 'w')
file.write("limor")
file.close()

# Ex. 9
file = open("words.txt", 'r')
print(file.read())
file.close()

# Ex. 10
file = open("words.txt", 'r+', encoding="utf8")
file.write("תרגילי בית מספר 31")
file.seek(0)
print(file.read())
file.close()

# Ex. 11
from PIL import Image, ImageDraw
my_image = Image.new('RGB', (200, 300), (201, 9, 188))
draw = ImageDraw.Draw(my_image)
draw.rectangle((500, 100, 300, 500), fill=(40, 31, 40), outline=(255, 255, 255))
my_image.save('my_image.png')