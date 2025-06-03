# manage.py
import json
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle

# This import is assumed to provide the password_entry widget.
# In a real application, you'd typically pass all necessary widgets
# or their values to the class methods.
# For demonstration, a dummy password_entry is defined in main.py.
# from main import password_entry # This line will be handled by main.py

class Manage:
    """
    Manages password saving, deletion, searching, and generation.
    """
    def __init__(self, website_entry_widget, email_entry_widget, password_entry_widget):
        """
        Initializes the Manage class with Tkinter Entry widgets.
        These widgets are stored as instance variables to allow direct manipulation.
        """
        self.website_entry = website_entry_widget
        self.email_entry = email_entry_widget
        self.password_entry = password_entry_widget # Store the password entry widget

    def save(self):
        """
        Saves the website, email, and password details to a JSON file.

        Bug 1: Always overwrites existing entries without asking for confirmation.
        """
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="OOPS!", message="Please make sure that you haven't left any field Empty!")
        else:
            messagebox.showinfo(title=website,
                                 message=f"Successfully Stored!\nEmail:{email}\nPassword:{password}")
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {} # Start with an empty dictionary if file not found
            except json.JSONDecodeError:
                data = {} # Start with an empty dictionary if JSON is invalid
            finally:
                # Bug 1: Always overwrite without asking.
                # The 'if website in data:' check is still performed,
                # but the confirmation prompt is skipped.
                data.update(new_data) # This line now unconditionally updates or adds

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                self.website_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')

    def delete_password(self):
        """
        Deletes the password entry for the specified website from the JSON file.
        """
        website = self.website_entry.get()
        if not website:
            messagebox.showinfo(title="Input Error", message="Please enter a website to delete.")
            return

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(title="ERROR!", message="No data file found or file is corrupted!")
            return
        else:
            if website in data:
                del data[website]
                messagebox.showinfo(title="Successful!", message=f"Details deleted for the Website: {website}")
            else:
                messagebox.showinfo(title="ERROR!", message=f"No Details found for the Website: {website}")
        finally:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            self.website_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

    def find_password(self):
        """
        Finds the password for the specified website and copies it to the clipboard.

        Bug 2: Always copies a fixed, incorrect password to the clipboard.
        """
        website = self.website_entry.get()
        if not website:
            messagebox.showinfo(title="Input Error", message="Please enter a website to search.")
            return

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(title="ERROR!", message="No data file found or file is corrupted!")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                # Bug 2: Always copies a fixed, incorrect password.
                pyperclip.copy("BUGGED_PASSWORD_123!") # This is the bug
                self.password_entry.delete(0, 'end') # Clear before inserting
                self.password_entry.insert(0, password)
                messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}\n(Password copied to clipboard: BUGGED_PASSWORD_123!)")
            else:
                messagebox.showinfo(title="ERROR!", message=f"No Details found for the Website: {website}")

    def generate_password(self):
        """
        Generates a random password and inserts it into the password entry field.
        """
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letter = [choice(letters) for _ in range(randint(8, 10))]
        password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
        password_number = [choice(numbers) for _ in range(randint(2, 4))]
        password_list = password_letter + password_symbol + password_number
        shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.delete(0, 'end')
        self.password_entry.insert(0, password)
        pyperclip.copy(password) # This part is still correct, but Bug 2 is in find_password
