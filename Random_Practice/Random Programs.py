#Translator
sent = input('Enter your sentence : ')
translation = ''
for let in sent:
    if let.lower() in "aeiou":
        if let.isupper():
            translation = translation + 'G'
        else :
            translation = translation + 'g'
    else:
        translation = translation + let
print(translation)