# Password Manager
import json
from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle

from main import password_entry


class Manage:
    def __init__(self, website_entry, email_entry, password_entry):
        self.website = website_entry
        self.email = email_entry
        self.password = password_entry

    def save(self):
        global data

        new_data = {
            self.website: {
                "email": self.email,
                "password": self.password,
            }
        }
        if len(self.website) == 0 or len(self.password) == 0:
            messagebox.showinfo(title="OOPS!", message="Please make sure that you haven't left any filed Empty!")
        else:
            messagebox.showinfo(title=self.website,
                                message=f"Successfully Stored!\nEmail:{self.email}\nPassword:{self.password}")
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = new_data
            except json.JSONDecodeError:
                data = new_data
            else:
                if self.website in data:
                    update = messagebox.askyesno("Warning", f"There is already a password saved for {self.website}.\n"
                                                            f"Would you like to overwrite?")
                    if update:
                        data[self.website]["password"] = self.password
                        data[self.website]["email"] = self.email
                    else:
                        return
                else:
                    data.update(new_data)

            finally:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                self.website.delete(0, END)
                self.password.delete(0, END)

    def delete_password(self):

        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except json.JSONDecodeError:
            messagebox.showinfo(title="ERROR!", message="File Not Found!")
        else:
            if self.website in data:
                del data[self.website]
                n_data = data
                data.update(n_data)
                messagebox.showinfo(title="Successful!", message=f"Details deleted for the Website:{self.website}")
            else:
                messagebox.showinfo(title="ERROR!", message=f"No Details2 for the Website:{self.website}")
        finally:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            self.website.delete(0, END)
            self.password.delete(0, END)

    def find_password(self):

        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except json.JSONDecodeError:
            messagebox.showinfo(title="ERROR!", message="File Not Found!")
        else:
            if self.website in data:
                email = data[self.website]["email"]
                password = data[self.website]["password"]
                pyperclip.copy(password)
                messagebox.showinfo(title=self.website, message=f"Email:{email}\nPassword:{password}")
                password_entry.insert(0, password)
            else:
                messagebox.showinfo(title="ERROR!", message=f"No Details1 for the Website:{self.website}")

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letter = [choice(letters) for _ in range(randint(8, 10))]
        password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
        password_number = [choice(numbers) for _ in range(randint(2, 4))]
        password_list = password_letter + password_symbol + password_number
        shuffle(password_list)

        password = "".join(password_list)
        password_entry.insert(0, password)
        pyperclip.copy(password)
#