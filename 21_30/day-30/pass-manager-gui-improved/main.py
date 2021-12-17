import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    passwd_list = password_letters + password_symbols + password_numbers
    random.shuffle(passwd_list)
    passwd = ''.join(passwd_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, passwd)

    pyperclip.copy(passwd)
    messagebox.showinfo('Success', 'The password was copied to clipboard!')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website_name = website.get()
    email_id = email.get()
    password_put = password.get()

    if website_name and email_id and password_put:
        is_okay = messagebox.askokcancel(website_name,
                                         f'Are you sure you want to save these: \n Email: {email_id} \n Password: {password_put}')
        if is_okay:
            password_to_add = {website_name: {"email": email_id, "password": password_put}}
            try:
                with open("passwords.json", "r+") as pass_file:
                    data = json.load(pass_file)
                    data.update(password_to_add)
                    pass_file.seek(0)
                    json.dump(data, pass_file, indent=4)
            except FileNotFoundError:
                with open("passwords.json", "w") as pass_file:
                    json.dump({}, pass_file, indent=4)
            finally:
                with open("passwords.json", "r+") as pass_file:
                    data = json.load(pass_file)
                    data.update(password_to_add)
                    pass_file.seek(0)
                    json.dump(data, pass_file, indent=4)
            website_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning!', 'Please don\'t leave any of the fields blank')


def search():
    website_name = website.get()
    if website_name:
        with open('passwords.json', 'r+') as pass_file:
            data = json.load(pass_file)
        try:
            search_data = data[website_name]
        except KeyError:
            messagebox.showerror('Not found', 'There was no password found for this website!')
        else:
            messagebox.showinfo('Password Found',
                                f'Email: {search_data["email"]} \n Password: {search_data["password"]}')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = tk.Label(text='Website: ', font=('Courier', 10))
email_label = tk.Label(text='Email/Username: ', font=('Courier', 10))
pass_label = tk.Label(text='Password: ', font=('Courier', 10))
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
pass_label.grid(row=3, column=0)

website = tk.StringVar()
website_entry = tk.Entry(textvariable=website, width=30)
website_entry.focus()
email = tk.StringVar()
email_entry = tk.Entry(textvariable=email, width=40)
password = tk.StringVar()
password_entry = tk.Entry(textvariable=password, width=24)
website_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, columnspan=1)

search_btn = tk.Button(text='Search', command=search)
search_btn.grid(row=1, column=2)
gen_pass_btn = tk.Button(text='Generate Password', command=generate_password)
add_btn = tk.Button(text='Add', width=25, command=save_to_file)
gen_pass_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=3)

window.mainloop()
