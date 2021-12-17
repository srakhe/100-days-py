from tkinter import *

window = Tk()
window.title('Miles and Kilometers Converter')
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)


def calc():
    if kms_entry.get():
        from_kms = int(kms_entry.get())
        to_miles = from_kms * 0.62137119
        miles_entry.insert(0, string=str(round(to_miles, 4)))
    elif miles_entry.get():
        from_miles = int(miles_entry.get())
        to_kms = from_miles * 1.609344
        kms_entry.insert(0, string=str(round(to_kms, 4)))


def clear():
    miles_entry.delete(0, END)
    kms_entry.delete(0, END)


title = Label(text='Leave the one to find blank and input the other:')
title.grid(row=0, column=1)
title.config(padx=10, pady=10)

label_kms = Label(text='Kms')
label_kms.grid(row=1, column=2)
label_kms.config(padx=10, pady=10)
kms_entry = Entry(width=10)
kms_entry.grid(row=1, column=1)

label_miles = Label(text='Miles')
label_miles.grid(row=2, column=2)
label_miles.config(padx=10, pady=10)
miles_entry = Entry(width=10)
miles_entry.grid(row=2, column=1)

submit_btn = Button(text='Calculate', command=calc)
submit_btn.grid(row=3, column=2)
submit_btn.config(padx=10, pady=10)

clear_btn = Button(text='Clear', command=clear)
clear_btn.grid(row=3, column=1)
clear_btn.config(padx=10, pady=10)

window.mainloop()
