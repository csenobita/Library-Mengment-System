import time
from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox

root1 = Tk()
root1.title("Book Registration")
root1.geometry("1026x770+350+50")
root1.resizable(False, False)
fream = Frame(root1, width = 1026, height = 770, border = 5)
fream.pack()

image1 = Image.open('book_reg.jpg')
image2 = ImageTk.PhotoImage(image1)
label = Label(image = image2, border = 0)
label.place(x = 0, y = 0)


def name_enter(e):
	book_name.delete(0, END)


def name_exit(e):
	if book_name.get() == '':
		book_name.insert(0, 'Book Name')


def book_id_enter(e):
	book_id.delete(0, END)


def book_id_exit(e):
	if book_id.get() == '':
		book_id.insert(0, 'Book ID')


def book_title_enter(e):
	book_title.delete(0, END)


def book_title_exit(e):
	if book_title.get() == '':
		book_title.insert(0, 'Book Title')


def book_auhter_enter(e):
	book_auhter.delete(0, END)


def book_auhter_exit(e):
	if book_auhter.get() == '':
		book_auhter.insert(0, 'Auhter Name')


def book_price_enter(e):
	book_price.delete(0, END)


def book_price_exit(e):
	if book_price.get() == '':
		book_price.insert(0, 'Book Price')

def main2():
	import main_page
def database_connect():
	global my_cursor, conn
	try:
		conn = pymysql.connect(host = 'localhost', user = 'root', password = '112233', database = 'userdata')
		my_cursor = conn.cursor()
	except:
		
		messagebox.showerror('Error', 'Database Not connecting')
	chack = 'select * from book where book_id=%s'
	my_cursor.execute(chack, (book_id.get()))
	row = my_cursor.fetchone()
	if row != None:
		messagebox.showerror('Error', 'Book ID already exists')
	
	else:
		
		qurey_insert = 'insert into book (book_name, book_id,book_title,book_auhter,book_price) values(%s,%s,%s,%s,%s)'
		my_cursor.execute(qurey_insert, (
		book_name.get(), book_id.get(), book_title.get(), book_auhter.get(), book_price.get()))
		conn.commit()
		messagebox.showinfo('success', 'Registartions successfully')
		conn.close()
		root1.destroy()
		main2()
		
		
		


book_name = Entry(label, font = ('arial', 12), bd = 0, bg = 'white', fg = 'black', width = 24)
book_name.place(x = 740, y = 151)
book_name.insert(0, 'Book Name')
book_name.bind('<FocusIn>', name_enter)
book_name.bind('<FocusOut>', name_exit)

book_id = Entry(label, font = ('arial', 12), bd = 0, bg = 'white', fg = 'black', width = 24)
book_id.place(x = 740, y = 217)
book_id.insert(0, 'Book ID')
book_id.bind('<FocusIn>', book_id_enter)
book_id.bind('<FocusOut>', book_id_exit)

book_title = Entry(label, font = ('arial', 12), bd = 0, bg = 'white', fg = 'black', width = 24)
book_title.place(x = 740, y = 284)
book_title.insert(0, 'Book Title')
book_title.bind('<FocusIn>', book_title_enter)
book_title.bind('<FocusOut>', book_title_exit)

book_auhter = Entry(label, font = ('arial', 12), bd = 0, bg = 'white', fg = 'black', width = 24)
book_auhter.place(x = 740, y = 350)
book_auhter.insert(0, 'Auhter Name')
book_auhter.bind('<FocusIn>', book_auhter_enter)
book_auhter.bind('<FocusOut>', book_auhter_exit)

book_price = Entry(label, font = ('arial', 12), bd = 0, bg = 'white', fg = 'black', width = 24)
book_price.place(x = 740, y = 416)
book_price.insert(0, 'Book Price')
book_price.bind('<FocusIn>', book_price_enter)
book_price.bind('<FocusOut>', book_price_exit)

image3 = Image.open('submit.jpg')
image4 = ImageTk.PhotoImage(image3)
sumbit_button = Button(label, image = image4, bd = 0, bg = 'white', activebackground = 'white',
                       command = database_connect)
sumbit_button.place(x = 790, y = 470)

root1.mainloop()
