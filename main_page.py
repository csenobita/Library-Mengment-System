import time
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql
from tkinter import messagebox
import datetime

root5 = Tk()

root5.title("Library Menagment system")
root5.geometry('1026x770+400+100')
root5.resizable(False, False)
frame = Frame(root5, width = 1026, height = 770, bd = 12, bg = 'blue')
frame.pack()
image1 = Image.open('home2.jpg')
image2 = ImageTk.PhotoImage(image1)
label = Label(root5, image = image2, bd = 0)
label.place(x = 0, y = 0)

book_name_var = StringVar()
book_id_var = StringVar()
book_author_name_var = StringVar()


def clear():
	student_name.delete(0, END)
	student_roll.delete(0, END)
	student_reg.delete(0, END)
	student_college_name.delete(0, END)
	student_mobile.delete(0, END)
	student_address.delete(0, END)
	book_name.delete(0, END)
	book_id.delete(0, END)
	book_author_name.delete(0, END)
	book_borrowed.delete(0, END)
	book_submit.delete(0, END)
	book_return.delete(0, END)


def select_cursor(event=''):
	rows = book_detail.focus()
	contend = book_detail.item(rows)
	row = contend['values']
	book_name_var.set(row[0])
	book_id_var.set(row[1])
	book_author_name_var.set(row[2])


def conform():
	if student_name.get() == '':
		messagebox.showerror('Error', 'Student Name not found')
	elif student_roll.get() == '':
		messagebox.showerror('Error', 'Roll Number not found')
	elif student_reg.get() == '':
		messagebox.showerror('Error', 'Registration Number not found')
	elif student_college_name.get() == '':
		messagebox.showerror('Error', 'College Name not found')
	elif student_mobile.get() == "":
		messagebox.showerror('Error', 'Mobile Number not found')
	elif student_address.get() == '':
		messagebox.showerror('Error', 'Address not found')
	elif book_name.get() == '':
		messagebox.showerror('Error', 'Book Name not found')
	elif book_id.get() == '':
		messagebox.showerror('Error', 'Book ID not found')
	elif book_author_name.get() == '':
		messagebox.showerror('Error', 'Auhtor Name not found')
	elif book_return.get() == '':
		messagebox.showerror('Error', 'Return Date Fine  not found')
	else:
		try:
			conn = pymysql.connect(host = 'localhost', user = 'root', password = '112233',
			                       database = 'userdata')
			my_cursor = conn.cursor()
		except:
			messagebox.showerror('Error', 'DataBase Not connect')
			return
		qurey1 = 'select * from student where roll=%s and reg=%s'
		my_cursor.execute(qurey1, (student_roll.get(), student_reg.get()))
		row = my_cursor.fetchone()
		if row == None:
			messagebox.showerror('Error', 'Invalid Roll Number and Registration Number')
		else:
			qurey3 = ('insert into kato (name,roll ,reg, college, mobile,address,bname,bid,baname,bbor,'
			          'bsub,br) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
			my_cursor.execute(qurey3, (
				student_name.get(), student_roll.get(), student_reg.get(), student_college_name.get(),
				student_mobile.get(),
				student_address.get(), book_name.get(), book_id.get(), book_author_name.get(),
				book_borrowed.get(),
				book_submit.get(), book_return.get()))
			conn.commit()
			conn.close()
			messagebox.showinfo('Successfully', 'Book Booking Success')
			clear()


def book_reg_page():
	root5.destroy()
	
	import Book_reg


def student_reg_page():
	root5.destroy()
	import student_reg


d1 = datetime.date.today()

d2 = datetime.timedelta(7)
d3 = d1 + d2
fine = '50tk'

student_name = Entry(label, font = ('times new roman ', 12), width = 23, bd = 0, fg = 'black')
student_name.place(x = 120, y = 200)
student_roll = Entry(label, font = ('times new roman ', 12), width = 23, bd = 0, fg = 'black')
student_roll.place(x = 120, y = 265)
student_reg = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black')
student_reg.place(x = 120, y = 330)
student_college_name = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black')
student_college_name.place(x = 120, y = 396)
student_mobile = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black')
student_mobile.place(x = 120, y = 461)
student_address = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black')
student_address.place(x = 120, y = 526)

book_name = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black', textvariable = book_name_var)
book_name.place(x = 450, y = 200)
book_id = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black', textvariable = book_id_var)
book_id.place(x = 450, y = 265)
book_author_name = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black',
                         textvariable = book_author_name_var)
book_author_name.place(x = 450, y = 330)
book_borrowed = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black')
book_borrowed.insert(0, str(d1))
book_borrowed.place(x = 450, y = 396)

book_submit = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black')
book_submit.place(x = 450, y = 461)
book_submit.insert(0, str(d3))
book_return = Entry(label, font = ('times new roman', 12), width = 26, bd = 0, fg = 'black')
book_return.place(x = 450, y = 526)
book_return.insert(0, fine)

book_frame2 = Frame(label, width = 230, height = 400, relief = RIDGE, bd = 5, bg = 'white')
book_frame2.place(x = 750, y = 170)
book_frame = Frame(book_frame2, width = 230, height = 400, relief = RIDGE, bd = 0, bg = 'white')
book_frame.place(x = 5, y = 5)


def book_input():
	conn = pymysql.connect(host = 'localhost', user = 'root', password = '112233', database = 'userdata')
	qurey = 'select book_name,book_id ,book_auhter from book '
	my_cursor = conn.cursor()
	my_cursor.execute(qurey)
	rows = my_cursor.fetchall()
	if len(rows) != 0:
		book_detail.delete(*book_detail.get_children())
		for row in rows:
			book_detail.insert("", END, values = row)
		conn.commit()
	conn.close()


book_detail = ttk.Treeview(book_frame, columns = ('book_name', 'book_id', 'book_auhter'))
book_detail.heading('book_name', text = 'Book Name')
book_detail.heading('book_id', text = 'Book ID')
book_detail.heading('book_auhter', text = 'Book Author')
book_detail['show'] = 'headings'
book_detail.pack(fill = BOTH, expand = 1, )
book_detail.column('book_id', width = 100)
book_detail.column('book_name', width = 100)
book_detail.column('book_auhter', width = 100)
book_detail.bind('<ButtonRelease-1>', select_cursor)
book_input()

confirmed_button = Button(label, text = 'conform', bg = 'white', fg = 'green', command = conform)
confirmed_button.place(x = 370, y = 600)

student_reg_button = Button(label, text = 'Student Registration', bg = '#987585', fg = '#124567', bd = 0,
                            font = ('arial', 10), command = student_reg_page)
student_reg_button.place(x = 885, y = 50)
book_reg_button = Button(label, text = 'Book Registration', bg = '#987685', fg = '#124567', bd = 0,
                         font = ('arial', 10), command = book_reg_page)
book_reg_button.place(x = 900, y = 80)

root5.mainloop()
