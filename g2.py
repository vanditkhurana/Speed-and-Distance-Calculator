from tkinter import *
from tkinter.ttk import Combobox
from math import *
import os
def csv1():
    Lcsv=[]
    f=os.path.abspath('.')
    L=os.listdir(f)
    for e in L:
        if('.csv' in e):
            Lcsv.append(e)
    return Lcsv
def calculate():
    file=s1.get()
    F=open(file,'r')
    line = F.readlines()
    line = line[1:]
    Lat=[]
    Lon=[]
    Time=[]
    for l in line:
        if(file=="gps1.csv"):
            L=l.split(";")
        else:
            L=l.split(",")
        Lat.append(float(L[0]))
        Lon.append(float(L[1]))
        Time.append(float(L[-1]))
    F.close()    
    calculate2(Lat,Lon,Time)
def calculate2(Lat,Lon,Time):
    i=0
    dis=0
    time=0
    speed=0
    a=len(Lat)-1
    for i in range(a):
        la1=float(Lat[i]*0.0174533)
        lo1=float(Lon[i]*0.0174533)
        la2=float(Lat[i+1]*0.0174533)
        lo2=float(Lon[i+1]*0.0174533)
        r=6371000
        y=float(la2-la1)
        x=float(lo2-lo1)*cos((la1+la2)/2)
        d=float(sqrt(pow(x,2)+pow(y,2))*r)
        dis=(dis+d)
        t=Time[i+1]-Time[i]
        t=t*(10**(-3))
        time=int(time+t)
        i=i+1
    sp=dis/time
    h=time//3600
    v=time%3600
    m=v//60
    s=v%60
    st2=str(h)+"hr(s) "+str(m)+"min(s) "+str(s)+"s"
    st1=str(round(dis,3))+"m"
    st3=str(round(sp,3))+"m/s"
    v1.set(str(st1))
    v2.set(str(st2))
    v3.set(str(st3))
window=Tk()
window.title("Distance")
l1=Label(window,text="Filename : ")
l1.grid(row=0,column=0)
s1=Combobox(window,values=csv1())
s1.grid(row=0,column=1)
l2=Label(window,text="Distance : ")
l2.grid(row=1,column=0)
v1=StringVar()
l3=Label(window,textvariable=v1,bg="beige")
l3.grid(row=1,column=1)
l4=Label(window,text="Time : ")
l4.grid(row=2,column=0)
v2=StringVar()
l5=Label(window,textvariable=v2,bg="beige")
l5.grid(row=2,column=1)
l6=Label(window,text="Speed : ")
l6.grid(row=3,column=0)
v3=StringVar()
l7=Label(window,textvariable=v3,bg="beige")
l7.grid(row=3,column=1)
#l8=Label(window,text="m")
#l8.grid(row=1,column=2)
#l10=Label(window,text="m/s")
#l10.grid(row=3,column=2)
b1=Button(window,text="Quit",command=quit)
b1.grid(row=4,column=0)
b2=Button(window,text="Calculate",command=calculate)
b2.grid(row=4,column=2)
window.mainloop()