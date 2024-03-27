from tkinter import *

from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox

root = Tk()
root.title("Libraryan Sinup")
root.geometry("1025x770+400+100")
root.resizable(False, False)

email_var = StringVar()
mobile_var = StringVar()
username_var = StringVar()
password_var = StringVar()

fream = Frame(root, width = 1025, height = 770)
fream.pack()

im2 = Image.open("Libraryan_sinup_page.jpg")
im3 = ImageTk.PhotoImage(im2)
label = Label(image = im3, border = 0)
label.place(x = -1, y = 0)


def clear():
	Librayan_txt_mobile.delete(0, END)
	Librayan_txt_username.delete(0, END)
	Librayan_txt_password1.delete(0, END)
	Librayan_txt_password2.delete(0, END)
	Librayan_txt_email.delete(0, END)


def connect_database():
	# ==================================================filed close=================================
	global my_cursor, conn
	if Librayan_txt_email.get() == '' or Librayan_txt_password1.get() == '' or Librayan_txt_password2.get() == '' or Librayan_txt_username.get() == '' or Librayan_txt_mobile.get() == '' or Librayan_txt_fullname.get() == '':
		
		messagebox.showerror('Error', 'All Fild Is Null')
	
	# =================================password chack=======================================
	elif Librayan_txt_password1.get() != Librayan_txt_password2.get():
		messagebox.showerror('Error', 'Password Not matching')
	
	else:
		
		try:
			# ============================================database connect==========================
			conn = pymysql.connect(host = 'localhost', user = 'root', password = '112233')
			my_cursor = conn.cursor()
		
		except:
			messagebox.showerror('Error', 'Database Connect Issue, Try Again')
		
		try:
			# ====================database create==============================
			
			qurey_database_add = 'create database userdata'
			my_cursor.execute(qurey_database_add)
			database_use = 'use userdata'
			my_cursor.execute(database_use)
			database_table_data = ('create table data(id int auto_increment primary key not null, email varchar(100), '
			                       'username varchar(100), password varchar(32),'
			                       'fullname varchar(100),mobile varchar(15))')
			
			
			my_cursor.execute(database_table_data)
		
		except:
			my_cursor.execute('use userdata')
		
		# =============================username chack========================================
		username_chack = 'select * from data where username=%s'
		my_cursor.execute(username_chack, (Librayan_txt_username.get()))
		row = my_cursor.fetchone()
		
		if row != None:
			messagebox.showerror('Error', 'Username Already Exists')
		
		
		else:
			# =====================================email chack===========================
			email1 = email_var.get()
			if (email1.count('@') == 1 and 1 == email1.count('.') and (
				email1.endswith("@gmail.com") or email1.endswith("@yahoo.com") or
				email1.endswith("outlook.com") or email1.endswith("@hotmail.com")) and len(
				email1) <= 32):
				
				# =====================================mobile  chack========================
				mobile1 = mobile_var.get()
				if ((mobile1.startswith('013') or mobile1.startswith('014') or mobile1.startswith('015')
				     or mobile1.startswith('016') or mobile1.startswith('017') or mobile1.startswith(
						'018') or mobile1.startswith('019'))
					and len(mobile1) == 11):
					# ======================================username  chack========================
					if username_var.get().islower():
						password3 = password_var.get()
						if 8 <= len(password3) <= 32:
							
							# ====================database upload ==========================
							
							qurey_insert = (
								'insert into data(fullname,email,mobile,username,password) values (%s,%s,%s,%s,%s)')
							my_cursor.execute(qurey_insert, (
								Librayan_txt_fullname.get(), Librayan_txt_email.get(),
								Librayan_txt_mobile.get(),
								Librayan_txt_username.get(),
								Librayan_txt_password1.get()))
							
							conn.commit()
							conn.close()
							messagebox.showinfo('Success', 'Registration is successful')
							clear()
							
							root.destroy()
							import login_page
						else:
							messagebox.showerror('Error',
							                     'Password must be between 8 and 32 characters')
					
					else:
						messagebox.showerror('Error', 'Username must be in lower case')
				else:
					messagebox.showerror('Error', 'Mobile Number Incorrect')
			else:
				messagebox.showerror('Error', 'Email incorrect')


