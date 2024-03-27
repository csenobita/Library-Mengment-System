from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox

root = Tk()
root.title("Libraryan Login Page")
root.geometry("1026x770+400+100")
root.resizable(False, False)

password_var=StringVar()
username_var=StringVar()
fream = Frame(root, width = 1920, height = 1800, border = 0, bd = 5)
fream.pack()
ima = Image.open("Librarya_login_page.jpg")

images = ImageTk.PhotoImage(ima)
level = Label(image = images)
level.place(x = 0, y = 0)


# =========================================================funsion==============================


def on_enter1(e):
	username.delete(0, END)


def close_enter1(e):
	name = username.get()
	if name == '':
		username.insert(0, "Username")


def ON_enter2(e):
	password.delete(0, END)


def close_enter2(e):
	name = password.get()
	if name == '':
		password.insert(0, "Password")


# ___________________________________________username--------------------------------------------


username = Entry(level, font = ("arial", 12), border = 0, fg = "black", width = 25,textvariable = username_var)
username.insert(0, "Username")
username.place(x = 725, y = 211)
username.bind('<FocusIn>', on_enter1)
username.bind('<FocusOut>', close_enter1)

# ==================================================passwrod============================


password = Entry(level, font = ("arial", 12), border = 0, fg = "black", width = 25,textvariable = password_var)
password.insert(0, "Password")
password.bind('<FocusIn>', ON_enter2)
password.bind('<FocusOut>', close_enter2)
password.place(x = 725, y = 267)


#############-------------------------------------bottom------------------------------------------


def user_login():
	try:
		conn = pymysql.connect(host = 'localhost', user = 'root', password = '112233',database = 'userdata')
		mycursor = conn.cursor()
	except:
		messagebox.showerror('Error', 'DataBase Not connect')
		return
	
	username1=username_var.get()
	if username1.islower():
		password1=password_var.get()
		if 8<= len(password1) <= 32:
			query1 = 'select * from data where username=%s and password =%s'
			mycursor.execute(query1, (username.get(), password.get()))
			row = mycursor.fetchone()
			if row == None:
				messagebox.showerror('Error', 'Invalid username and password')
			else:
				messagebox.showinfo('Plz Waiting', 'account login ')
				root.destroy()
				
				import main_page
		else:
			messagebox.showerror('Error', 'Password must be between 8 and 32 characters')
	else:
		messagebox.showerror('Error', 'Username must be in lower case')


log_ima = Image.open("login3.png")
imag = ImageTk.PhotoImage(log_ima)

login_button = Button(level, image = imag, bg = "#FFFFFF", border = 0, activebackground = "white", cursor = "hand2",
                      command = user_login)
login_button.place(x = 800, y = 320)

signup_title = Label(level, text = "Have not account yet?", font = ('arial', 10), border = 0, bg = "white")
signup_title.place(x = 700, y = 450)


def sign_up():
	root.destroy()
	import reg


def close_button():
	root.destroy()


sinup_button = Button(level, text = "Sign Up", font = ('arial', 8), fg = "blue", border = 0, bg = "#FFFFFF",
                      activebackground = "white", cursor = "hand2", command = sign_up)
sinup_button.place(x = 900, y = 450)

close_button = Button(level, text = "close", font = ('arial', 10, 'bold'), fg = 'black', border = 0, bg = "white",
                      command = close_button)
close_button.place(x = 950, y = 10)

root.mainloop()
