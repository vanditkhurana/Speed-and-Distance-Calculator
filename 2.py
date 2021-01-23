y=1
r="y"
while(r=="y"):
    x=int(input("Enter a number"))
    if(x>1 and x<=10):

        print("             *******----------********")
        print("                   Table of ",x)
        print("             *******----------********")
        #while(y<=10):
        #    print("                 ",x," * ",y," = ",x*y)
        #    y=y+1
        #print("             *******----------********")
        for y in range(1,11):
            print("                 ",x," * ",y," = ",x*y)
            y=y+1
        print("             *******----------********")
        y=0
    else:
        print("Out of Range")
    r=input("Wanna Continue?(y/n)")
    if(r=="n"):
        print("Goodbye")