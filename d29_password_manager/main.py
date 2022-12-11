# from tkinter import *
# from tkinter import messagebox
# import random
#
# import pyperclip
#
#
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
#
#
# def generate_password():
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     nr_letters = random.randint(8, 10)
#     nr_symbols = random.randint(2, 4)
#     nr_numbers = random.randint(2, 4)
#     password_letters = [random.choice(letters) for _ in range(nr_letters)]
#     password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
#     password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
#     password_list = password_numbers + password_letters + password_symbols
#
#     random.shuffle(password_list)
#
#     password = "".join(password_list)
#     entry3.delete(0, END)
#     entry3.insert(0, string=password)
#
#     pyperclip.copy(password)
#
# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save_password():
#     my_website = entry1.get()
#     my_email = entry2.get()
#     my_password = entry3.get()
#     if my_website == "" or my_email == "" or my_password == "":
#         messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
#     else:
#         new_entry = f"{my_website} | {my_email} | {my_password}\n"
#         if messagebox.askokcancel(title=my_website, message=f"These are the details entered: \nEmail: {my_email}\n"
#                                                          f"Password: {my_password}"):
#             print(new_entry)
#             with open("data.txt", mode="a") as file:
#                 file.write(new_entry)
#             entry1.delete(0, END)
#             entry2.delete(0, END)
#             entry3.delete(0, END)
#             entry2.insert(0, string="mo1der@hotmail.com")
#             entry1.focus()
#
# # ---------------------------- UI SETUP ------------------------------- #
#
# FONT_NAME = "Arial"
# FONT_SIZE = 10
#
# window = Tk()
# window.title("Password Manager")
# window.config(padx=20, pady=20, bg="white")
#
# canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
# my_pass_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=my_pass_img)
# canvas.pack()
# canvas.grid(row=0, column=1)
#
# label1 = Label(text="Website:", font=(FONT_NAME, FONT_SIZE, "normal"), fg="black", bg="white")
# label1.config(padx=5, pady=5)
# label1.grid(sticky="E", row=1, column=0)
#
# label2 = Label(text="Emai/Username:", font=(FONT_NAME, FONT_SIZE, "normal"), fg="black", bg="white")
# label2.config(padx=5, pady=5)
# label2.grid(sticky="E", row=2, column=0)
#
# label3 = Label(text="Password:", font=(FONT_NAME, FONT_SIZE, "normal"), fg="black", bg="white")
# label3.config(padx=5, pady=5)
# label3.grid(sticky="E", row=3, column=0)
#
# button1 = Button(text="Generate Password", command=generate_password)
# button1.grid(sticky="W", row=3, column=2)
#
# button2 = Button(text="Add", command=save_password, width=36)
# button2.grid(sticky="W", row=4, column=1, columnspan=2)
#
# entry1 = Entry(width=35)
# entry1.insert(END, string="")
# entry1.grid(sticky="W", row=1, column=1, columnspan=2)
# entry1.focus() #ustawia kursor na danym polu
#
# entry2 = Entry(width=35)
# entry2.insert(0, string="mo1der@hotmail.com") # 0 początek, przed ewentualym tekstem, END na końcu
# entry2.grid(sticky="W", row=2, column=1, columnspan=2)
#
# entry3 = Entry(width=21)
# entry3.insert(END, string="")
# entry3.grid(sticky="W", row=3, column=1)
#
#
#
#
# window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
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
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()