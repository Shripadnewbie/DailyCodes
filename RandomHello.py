print("Greetings User!")
perm1 = input("May I know your name?")
if perm1.upper() == 'YES':
    name1 = input("Enter your name : ")
else :
    print("Okay! I will Call you Stranger")
if perm1.capitalize() == 'Yes':
    print("It is Nice to meet you "+name1+ "!!!")
else :
    print("It is nice to meet you Stranger!!!")
age = input("Please enter your age : ")
print("You will be " + str(int(age)+1) + " years old, after a year")