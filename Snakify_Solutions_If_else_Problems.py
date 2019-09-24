#Sign function
inp = int(input("Enter the number to test : "))
if inp > 0:
    print(1)
elif inp == 0:
    print(0)
else :
    print(-1)
#Three numbers
num1 = int(input())
num2 = int(input())
num3 = int(input())
list=[num1,num2,num3]
print(min(list))
#Equal numbers
num1 = input()
num2 = input()
num3 = input()
if num1.count()>1:
    print(num1)
elif num2.count()>1:
    print(num2)
elif num3.count()>1:
    print(num3)

#rook move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
#Same color chess board
h1 = int(input())
w1 = int(input())
h2 = int(input())
w2 = int(input())

def is_same_colour(h1, w1, h2, w2):
    if (h1 + w1+h2 + w2) % 2 == 0):
        print('YES')
    else:
        print('NO')

is_same_colour(h1, w1, h2, w2)


#King move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x = if x1 -x2 > 0:
        print(x1 - x2)
    elif x1 - x2 < 0:
        print(x2-x1)
#Bishop move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1-x2)==abs(y1-y2):
    print("YES")
else: print("NO")

#Knight Move
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if abs(x1 - x2) == 2 * abs(y1 - y2) or 2 * abs(x1 - x2) == abs(y1 - y2):
        print("YES")
    else:
        print("NO")
#Chocolate bar
    n = int(input())
    m = int(input())
    k = int(input())
    if k <= n * m and (k % n == 0 or k % m == 0):
        print('YES')
    else:
        print('NO')
#Leap_year_Problem
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('LEAP')
    else:
        print('COMMON')
