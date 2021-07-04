from tkinter import *

grams=1000
pounds=2.20462
ounces=35.274

def convert():
	print(ke_value)
	gt.delete('1.0', END)
	pt.delete('1.0', END)
	ot.delete('1.0', END)
	gt.insert(END, float(ke_value.get())*grams)
	pt.insert(END, float(ke_value.get())*pounds)
	ot.insert(END, float(ke_value.get())*ounces)

window = Tk()

kg=Label(window, text="Kg")
kg.grid(row=1, column=1)

ke_value=StringVar()
ke=Entry(window, textvariable=ke_value)
ke.grid(row=1, column=2)

b1=Button(window, text="Convert", command=convert)
b1.grid(row=1, column=3)

gt=Text(window, height=1, width=20)
gt.grid(row=2, column=1)

pt=Text(window, height=1, width=20)
pt.grid(row=2, column=2)

ot=Text(window, height=1, width=20)
ot.grid(row=2, column=3)

window.mainloop()
