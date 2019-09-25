#List of Squares
N=int(input())
i=1
while i**2 <= N:
    print(i**2)
    i=i+1


#Least Divisor
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

#power of two
N = int(input())
i=0
p=1
while p * 2 <= N:
    i = i + 1
    p = p * 2
print(i, p)

#jogger
G = float(input('Enter your Goal : '))
i=1
x=float(input("Enter your first day distance : "))
while x < G:
    x = x * 1.1
    i= i+1
print(i)

#Sequence
i=0
while int(input()) != 0:
    i=i+1
print(i)