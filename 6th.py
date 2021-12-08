a = eval(input("Enter list of dictionaries"))

b = {x['name']:x for x in a}.values()


print(b)
