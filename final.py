import matplotlib.pyplot as plt 
import numpy as np
import math
from tkinter import *
from tkinter import messagebox

root=Tk()

superscripts="⁰¹²³⁴⁵⁶⁷⁸⁹"

labels=[]

def create_cart_plane(lim=6,title="Cartesian plane"):
    '''Creates cartesian plane'''
    plt.title(title)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    x_y=[]
    for i in range(lim*2+1):
        x_y.append(0)
    y_y=np.arange(-1*lim,lim+1,1)
    plt.plot(x_y,y_y,"k",marker="_",linewidth=0.2)#y-axis
    x_x=y_y
    y_x=x_y
    plt.plot(x_x,y_x,"k",marker="|",linewidth=0.2) #x-axis

    #Arrows at end of axes
    plt.arrow(0,0,lim,0,head_width=0.3,color="k")
    plt.arrow(0,0,-1*lim,0,head_width=0.3,color="k")
    plt.arrow(0,0,0,lim,head_width=0.3,color="k")
    plt.arrow(0,0,0,-1*lim,head_width=0.3,color="k")

    #Grid
    for i in range(-1*lim,lim+1):
        a=[]
        b=[]
        for j in range(2*lim+1):
            a.append(i) #plotting x=a where a is in limit
        for k in range(-1*lim,lim+1):
            b.append(k) #plotting y=a where a is in limit
        plt.plot(a,b,"k",linewidth=0.15)
        plt.plot(b,a,"k",linewidth=0.15)

selection=0

def plot():
    '''Plots graph'''
    global selection
    global i
    i=-1
    if selection==1:
        create_cart_plane(10,"Taylor series")
        x=np.arange(-3*np.pi,3*np.pi,0.1)
        y=(np.sin(x))
        plt.plot(x,y,label="y=sin(x)")
    elif selection==2:
        create_cart_plane(10,"Taylor series")
        x=np.arange(-3*np.pi,3*np.pi,0.1)
        y=(np.cos(x))
        plt.plot(x,y,label="y=cos(x)")
    elif selection==3:
        create_cart_plane(15,"Taylor series")
        x=np.arange(-10,2.8,0.1)
        y=(np.e)**x
        plt.plot(x,y,label="y=e^x")
    elif selection==4:
        create_cart_plane(10,"Taylor series")
        x=np.arange(-1,9,0.1)
        y=(np.log(1+x))
        plt.plot(x,y,label="y=ln(1+x)")
    plt.legend()
    plt.show()

global temp
temp=[2]

def make_series():
    '''Makes next term of series'''
    global temp
    global i
    global stuff
    i+=1
    if i>=len(stuff):
        messagebox.showwarning("Warning","You have crossed the amount of terms")
        return
    if i>=1:
        graph=temp.pop(0)
        graph.remove()
    def expression(x,ind):
        global label
        label='y='
        s=0
        for j in range(ind+1):
            s+=eval(stuff[j])
            label+=showing[j]
        return s        
    if selection==1:
        x=np.arange(-4.5,4.5,0.01)
        y=expression(x,i)
    elif selection==2:
        x=np.arange(-4.5,4.5,0.01)
        y=expression(x,i)
    elif selection==3:
        x=np.arange(-5,2,0.01)
        y=expression(x,i)
    elif selection==4:
        x=np.arange(-1.5,2,0.01)
        y=expression(x,i)
    temp=plt.plot(x,y,label=label)
    plt.legend()

    plt.show()

def select():
    '''Decides which function based on radio-button input'''
    global selection
    global stuff
    global showing
    selection=var.get()
    if selection==1:
        stuff=['x','-x**3/math.factorial(3)','+x**5/math.factorial(5)','-x**7/math.factorial(7)','x**9/math.factorial(9)','-x**11/math.factorial(11)']
        showing=['x','-x³/3!','+x⁵/5!','-x⁷/7!','+x⁹/9!','-x¹¹/11!']
    elif selection==2:
        stuff=['x**0','-x**2/math.factorial(2)','+x**4/math.factorial(4)','-x**6/math.factorial(6)','x**8/math.factorial(8)','-x**10/math.factorial(10)']
        showing=['1','-x²/2!','+x⁴/4!','-x⁶/6!','+x⁸/8!','-x¹⁰/10!']
    elif selection==3:
        stuff=['x**0','x**1','+x**2/math.factorial(2)','x**3/math.factorial(3)','x**4/math.factorial(4)','x**5/math.factorial(5)']
        showing=['1','+x','+x²/2!','+x³/3!','+x⁴/4!','+x⁵/5!']
    elif selection==4:
        stuff=['x','-x**2/2','x**3/3','-x**4/4','x**5/5','-x**6/6']
        showing=['x','-x²/2','+x³/3','-x⁴/4','+x⁵/5','-x⁶/6']

canvas=Canvas(root,width=552,height=312)
canvas.pack()
img=PhotoImage(file="yes.ppm")
canvas.create_image(20,20,anchor=NW, image=img)

var=IntVar()
rad1=Radiobutton(root, text="sin(x)", variable=var,value=1, command=select)
rad2=Radiobutton(root, text="cos(x)", variable=var,value=2, command=select)
rad3=Radiobutton(root, text="e^x", variable=var, value=3, command=select)
rad4=Radiobutton(root, text="ln(1+x)", variable=var, value=4, command=select)
rad1.pack()
rad2.pack()
rad3.pack()
rad4.pack()

button=Button(root,text="plot",command=plot)
button.pack()
i=-1
button2=Button(root,text="next term",command=make_series)
button2.pack()


root.mainloop()
