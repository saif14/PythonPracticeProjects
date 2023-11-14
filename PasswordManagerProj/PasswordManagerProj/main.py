from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(9, 12))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops!", message="Please make sure you haven't left any field empty.")
    else:
        # table = [[website, email, password]]
        # tab = PrettyTable(table[0])
        # print(tab)
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    website_entry.focus()


# -------------------------- Find Password ----------------------------

def find_password():
    try:
        with open("data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
            value = data[website_entry.get()]

    except FileNotFoundError:
        messagebox.showerror(title="No Data File Found!", message="Sorry! No Data File Found!")

    except KeyError:
        messagebox.showwarning(title="No Details Found!", message="Sorry! No details for the website exists!")

    else:
        email = value["email"]
        password = value["password"]
        messagebox.showinfo(title=f"{website_entry.get().title()}", message=f"Website: {website_entry.get()}\n"
                                                          f"Email: {email}\n"
                                                          f"Password: {password}")




# -------------------------Button Hover Setting------------------------
def enter(e):
    e.widget["bg"] = "#0a0a23"
    e.widget["fg"] = "white"


def leave(e):
    e.widget["bg"] = "SystemButtonFace"
    e.widget["fg"] = "black"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=logo_image)
canvas.grid(row=0, column=1)

window.iconphoto(False, logo_image)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
user_name_label = Label(text="Email/User Name:")
user_name_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=28, borderwidth=0)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()
user_name_entry = Entry(width=53, borderwidth=0)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "mahmudalsaif@gmail.com")
password_entry = Entry(width=28, borderwidth=0)
password_entry.grid(row=3, column=1, sticky="w", padx=0)

generate_pass_btn = Button(text="Generate Password", borderwidth=0.5, command=password_generator, width=15)
generate_pass_btn.grid(row=3, column=2, pady=5)

add_btn = Button(text="Add", width=30, command=save_password, borderwidth=0.5)
add_btn.grid(row=5, column=1, columnspan=2)

search_btn = Button(text="Search", width=15, borderwidth=0.5, command=find_password)
search_btn.grid(row=1, column=2, sticky="w", pady=5)

generate_pass_btn.update()
print(search_btn.cget("bg"))

# Handling button hover animation
search_btn.bind("<Enter>", enter)
search_btn.bind("<Leave>", leave)
generate_pass_btn.bind("<Enter>", enter)
generate_pass_btn.bind("<Leave>", leave)
add_btn.bind("<Enter>", enter)
add_btn.bind("<Leave>", leave)

window.mainloop()
