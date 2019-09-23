#Minimum of given numbers
values = input("Enter two numbers separated by either by a space or a comma : ")
if values[str.find(values,',')] == ',':
    list = map(int,values.split(","))
elif values[str.find(values,' ')] == ' ':
    list = map(int,values.split(" "))
print(min(list))

