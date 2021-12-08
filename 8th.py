from collections import Counter
dict1 = eval(input("Enter Dictionary 1"))
dict2 = eval(input("Enter Dictionary 2"))
d = Counter(dict1) + Counter(dict2)
print(d)
