from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(1, nr_letters + 1)]
    password_list += [random.choice(symbols) for _ in range(1, nr_symbols + 1)]
    password_list += [random.choice(numbers) for _ in range(1, nr_numbers + 1)]

    random.shuffle(password_list)

    new_password = "".join(password_list)
    password.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_name.get()
    username = email_username.get()
    password_text = password.get()

    if website == "" or password_text == "":
        messagebox.showwarning(title=website,
                               message="You cannot leave the fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered: \nUsername: {username} "
                                           f"\nPassword: {password_text} \nIs it okay to save?")

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {username} | {password_text} \n")
            file.close()
            website_name.delete(0, END)
            password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_em_us = Label(text="Email/Username:")
label_em_us.grid(row=2, column=0)

label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

website_name = Entry(width=38)
website_name.grid(row=1, column=1, columnspan=2)
website_name.focus()

email_username = Entry(width=38)
email_username.grid(row=2, column=1, columnspan=2)
email_username.insert(0, "abc@gmail.com")

password = Entry(width=21)
password.grid(row=3, column=1)

gen_pass_button = Button(text="Generate Password", command=password_generator)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
