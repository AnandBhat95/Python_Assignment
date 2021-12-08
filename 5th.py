list1=eval(input("Enter list of cities"))
list2=[]
for state1 in list1:
    str1 = "How is the weather in "+state1
    list2.append(str1) 
    for state2 in list1:
        if state1 != state2:
            str = "How far is "+state1+" from "+state2
            list2.append(str)
            
print(list2)
