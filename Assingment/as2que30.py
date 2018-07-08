from random import randint
def game():   
    f=open("sowpods.txt","r")
    s=f.read().split("\n")
    t=randint(0,len(s))
    w=s[t]
    print("Welcome to Hangman!")
    k=0
    l=['_' for i in range(len(w))]
    g=[]
    while(k!=1):
        print("\nyou have ",6-len(g)," incorrect guesses left")
        if(len(g)==6):
            print("\nyour chance has been over ,you loose: ")
            print("\n1.play again\n2.Exit")
            cs=int(input())
            if(cs==1):
                game()
            else:
                exit
        m=0
        for  i in l:
            print(i,end=' ')
        ch=input("Guess your letter: ")
        if ch not in g and ch not in w:
            g.append(ch)
        for i in range(len(w)):
            if ch==w[i]:
                l[i]=w[i]
                m=m+1
        if(m==0):
            print("\nIncorrect!")
        
        if(w==''.join(l)):
            print("\nyou won: \n the letter is: ",w)
            print("\n1.play again\n2.Exit")
            cs=int(input())
            if(cs==1):
                game()
            else:
                exit
            k=1

game()      
        