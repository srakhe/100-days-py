import tkinter

# Create window and modify properties
window = tkinter.Tk()
window.title('First GUI')
window.minsize(width=500, height=300)

# Create label
my_label = tkinter.Label(text='Hi this is a label', font=('Arial', 24, 'bold'))
my_label.pack(side='left')

my_label.config(text='New text')
my_label['text'] = 'Other text'


def clicked():
    my_label.config(text=my_entry.get())


# Create Button
my_button = tkinter.Button(text='Click Me', command=clicked)
my_button.pack(side='right')

# Input Field: Entry
my_entry = tkinter.Entry(width=10)
my_entry.pack()


# Clear the tkinter window

def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list


widget_list = all_children(window)
for item in widget_list:
    item.pack_forget()

# Other things tkinter ~~~~~~~~~~~~~

# Text (multi line entry)
# Spinbox
# Scale
# Radiobutton
# Checkbutton
# Listbox

# Text height = no of lines
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
# text.insert("Example of multi-line text entry.", chars='30')
# Get's current value in textbox at line 1, character 0
print(text.get("1.0"))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
