file=input("Enter your file name : ")
F=open(file,"r")
line=F.readlines()
line=line[1:]
Time=[]
i=0
#time=0
for l in line:
    L=l.split(";")
    Time.append(int(L[4]))
F.close()
#for i in range(len(Time)-1):
#    time=time+(Time[i+1]-Time[i])
#    i=i+1
time=int(Time[-1]-Time[0])
time=int(time*(10**(-3)))
h=time//3600
v=time%3600
m=v//60
s=v%60
if h!=0:
    print(h,"hr(s) ",m,"min(s) ",s,"s")
else:
    print(m,"min(s) ",s,"s")