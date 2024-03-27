from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import ttk
from tkinter import messagebox

root2 = Tk()

root2.title("Student Registration")
root2.geometry("1026x770+400+100")
root2.resizable(False, False)

roll_var=StringVar()
reg_var=StringVar()
mobile_var=StringVar()
email_var=StringVar()




fream = Frame(root2, width = 1026, height = 770, border = 0, bd = 5)
fream.pack()
ima = Image.open("Student_reg_form.jpg")

images = ImageTk.PhotoImage(ima)
level = Label(image = images)
level.place(x = 0, y = 0)


def student_database_connect():
	conn = pymysql.connect(host = 'localhost', user = 'root', password = '112233', database = 'userdata')
	my_cursor = conn.cursor()
	chack_data = 'select * from student where reg=%s and roll=%s'
	my_cursor.execute(chack_data, (Student_reg.get(), Student_roll.get()))
	row = my_cursor.fetchone()
	if row != None:
		messagebox.showerror('Error', 'Roll number and Reg. Number already exists')
	else:
		roll1=roll_var.get()
		reg1=reg_var.get()
		mobile1=mobile_var.get()
		email1=email_var.get()
		if len(roll1)==6:
			if len(reg1)==6 or len(reg1)==10:
				if len(mobile1)==11  :
					if  (mobile1.startswith('013') or  mobile1.startswith('014') or mobile1.startswith('015') or mobile1.startswith('016') or mobile1.startswith('017') or
				                           mobile1.startswith('018') or mobile1.startswith('019')):
						if ((email1.endswith('@gmail.com') or email1.endswith('@yahoo.com') or
							email1.endswith('@hotmail.com') or email1.endswith('@outlook.com') )
							and len(email1)<=32 and email1.count('.')==1 and email1.count('@') and email1.count(' ')==0 and email1.count('_')==0):
				
		
		
							qurey_insert = ('insert into student(name,roll,reg,mobile,email,college,address,blood ) values(%s,%s,'
							                '%s,%s,%s,%s,%s,%s)')
							my_cursor.execute(qurey_insert, (Student_name.get(), Student_roll.get(),
							                                 Student_reg.get(), Student_mobile.get(),
							                                 Student_email.get(), Student_college.get(),
							                                 Student_address.get(), Student_blood.get()))
							conn.commit()
							conn.close()
							messagebox.showinfo('Success', 'Registration is successful')
							root.destroy()
						else:
							messagebox.showerror('Error', 'Email Address is not valid')
					else:
						messagebox.showerror('Error', 'Needed Bangladesh Mobile Number  ')
				else:
					messagebox.showerror('Error ','Mobile Number must be 11 digits ')
				
			else:
				messagebox.showerror('Error','Registration is must be 6 and 10 digits')
		else:
			messagebox.showerror('Error', 'Roll Number must be 6 digits')
			
	
	
	


def name_enter(e):
	Student_name.delete(0, END)


def name_levea(e):
	if Student_name.get() == '':
		Student_name.insert(0, 'Student Name')


def roll_enter(e):
	Student_roll.delete(0, END)


def roll_levea(e):
	if Student_roll.get() == '':
		Student_roll.insert(0, "Roll Number")


def reg_enter(e):
	Student_reg.delete(0, END)


def reg_levea(e):
	if Student_reg.get() == '':
		Student_reg.insert(0, 'Reg. Number')


def mobile_enter(e):
	Student_mobile.delete(0, END)


def mobile_levea(e):
	if Student_mobile.get() == '':
		Student_mobile.insert(0, "Mobile Number")


def college_enter(e):
	Student_college.delete(0, END)


def college_levea(e):
	if Student_college.get() == '':
		Student_college.insert(0, 'College Name')


def email_enter(e):
	Student_email.delete(0, END)


def email_levea(e):
	if Student_email.get() == '':
		Student_email.insert(0, "Email")


def address_enter(e):
	Student_address.delete(0, END)


def address_levea(e):
	if Student_address.get() == '':
		Student_address.insert(0, 'Student Address')


def blood_enter(e):
	Student_blood.delete(0, END)


def blood_levea(e):
	if Student_blood.get() == '':
		Student_blood.insert(0, "Blood Group")


Student_name = Entry(level, font = ('arial', 12), bd = 0, bg = 'white', width = 27)
Student_name.place(x = 700, y = 127)
Student_name.insert(0, 'Student Name')
Student_name.bind('<FocusIn>', name_enter)
Student_name.bind('<FocusOut>', name_levea)

Student_roll = Entry(level, font = ('arial', 12), bd = 0, bg = 'white', width = 27,textvariable = roll_var)
Student_roll.place(x = 700, y = 192)
Student_roll.insert(0, 'Roll Number')
Student_roll.bind('<FocusIn>', roll_enter)
Student_roll.bind('<FocusOut>', roll_levea)

Student_reg = Entry(level, font = ('arial', 12), bd = 0, bg = 'white', width = 27,textvariable = reg_var)
Student_reg.place(x = 700, y = 257)
Student_reg.insert(0, 'Reg. Number')
Student_reg.bind('<FocusIn>', reg_enter)
Student_reg.bind('<FocusOut>', reg_levea)

Student_college = Entry(level, font = ('arial', 12), bd = 0, bg = 'white', width = 27)
Student_college.place(x = 700, y = 322)
Student_college.insert(0, 'College Name')
Student_college.bind('<FocusIn>', college_enter)
Student_college.bind('<FocusOut>', college_levea)

Student_mobile = Entry(level, font = ('arial', 12), bd = 0, bg = 'white', width = 27,textvariable = mobile_var)
Student_mobile.place(x = 700, y = 387)
Student_mobile.insert(0, 'Mobile Number')
Student_mobile.bind('<FocusIn>', mobile_enter)
Student_mobile.bind('<FocusOut>', mobile_levea)

Student_email = Entry(level, font = ('arial', 12), bd = 0, bg = 'white', width = 27,textvariable = email_var)
Student_email.place(x = 700, y = 452)
Student_email.insert(0, 'Email')
Student_email.bind('<FocusIn>', email_enter)
Student_email.bind('<FocusOut>', email_levea)




Student_blood = ttk.Combobox(level, font = ('arial', 11),width = 30)
Student_blood['value']=('A+','A-','AB+','AB-','B+','B-','O+','O-')
Student_blood.place(x = 700, y = 517)
Student_blood.set('Select Blood Group',)

Student_address = Entry(level, font = ('arial', 12), bd = 0, bg = 'white', width = 27)
Student_address.place(x = 700, y = 582)
Student_address.insert(0, 'Student Address')
Student_address.bind('<FocusIn>', address_enter)
Student_address.bind('<FocusOut>', address_levea)

im = Image.open('submit.jpg')
ima = ImageTk.PhotoImage(im)

submit_butoon = Button(level, image = ima, bd = 0, bg = 'white', fg = 'blue', activebackground = 'white',
                       command = student_database_connect)
submit_butoon.place(x = 775, y = 650)

root2.mainloop()
