from re import search
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#---------------------------- Search ---------------------------------------------#
def search_web():
    web = website_entry.get()
    with open('data.json', 'r') as data_file:
        try:
            data = json.load(data_file)
            messagebox.showinfo(title=web, message=f"Email:{data[web]['email']}\n Password:{data[web]['password']}")
        except KeyError:
            if web == '':
                messagebox.showinfo(title='Error', message= 'Please enter your website')
            else:
                messagebox.showinfo(title='Error', message='Your website is not saved please check the it properly')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data ={
        website: {
            "email": email,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:

                    # reading old data
                    data = json.load(data_file)
                    # updating old data
                    data.update(new_data)

            except FileNotFoundError:
                    with open("data.json", 'w') as data_file:
                        # saving the data
                            json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", 'w') as data_file:
                # saving the data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,sticky = W, padx= 20)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky= W, padx= 20)
email_entry.insert(0, "soumyarawat0305@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky= W, padx= 20)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, width=16)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky= W)
search_button = Button(text='Search', width=16, command=search_web)
search_button.grid(row=1, column=2, sticky=W)

window.mainloop()