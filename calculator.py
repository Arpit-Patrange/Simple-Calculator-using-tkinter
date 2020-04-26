from tkinter import *
root =Tk()
root.title("Simple calculator")

e=Entry(root,width=40,borderwidth=2)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def link_button(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear_button():
    e.delete(0,END)

def add_button():
    first_number =e.get()
    global f_num
    global  math
    math = "addition"
    f_num=int(first_number)
    e.delete(0,END)

def multiplication_button():
    first_number =e.get()
    global f_num
    global  math
    math = "multiplication"
    f_num=int(first_number)
    e.delete(0,END)

def substraction_button():
    first_number =e.get()
    global f_num
    global  math
    math = "substraction"
    f_num=int(first_number)
    e.delete(0,END)

def division_button():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def equals_button():
    second_number=e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "substraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))





button_1=Button(root,text="1",padx=40,pady=20, command=lambda:link_button(1))
button_2=Button(root,text="2",padx=40,pady=20, command=lambda:link_button(2))
button_3=Button(root,text="3",padx=40,pady=20, command=lambda:link_button(3))
button_4=Button(root,text="4",padx=40,pady=20, command=lambda:link_button(4))
button_5=Button(root,text="5",padx=40,pady=20, command=lambda:link_button(5))
button_6=Button(root,text="6",padx=40,pady=20, command=lambda:link_button(6))
button_7=Button(root,text="7",padx=40,pady=20, command=lambda:link_button(7))
button_8=Button(root,text="8",padx=40,pady=20, command=lambda:link_button(8))
button_9=Button(root,text="9",padx=40,pady=20, command=lambda:link_button(9))
button_0=Button(root,text="0",padx=40,pady=20, command=lambda:link_button(0))
button_equals=Button(root,text="=",padx=50,pady=20, command=equals_button)
button_clear=Button(root,text="clear",padx=70,pady=20, command=clear_button)
button_add=Button(root,text="+",padx=40,pady=50, command=add_button)
button_substraction=Button(root,text="-",padx=40,pady=20, command=substraction_button)
button_multiplication=Button(root,text="*",padx=40,pady=20, command=multiplication_button)
button_division=Button(root,text="/",padx=40,pady=20, command=division_button)


button_1.grid(row= 3,column= 2)
button_2.grid(row= 3,column= 1)
button_3.grid(row= 3,column= 0)

button_4.grid(row= 2,column= 2)
button_5.grid(row= 2,column= 1)
button_6.grid(row= 2,column= 0)

button_7.grid(row= 1,column= 2)
button_8.grid(row= 1,column= 1)
button_9.grid(row= 1,column= 0)

button_0.grid(row=4 ,column= 0)
button_equals.grid(row= 4,column=1 )
button_clear.grid(row= 5,column=0 ,columnspan=2)
button_add.grid(row= 4,column= 2,rowspan=2)

button_substraction.grid(row= 6,column= 2)
button_multiplication.grid(row= 6,column= 1)
button_division.grid(row= 6,column= 0)




root.mainloop()