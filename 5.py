is_true = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
print(type(a == b))
if a < b and (b != 1 or not strThree == "moshe"):
    print("a is smaller than b")
elif a == b:
    print("a equals b")
elif b > 1:
    print("blabla")
else:
    print("something")
names = ["chanan", "tom", "zack","aharon"]

other_list = []
name_to_find = "ariel"
if name_to_find in names:
    print(f"we found {name_to_find}")
else:
    print(f"we did not find {name_to_find}")

if other_list:
    print("other list has values")

if len(other_list) > 0:
    print("other list has values")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
if type (k) is int:
    print("i like numbers")
elif type(k) is str:
    print("I like strings")
print(k == f)
print(k is f)
print(t == e)
print(t is e)
t = (1, 2, 3)
e = (1, 2, 3)
print(t is e)


