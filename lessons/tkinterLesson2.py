from tkinter import *

window=Tk()
window.title("Tkinter Learn Lesson")
window.minsize(width=600,height=600)
window.config(padx=20,pady=20,bg="gray")
window.config

## Label
my_label=Label(text="I am a label",font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)
# my_label.place(x=0,y=0)


## Button
def button_clicked():
    my_label.config(text="Clicked Button")
    new_text=input.get()
    my_label.config(text=new_text)

button=Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)


## New Button
new_button=Button(text="New Button")
new_button.grid(column=2,row=0)

input=Entry()
input.grid(column=3,row=2)




##
mainloop()