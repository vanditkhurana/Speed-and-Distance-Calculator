n=input("Enter your name : ")
s=input("Enter your Surname : ")
m1=float(input("Enter your physics marks : "))
m2=float(input("Enter your chemistry marks : "))
m3=float(input("Enter your maths marks : "))
av=((m1+m2+m3)/3)
f=open("marks.txt","a+")
f.write(n+" ; "+s+" ; "+str(m1)+" ; "+str(m2)+" ; "+str(m3)+" ; "+str(av))
f.close()