from tkinter import *

window=Tk()
window.title("Tkinter Learn Lesson")
window.minsize(width=600,height=600)

#label
my_label=Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack()

# my_label["text"]="new text"
# my_label.config(text="New Textt")

## Button

def button_clicked():
    my_label.config(text="Clicked Button")
    new_text=input.get()
    my_label.config(text=new_text)

button=Button(text="Click Me",command=button_clicked)
button.pack()

## Entry
input=Entry(width=50)
input.pack()
print(input.get())

## Text-Box
# text=Text(height=5,width=30)
# text.focus()
# # text.insert(END,string="placeholder")
# text.pack()


## Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10,width=20,command=spinbox_used)
spinbox.pack()

## Scale
def scale_used(value):
    print(value)
    
scale=Scale(from_=0,to=100,command=scale_used)
scale.pack()

## Check-Button
def checkButtonUsed():
    print(checked_state.get())
    
checked_state=IntVar()
checkButton=Checkbutton(text="Is On?",variable=checked_state,command=checkButtonUsed)
checked_state.get()
checkButton.pack()


## Radio Button
def radio_used():
    print(radio_state.get())
    
radio_state=IntVar()
radioButton1=Radiobutton(text="Option-1",value=1,variable=radio_state,command=radio_used)
radioButton2=Radiobutton(text="Option-2",value=2,variable=radio_state,command=radio_used)

radioButton1.pack()
radioButton2.pack()


## List Box
def listBoxUsed(event):
    print(listBox.get(listBox.curselection()))

listBox=Listbox(height=4)
fruits=["banana","apple","orange","pear"]

for item in fruits:
    listBox.insert(fruits.index(item),item)
listBox.bind("<<ListboxSelect>>",listBoxUsed)
listBox.pack()




##
window.mainloop()