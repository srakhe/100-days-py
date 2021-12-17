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
my_label.place(x=250, y=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.place(x=0, y=150)
new_button = Button(text="New Button")
new_button.place(x=250, y=250)

# Entry
my_input = Entry(width=10)
print(my_input.get())
my_input.place(x=400, y=200)

window.mainloop()
