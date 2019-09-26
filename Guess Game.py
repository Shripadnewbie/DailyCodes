secretWord = 'Mello'
guess = ''
counter = 0
left = 3
while guess != secretWord and left != 0:
    guess = input('Enter your guess below '+ "You have "+ str(left) + " number of guesses left\n :")
    counter = counter+1
    left = left -1
if counter == 3 and guess != secretWord:
    print('Out of guesses.You Lose!!')
elif counter <= 3 and guess == secretWord:
    print('You win')

#Print Pattern
a = input()
for i in range(len(a)+1):
    print(a[:i])