from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("350x350")
#root.resizable(0,0)
menubar=Menu(root)
file=Menu(menubar,tearoff=0)
file.add_command(label="Programmer")
file.add_command(label="Scientifc")
file.add_command(label="Progaramer")
file.add_separator()
file.add_command(label="Convertor")
menubar.add_cascade(label="Standard ~ ",font=('Arial','20','bold'),menu=file,underline=70)
root.config(menu=menubar)

e2=Entry(text="",font=('Arial','20',"bold"),bg="skyblue",width=1)
e2.grid(columnspan=4,ipadx=150)
def btn1():
    e2.delete(0,END)
def btn2():
    n=len(e2.get())
    e2.delete(n-1,END)
def btn3():
    global a
    a = e2.get()
    a = a + "%"
    e2.delete(0, END)
def btn4():
    global a
    a = e2.get()
    a = a + "/"
    e2.delete(0, END)
def btn5():
    z=b5['text']
    e2.insert(END,z)
def btn6():
    b=b6['text']
    e2.insert(END,b)
def btn7():
    c=b7['text']
    e2.insert(END,c)
def btn8():
    global a
    a = e2.get()
    a = a + "*"
    e2.delete(0, END)
def btn9():
    e=b9['text']
    e2.insert(END,e)
def btn10():
    f=b10['text']
    e2.insert(END,f)
def btn11():
    g=b11['text']
    e2.insert(END,g)
def btn12():
    global a
    a = e2.get()
    a = a + "-"
    e2.delete(0, END)

def btn13():
    i=b13['text']
    e2.insert(END,i)
def btn14():
    j=b14['text']
    e2.insert(END,j)
def btn15():
    k=b15['text']
    e2.insert(END,k)

def btn16():
    global a
    a=e2.get()
    a=a+"+"
    e2.delete(0,END)
def btn17():
    m=b17['text']
    e2.insert(END,m)
def btn18():
    n=b18['text']
    e2.insert(END,n)
def btn19():
    o=b19['text']
    e2.insert(END,o)
def btn20():
    global a
    s=eval(a+e2.get())
    e2.delete(0,END)
    e2.insert(0,s)


b1=Button(text="Clear",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn1)
b1.grid(column=0,row=1)
b2=Button(text="X",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn2)
b2.grid(column=1,row=1)
b3=Button(text="%",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn3)
b3.grid(column=2,row=1)
b4=Button(text="/",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn4)
b4.grid(column=3,row=1)
b5=Button(text="7",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn5)
b5.grid(column=0,row=2)
b6=Button(text="8",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn6)
b6.grid(column=1,row=2)
b7=Button(text="9",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn7)
b7.grid(column=2,row=2)
b8=Button(text="*",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn8)
b8.grid(column=3,row=2)
b9=Button(text="4",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn9)
b9.grid(column=0,row=3)
b10=Button(text="5",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn10)
b10.grid(column=1,row=3)
b11=Button(text="6",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn11)
b11.grid(column=2,row=3)
b12=Button(text="-",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn12)
b12.grid(column=3,row=3)
b13=Button(text="1",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn13)
b13.grid(column=0,row=4)
b14=Button(text="2",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn14)
b14.grid(column=1,row=4)
b15=Button(text="3",font=('Arial','15',"bold"),bg="black",
fg="white",height=1,width=5,command=btn15)
b15.grid(column=2,row=4)
b16=Button(text="+",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn16)
b16.grid(column=3,row=4)
b17=Button(text=":",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn17)
b17.grid(column=0,row=5)
b18=Button(text="0",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn18)
b18.grid(column=1,row=5)
b19=Button(text=".",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn19)
b19.grid(column=2,row=5)
b20=Button(text="=",font=('Arial','15',"bold"),bg="black",fg="white",height=1,width=5,command=btn20)
b20.grid(column=3,row=5)
root.mainloop()