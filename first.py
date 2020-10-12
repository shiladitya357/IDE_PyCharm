# interpreted language
# dynamic, typed

i1 = [1, 2, 3, 4]

i2 = (1, 2, 3, 4)

i3 = {"John": 123, "Merry": 456}
print(i3, type(i3))

data = """line 1
line 2
line 3
"""

print(data)

# {} can be used in a sentence to replace with variables, in the order of their appearance

counter = 0
while counter < 3:
    print("Square of {} : {}".format(counter, counter ** 2))
    counter += 1

for i in range(4):
    print("i before : ", i)

for i in range(1, 11, 2):
    print("i after : ", i)


# defining a function
def add(a, b):
    # Optional documentation below
    """
    :param a:
    :param b:
    :return: sum of a and b
    """

    result = a + b
    print("{} + {} = {}".format(a, b, result))
    return a + b


add(10, 25)

# for doing function overloading we can either use a default argument for the function like add(a,b,c=10)

#now for multiple arguments

def joinStr(*args):
    print("No of arguments is ",len(args))
    result=" ".join(args)
    print(result)

joinStr("Hello","bhai","kaise ho?")