# ====================================== open_close =====================================
def Name_enter(e):
	Librayan_txt_fullname.delete(0, END)


def Name_close(e):
	name = Librayan_txt_fullname.get()
	if name == '':
		Librayan_txt_fullname.insert(0, "Full Name")


def email_enter(e):
	Librayan_txt_email.delete(0, END)


def email_close(e):
	name = Librayan_txt_email.get()
	if name == '':
		Librayan_txt_email.insert(0, "Email")


def mobile_enter(e):
	Librayan_txt_mobile.delete(0, END)


def mobile_close(e):
	name = Librayan_txt_mobile.get()
	if name == '':
		Librayan_txt_mobile.insert(0, "Mobile")


def username_enter(e):
	Librayan_txt_username.delete(0, END)


def username_close(e):
	name = Librayan_txt_username.get()
	if name == '':
		Librayan_txt_username.insert(0, "Username")


def password1_enter(e):
	Librayan_txt_password1.delete(0, END)


def password1_close(e):
	name = Librayan_txt_password1.get()
	if name == '':
		Librayan_txt_password1.insert(0, "Password")


def password2_enter(e):
	Librayan_txt_password2.delete(0, END)


def password2_close(e):
	name = Librayan_txt_password2.get()
	if name == '':
		Librayan_txt_password2.insert(0, "Conform Password")


# ===========================================informations=========================================

Librayan_txt_fullname = Entry(label, font = ("arial", 12), width = 26, border = 0)
Librayan_txt_fullname.place(x = 719, y = 140)
Librayan_txt_fullname.insert(0, "Full Name")
Librayan_txt_fullname.bind('<FocusIn>', Name_enter)
Librayan_txt_fullname.bind('<FocusOut>', Name_close)

Librayan_txt_email = Entry(label, font = ("arial", 12), width = 26, border = 0, textvariable = email_var)
Librayan_txt_email.place(x = 719, y = 205)
Librayan_txt_email.insert(0, "Email")
Librayan_txt_email.bind('<FocusIn>', email_enter)
Librayan_txt_email.bind('<FocusOut>', email_close)

Librayan_txt_mobile = Entry(label, font = ("arial", 12), width = 26, border = 0, textvariable = mobile_var)
Librayan_txt_mobile.place(x = 719, y = 270)
Librayan_txt_mobile.insert(0, "Mobile")
Librayan_txt_mobile.bind('<FocusIn>', mobile_enter)
Librayan_txt_mobile.bind('<FocusOut>', mobile_close)

Librayan_txt_username = Entry(label, font = ("arial", 12), width = 26, border = 0, textvariable = username_var)
Librayan_txt_username.place(x = 719, y = 335)
Librayan_txt_username.insert(0, "Username")
Librayan_txt_username.bind('<FocusIn>', username_enter)
Librayan_txt_username.bind('<FocusOut>', username_close)

Librayan_txt_password1 = Entry(label, font = ("arial", 12), width = 26, border = 0, textvariable = password_var)
Librayan_txt_password1.place(x = 719, y = 400)
Librayan_txt_password1.insert(0, "Password")
Librayan_txt_password1.bind('<FocusIn>', password1_enter)
Librayan_txt_password1.bind('<FocusOut>', password1_close)

Librayan_txt_password2 = Entry(label, font = ("arial", 12), width = 26, border = 0)
Librayan_txt_password2.place(x = 719, y = 470)
Librayan_txt_password2.insert(0, "Conform Password")
Librayan_txt_password2.bind('<FocusIn>', password2_enter)
Librayan_txt_password2.bind('<FocusOut>', password2_close)

# ========================Buttons Images add ==========================================================

im = Image.open("sinup.png")
im4 = ImageTk.PhotoImage(im)
sin_up_ = Button(label, image = im4, border = 0, bg = "white", activebackground = "white",
                 command = connect_database)
sin_up_.place(x = 770, y = 560)

root.mainloop()
