#Sum of 10 numbers
S = 0
for i in range(0, 10):
    n = int(input())
    S = S + n
print(S)

#Sum of n numbers
N = int(input())
S = 0
for i in range(N):
    S = S + int(input())
print(S)

#Sum of n cubes:
n = int(input())
S = 0
for i in range(1, n +1):
    S = S + i**3
print(S)

#factorial
n = int(input())
f = 1
for i in range(1, n +1):
    f *= i
print(f)

#number of zeroes
counter = 0
for i in range(int(input())):
    if int(input()) == 0:
        counter += 1
print(counter)

#Ladder
n = int(input())
i=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
#Lost Card
n = int(input())
sum_cards = 0
for i in range(1, n + 1):
    sum_cards += i
# One can prove the following:
# sum_cards == n * (n + 1) // 2
# However, we'll calculate that using the loop.
for i in range(n - 1):
    sum_cards -= int(input())
print(sum_cards)
