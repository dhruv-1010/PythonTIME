import random
# checks the number is correct and gives randomly generated anweser
def checker(guess,secretN):
    if(guess == secretN):
        return 'Your Answer is correct!!! Keep it up!!!!'#important thing to not after function returned 
        # following code is executed.
    clue = []
    for i in range(3):
        if guess[i] == secretN[i] :
            clue.append('Fermi')
        elif guess[i] in secretN :
            clue.append('Pico')
    
    if len(clue) == 0 :
        return 'Bagels'
    else : 
        clue.sort()
        return ' '.join(clue)
# generates that dark hidden spell
def generator():
    number = list('0123456789')
    random.shuffle(number)
    # awesome jsut awesome maybe i should learn the random module now
    secretN=''
    for i in range(3):
        secretN+=str(number[i])
    return secretN
# guess = list('013')
# secretN = generator()
# print(checker(guess, secretN))

def main():
    while True:
        secretN = generator()
        print("Ah mmmm yes the spell so dark so delicious but can you guess it !!!! think think guess guess think think guess guess")
        print("OK your turn now!show you wit")
        for i in range(11):
            guess = ''
            while len(guess)!=3 or not guess.isdecimal():
                print("your %d chance"%i)
                guess = input('> ')
            clues = checker(guess, secretN)
            print(clues)
            if guess == secretN:
                break # They're correct, so break out of this loop.
        # code copied below rest is handwritten i did a good job although but best if i could have made it myself 
        #  yet i loved it .........
 # Ask player if they want to play again.
        print("AH shoot the spell was ",secretN)
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
# at least i learned something new that was awesome
# __name__ = '__main__'  method is uesful if you want to run your large and bulky program instead of directly importing some of its modules it

if __name__=='__main__':
    print('''WELCOME MY FELLOW LORDS........TO THE KINGDOM OF...
    """"  BAGELS   """""    where lies the mystic valleys of death and life alone the 
    power of god himself
    !!!!!What you want to Enter????
    My fellow child to pass you must break the enchanted spells of
    Darkness !!!
    Guess it,Guess a three digit spell to break the darkness and provide 
        you the riches!!!!!!you dont have much time think think guess guess think think guess guess
    OK ... for your help following hints in response to your guess:
    “Pico” when your guess has a correct digit in the
            wrong place, 
    “Fermi” when your guess has a correct
            digit in the correct place, 
    and “Bagels” if your guess
            has no correct digits. 
    You have 10 tries to guess the secret number.''')    
    main()













