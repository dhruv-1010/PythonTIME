import random
import time
def choices(choice):
    if choice =='1':
        for i in range(3):
            if choice == '1':
                print("Enter any number but [i am never zero] !!!!!")
                a = int(input())
                print(a)
                collatz(a)
            if(i==1):
                print("Hmm getting out of tries ,, last one!!!")
            i=i+1
    else :
        print("HaHa you thought you or your gods can defeat me  I am Inevitable  !!!")
        print("""(Sorry all the thing is this was just to teach you that sometimes googling thing helps!!! )
            query google about Collatz Sequence...""")
    
def collatz(a):
    while(a!=1):

        if(a%2==0):
            if(a == 4 or a== 2):
                print("we are getting closer!!!!")
            else:
                print("haha even")
            time.sleep(1)
            print()
            print(a//2)
            a = a//2
        else:
            print("HMM odd")
            time.sleep(.1)
            print()
            print(3*a+1)
            a = 3*a+1
    print("No matter how hard you try i am inevitable i am ONE!!!1")
def main():
    print('''hmm !!!! so you defeated bagels now its my turn 
        the infinite ONE above all the Collatzzzz the knight of darkness the inevitable 'One',,
        can you stop me 
        (so the goal above is to guess a number which you think can stop thim or just randomly choose any one !!)''' )
    choice  = input('''Enter choice
                        1 -->Choose to bear the burden yourself!!the hard way
                        2 -->Let me out!!fools way
                        ''')
    choices(choice)    

if __name__=='__main__':
    main()    
