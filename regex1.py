import re

pattern = r'm\w\w'
data = "cat mat bat rat mam book"
# option 1 first compile and then do operation


regexObj = re.compile(pattern)
matchObj = regexObj.match(data)

if matchObj:
    print("String starts with m",matchObj.group())
else:
    print("String doesn't start with m")

# option2 Straight away do the operation

matchObj = re.match(pattern,data)
print(matchObj)

# search
matchObj = re.search(pattern,data)
print(matchObj)
# findall
matchObj = re.findall(pattern,data)
print(matchObj)
# split
matchObj = re.split(pattern,data)
print(matchObj)

# substitute
# matchObj = re.sub(pattern,data)
# print(matchObj)
