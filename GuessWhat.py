from random import randint
x=()
y=()
z=()
x=randint(1,101)
y=int(input('You are about to begin a guessing-game.\nYou need to guess a number with the lowest number of guesses.\nI will give you a hint after your each guess.\nThe number was randomly picked from interval (1,100).\nPlease make your first guess with a number from 1 to 100: '))
i=1

while y < 1 or y > 100:
    y=int(input('OUT OF BOUNDS. Make a guess with a number from 1 to 100: '))
else:
    if x==y:
        print (f'Correct! It took you {i} guess to succeed.')
        print ('Thanks for playing.')
    elif y>=(x-10) and y<=(x+10):
        print ('WARM')
    else:
        print ('COLD')          

z=abs(x-y)
        
while x!=y:
    i+=1
    y=int(input('Make another guess: '))
    if y < 1 or y > 100:
        print('OUT OF BOUNDS.')
    elif z>abs(x-y):
        print('WARMER.')
    elif z<=abs(x-y):
        print('COLDER.')
    z=abs(x-y)
    
else:
    if i==1:
        pass
    else:
        print(f'Correct! It took you {i} guesses to succeed')
        print ('Thanks for playing.')