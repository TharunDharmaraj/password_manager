# from random import choice, randint, shuffle
from tkinter import *
# from tkinter import messagebox
# import pyperclip
# import json


import manage_password

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u',
#                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P',
#                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     password_letter = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
#     password_number = [choice(numbers) for _ in range(randint(2, 4))]
#     password_list = password_letter + password_symbol + password_number
#     shuffle(password_list)
#
#     password = "".join(password_list)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
#
#
# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():
#     global data
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     new_data = {
#         website: {
#             "email": email,
#             "password": password,
#         }
#     }
#     if len(website) == 0 or len(password) == 0:
#         messagebox.showinfo(title="OOPS!", message="Please make sure that you haven't left any filed Empty!")
#     else:
#         messagebox.showinfo(title=website, message=f"Successfully Stored!\nEmail:{email}\nPassword:{password}")
#         try:
#             with open("data.json", "r") as data_file:
#                 data = json.load(data_file)
#         except FileNotFoundError:
#             data = new_data
#         except json.JSONDecodeError:
#             data = new_data
#         else:
#             if website in data:
#                 update = messagebox.askyesno("Warning", f"There is already a password saved for {website}.\n"
#                                                         f"Would you like to overwrite?")
#                 if update:
#                     data[website]["password"] = password
#                     data[website]["email"] = email
#                 else:
#                     return
#             else:
#                 data.update(new_data)
#
#         finally:
#             with open("data.json", "w") as data_file:
#                 json.dump(data, data_file, indent=4)
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
#
#
# # ---------------------------delete the particular password------------------- #
# def delete_password():
#     website = website_entry.get()
#
#     try:
#         with open("data.json") as data_file:
#             data = json.load(data_file)
#     except json.JSONDecodeError:
#         messagebox.showinfo(title="ERROR!", message="File Not Found!")
#     else:
#         if website in data:
#             del data[website]
#             n_data=data
#             data.update(n_data)
#             messagebox.showinfo(title="Successful!", message=f"Details deleted for the Website:{website}")
#         else:
#             messagebox.showinfo(title="ERROR!", message=f"No Details for the Website:{website}")
#     finally:
#         with open("data.json", "w") as data_file:
#              json.dump(data, data_file, indent=4)
#         website_entry.delete(0, END)
#         password_entry.delete(0, END)
#
# # ---------------------------- find password------------------------------- #
# def find_password():
#     website = website_entry.get()
#     try:
#         with open("data.json") as data_file:
#             data = json.load(data_file)
#     except json.JSONDecodeError:
#         messagebox.showinfo(title="ERROR!", message="File Not Found!")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             pyperclip.copy(password)
#             messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
#             password_entry.insert(0, password)
#         else:
#             messagebox.showinfo(title="ERROR!", message=f"No Details for the Website:{website}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# labels
website_lable = Label(text="Website:")
website_lable.grid(row=1, column=0)
email_lable = Label(text="Email/Username:")
email_lable.grid(row=2, column=0)
password_lable = Label(text="password:")
password_lable.grid(row=3, column=0)
# entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(END, "tharun@gmail.com")
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1, sticky="EW")
password = manage_password.Manage(website_entry.get(), email_entry.get(), password_entry.get())
# buttons
search_button = Button(text="Search")
search_button.grid(row=2, column=2, sticky="EW")
delete_button = Button(text="Delete")
delete_button.grid(row=1, column=2, sticky="EW")
generate_password_button = Button(text="Generate Password", command=password.generate_password())
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Save Password", width=36, command=password.save())
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
