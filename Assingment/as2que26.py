def player1():
    print("player 1: enter row and coloumn")
    r=int(input())
    c=int(input())
    return r-1,c-1

def player2():
     print("player 2: enter row and column")
     r=int(input())
     c=int(input())
     return r-1,c-1
    


l=[]
#p=[]
for i in range(3):
    l1=[]
    p1=[]
    for j in range(3):
        l1.append(0)
        #p1.append(j+1)
    l.append(l1)
    #p.append(p1)
print("who want to start first: \n1.player 1\n2.player 2")
ch=int(input())
if ch==1:
    if(input("press any key to start the game...")):
        k=0
        while(k!=1):
            for i in l:
                print(i)
            m=0
            while(m!=1):
                r1,c1=player1()
                if l[r1][c1]=='O':
                    print("player 2 have entered here, please enter again: ")
                elif l[r1][c1]=='X':
                    print("you yourself entered here, please enter again: ")
                else:
                    l[r1][c1]='X'
                    m=1
            m=0
            while(m!=1):
                r2,c2=player2()
                if l[r2][c2]=='X':
                    print("player 1 have entered here, please enter again: ")
                    
                elif l[r2][c2]=='O':
                    print("you yourself have entered here, please enter again: ")
                else:
                    l[r2][c2]='O'
                    m=1
            #comparing through rows
            for i in l:
                #for player 1
                c=0
                for j in range(len(i)):
                    if(i[j]=='X'):
                        c=c+1
                    if(c==3):
                        print("palyer 1 has won: ")
                        for g in l:
                            print(g)
                            k=1
                        break
                if(k==1):
                    break
                #for player 2
                c=0
                for j in range(len(i)):
                    if(i[j]=='O'):
                        c=c+1
                    if(c==3):
                        print("palyer 2 has won: ")
                        for g in l:
                            print(g)
                            k=1
                        break
                if(k==1):
                    break
                
            #comparing through column
            for i in range(3):
                #player 1
                c=0
                for j in range(3):
                    if l[j][i]=='X':
                        c=c+1
                        
                    if(c==3):
                        print("palyer 1 has won: ")
                        for g in l:
                            print(g)
                            k=1
                        break
                if(k==1):
                     break
                #player 2
                c=0
                for j in range(3):
                    if l[j][i]=='O':
                        c=c+1
                        
                    if(c==3):
                        print("palyer 2 has won: ")
                        for g in l:
                            print(g)
                            k=1
                        break
                if(k==1):
                    break
            #comparing through daigonal
            c=0
            i=0
            j=0
            #for player 1
            for g in range(3):
                if(l[i][j]=='X'):
                    c=c+1
                i=i+1
                j=j+1
            if(c==3):
                print("palyer 1 has won: ")
                for g in l:
                    print(g)
                    k=1
                    
            c=0
            i=0
            j=0
            # for player 2
            for g in range(3):
                if(l[i][j]=='O'):
                    c=c+1
                i=i+1
                j=j+1
            if(c==3):
                print("palyer 2 has won: ")
                for g in l:
                    print(g)
                    k=1
        
                
                 
                             
                             
                         
                
                
                    
                        
                
            
            
        
        
    