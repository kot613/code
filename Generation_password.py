import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH ACCOUNT ------------------------------- #
def search():
    website = input_website.get()
    with open('data/data_my_pass.json', 'r', encoding='utf-8') as read_f:
        data_file = json.load(read_f)
        website_data = data_file.get(website)
        if website_data:
            input_password.insert(0, website_data['password'])
            messagebox.showinfo(title='Search',
                                message=f'Website:{website}\nEmail:{website_data["email"]}\nPassword:{website_data["password"]}')
        else:
            messagebox.showinfo(title='Search',
                                message=f'No details for the website {website} exists')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    input_password.delete(0, tk.END)
    ch_letters = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ch_numbers = '1234567890'
    ch_symbols = '+-/*!&$#?=@<>'
    num_letters = random.randint(8, 10)
    num_numbers = random.randint(3, 5)
    num_symbols = random.randint(2, 4)

    lst_letters = [random.choice(ch_letters) for _ in range(num_letters)]
    lst_numbers = [random.choice(ch_numbers) for _ in range(num_numbers)]
    lst_symbols = [random.choice(ch_symbols) for _ in range(num_symbols)]

    password_lst = lst_letters + lst_numbers + lst_symbols
    random.shuffle(password_lst)
    password = ''.join(password_lst)
    input_password.insert(0, password)
    pyperclip.copy(text=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def submit():
    website = input_website.get().lower()
    email = input_email.get().lower()
    password = input_password.get()
    data = {
        website: {
            'email': email,
            'password': password,
        }
    }
    if website and email and password:
        # is_ok = messagebox.askokcancel(title=website, message=f"Yor data:\nEmail: {email}\nPassword: {password}\nSave?")
        # if is_ok:
        try:
            with open('data/data_my_pass.json', 'r', encoding='utf-8') as read_f:
                data_file = json.load(read_f)
                data_file.update(data)
        except Exception as ex:
            print(f'Catch exceptions{ex.__class__}--{ex}')
            data_file = data
        with open('data/data_my_pass.json', 'w', encoding='utf-8') as write_f:
            json.dump(data_file, write_f, indent=4)

        input_website.delete(0, tk.END)
        input_password.delete(0, tk.END)
    else:
        messagebox.showinfo(title='Generate Password', message='Wrong data input')


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

canvas = tk.Canvas(width=200, height=189)
image = tk.PhotoImage(file='data/logo_pass.png')
canvas.create_image(100, 95, image=image)
canvas.grid(row=0, column=1)

label_website = tk.Label(text='Website:', font=20)
label_website.grid(row=1, column=0)

label_email = tk.Label(text='Email/Username:', font=20)
label_email.grid(row=2, column=0)

label_password = tk.Label(text='Password:', font=20)
label_password.grid(row=3, column=0)

input_website = tk.Entry(width=30)  # 50
input_website.focus()
input_website.grid(row=1, column=1)

input_email = tk.Entry(width=30)  # 50
input_email.grid(row=2, column=1)
input_email.insert(0, 'email@email.com')

input_password = tk.Entry(width=30)  # 31
input_password.grid(row=3, column=1)

button_generate = tk.Button(text='Generate Password', command=generate, width=20)
button_generate.grid(row=3, column=2)

button_search = tk.Button(text='Search', command=search, width=20)
button_search.grid(row=1, column=2)

button_submit = tk.Button(text='Add', command=submit, width=50)  # 42
button_submit.grid(row=4, column=1, columnspan=2)

window.mainloop()
