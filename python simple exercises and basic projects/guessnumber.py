import random 
answer = random.randint(1 , 100)
guess = int (input ('choose between 1 to 100  :') )
while answer != guess :
    if answer > guess :
        print ('answer is more ! ')
    else :
        print (' answer is less !')
    guess = int (input (''))
print ('congrats !!') 