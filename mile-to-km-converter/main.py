from tkinter import *

FONT=("Arial",24,"normal")

window=Tk()
window.title("Mile to KM Converter")
# window.minsize(width=500,height=500)
window.config(padx=50,pady=50)


def milesToKm():
    miles=float(miles_value.get())
    km=round(miles*1.609)
    kilometer_result_label.config(text=f"{km}")



## Label
miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)


## create input miles
miles_value=Entry()
miles_value.grid(column=1,row=0)

## New Label
is_equal_to=Label(text="is equal to")
is_equal_to.grid(column=0,row=1)


## Kilometer
kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=1,row=1)

## Kilometer Label
kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)

## Calculate Button
calculate_button=Button(text="Calculate",command=milesToKm)
calculate_button.grid(column=1,row=2)










##
window.mainloop()