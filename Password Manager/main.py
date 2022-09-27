from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_clicked():

    website = website_entry.get().title()
    email = email_entry.get()
    pw = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pw,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(pw) == 0:
        messagebox.showwarning(title="Insufficient info", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                try:
                    #reading old data
                    data = json.load(data_file)
                    #updating old data with new data
                    data.update(new_data)
                except json.JSONDecodeError:
                    data = new_data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                delete_entries()

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                delete_entries()


def delete_entries():

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# ---------------------------- SEARCH SETUP ------------------------------- #

def find_password():
    search = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message='Error: File of user/passwords is empty')
    else:
        if search in data:
            current_pw = data[search]["password"]
            current_mail = data[search]["email"]
            messagebox.showinfo(title=search, message=f'Email/User: {current_mail}\nPassword: {current_pw}')
        else:
            messagebox.showinfo(title="No details", message='No details for the website/game exists')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Jeppe's Password Manager")
window.configure(padx=40, pady=20)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

#------ Labels -------
website = Label(text="Website:")
website.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

#------ Entries -------
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus_set()
email_entry = Entry(width=44)
email_entry.grid(column=1, row=2, columnspan=2, sticky=E)
email_entry.insert(0, "Jeppeh92@gmail.com")
password_entry = Entry(width=36)
password_entry.grid(column=1, row=3, columnspan=2)

#------ Buttons --------
generate_pw = Button(text="Generate Password", command=password_generation)
generate_pw.grid(column=2, row=3, sticky=W)
search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1, sticky=W)
add = Button(text="Add", width=37, command=add_clicked)
add.grid(column=1, row=4, columnspan=2, sticky=E)





window.mainloop()