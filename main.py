from tkinter import END, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox
from random import randint, choice, shuffle
import pyperclip
import json

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Random Password Generator
def generator():
    letters_raw = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    letters_cap_raw = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    symbols_raw = "!,@,#,$,%,^,&,*,(,),_,+,=,-,.,/,<,>,?,;,:"
    numbers_raw = "1,2,3,4,5,6,7,8,9,0"
    letters = letters_raw.split(",")
    capitals = letters_cap_raw.split(",")
    symbols = symbols_raw.split(",")
    numbers = numbers_raw.split(",")

    pass_letters = [choice(letters) for _ in range(randint(3, 4))]
    pass_symbols = [choice(symbols) for _ in range(randint(3, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(3, 4))]
    pass_capital = [choice(capitals) for _ in range(randint(2, 3))]

    password_list = pass_letters + pass_numbers + pass_symbols + pass_capital
    shuffle(password_list)
    password = "".join(password_list)
    passwd_input.insert(0, password)
    pyperclip.copy(password)


# Saving data
def save_data():
    web = website_input.get()
    username = email_input.get()
    passwd = passwd_input.get()
    new_data = {
        web: {
            "username": username,
            "passwd": passwd,
        }
    }

    if len(web) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="OOPS", message="Please fill all fields!")
    else:
        try:
            with open("./data.json", "r") as data_file:
                # Reading da.json
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./data.json", "w") as data_file:
                json.dump(new_data, data_file)
        else:
            # Updating data.json
            data.update(new_data)

            with open("./data.json", "w") as data_file:
                json.dump(data, data_file)
        finally:
            website_input.delete(0, END)
            passwd_input.delete(0, END)


# Search through data
def search():
    web = website_input.get()
    if len(web) == 0:
        messagebox.showinfo(title="Error", message="You have not Entered any thing")
    else:
        try:
            with open("./data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found")
        else:
            if web in data:
                username = data[web]["username"]
                password = data[web]["passwd"]
                pyperclip.copy(password)
                messagebox.showinfo(
                    title="Website Info",
                    message=f"Username is {username} and password is {password}",
                )
            else:
                messagebox.showinfo(
                    title="Error", message=f"No deetails for {web} found in data"
                )


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

website = Label(text="Website:")
website.grid(row=2, column=1)

email = Label(text="Email/Username:")
email.grid(row=3, column=1)

passwd = Label(text="Password:")
passwd.grid(row=4, column=1)

# Button
generate_btn = Button(text="Generate", command=generator, width=10)
generate_btn.grid(row=4, column=3)

add_btn = Button(text="Add", width=35, command=save_data)
add_btn.grid(row=5, column=2, columnspan=2)

search_btn = Button(text="Search", command=search, width=10)
search_btn.grid(row=2, column=3)

# Entry
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=2, column=2)

email_input = Entry(width=35)
email_input.insert(0, "subrathitachi6@gmail.com")
email_input.grid(row=3, column=2, columnspan=2)

passwd_input = Entry(width=21)
passwd_input.grid(row=4, column=2)


window.mainloop()
