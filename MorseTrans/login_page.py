import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

username = "admin" #that's the given username
password = "admin" #that's the given password


class LoginPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Login Page")

        style = ttk.Style()
        style.configure("TEntry", foreground="red",background="yellow")

        # Add a label for the title
        title_label = tk.Label(self, text="Login to access to Translator App", font=("Calibri (Body)", 20))
        title_label.pack(pady=10)

        # Add a label for the username field
        username_label = tk.Label(self, text="Username", font=("courier", 12))
        username_label.pack(pady=(30, 10))

        # Add an entry for the username field
        self.username_entry = ttk.Entry(self,  font = ('courier', 12, 'bold'), justify = CENTER, width=30, style="TEntry")
        self.username_entry.pack()

        # Add a label for the password field
        password_label = tk.Label(self, text="Password", font=("courier", 12))
        password_label.pack(pady=(20, 10))

        # Add an entry for the password field
        self.password_entry = ttk.Entry(self, show="*", font = ('courier', 12, 'bold'),justify = CENTER, width=30,style="TEntry")
        self.password_entry.pack()

        # Add a button for the login action
        login_button = tk.Button(self, text="Login", font=("courier", 12), bg="#4CAF50", fg="#FFF", width=15, padx=5, pady=6, command=self.login)
        login_button.pack(pady=20)

        # Add a button for the dark mode toggle
        self.dark_mode = tk.BooleanVar()
        dark_mode_checkbox = tk.Checkbutton(self, text="Dark mode", variable=self.dark_mode, font=("Arial", 12), command=self.toggle_dark_mode)
        dark_mode_checkbox.pack(pady=20)


        self.ErrorM = tk.Label(self, text="", font=("courier", 10))
        self.ErrorM.pack(pady=(5))

        # Set the initial theme
        self.set_theme()

    def new_win(self,name_page):
        import self.name_page

    def login(self):
        # Add your login code here
        if username == self.username_entry.get() and password == self.password_entry.get():
            print("Correct")
            self.parent.destroy()
            import home_page
            
        else:
            print("Wrong")
            self.ErrorM['text'] = 'Wrong Entry!'
            self.ErrorM.config(bg= "white", fg= "red")




    def set_theme(self):

        # Set the theme based on the dark mode flag
        if self.dark_mode.get():
            self.configure(background="#333")
            for child in self.winfo_children():
                child.configure(background="#333", foreground="#0052cc")
        else:
            self.configure(background="#1a75ff")
            for child in self.winfo_children():
                child.configure(background="#1a75ff", foreground="#000000")


    def toggle_dark_mode(self):
        # Toggle the dark mode flag and update the theme
        self.set_theme()


# Create the main window and login page
root = tk.Tk()

width_of_window = 550
height_of_window = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

# root.geometry("400x400")
login_page = LoginPage(root)
login_page.pack(fill="both", expand=True)

# Start the event loop
root.mainloop()
