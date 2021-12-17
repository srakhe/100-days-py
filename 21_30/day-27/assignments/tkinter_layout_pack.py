from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = my_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)
my_label.pack(side='left')

# Button
button = Button(text="Click Me", command=button_clicked)
button.pack(side='right')
new_button = Button(text="New Button")
new_button.pack(side='bottom')

# Entry
my_input = Entry(width=10)
print(my_input.get())
my_input.pack(side='top')

window.mainloop()
