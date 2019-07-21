from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
from sqlite3 import Error

def sql_con(dbname):
    try:
        con = sqlite3.connect(dbname)
        return con
    except (Error) as e:
        print(e)

def sql_table(con):

    cur = con.cursor()
    add = '''CREATE TABLE IF NOT EXISTS members (
    id integer primary Key AUTOINCREMENT,
    firstname text,
    lastname text,
    phone integer,
    username text,
    password text,
    Unique(username))
            '''   
    cur.execute(add)
    
    con.commit()


    
def add_data(con, data):
    cur = con.cursor()
    cur.execute('INSERT INTO members(`firstname`, `lastname`, `phone`, `username`, `password`) VALUES (?, ?, ?, ?, ?)',data)
    con.commit()
    
def user_log(con, data):
    cur =  con.cursor()
    cur.execute('SELECT * FROM members WHERE username == ? and password == ?', data)
    res = cur.fetchone()[1]
    Label(scr1, text=res).pack()

def log():
    con = sql_con('mydata.db')
    user_info = username.get()
    passw = password.get()
    dataa = (user_info, passw)
    user_log(con ,dataa)
    
    
def dele():
    fname_entry.delete(0, END)
    name_entry.delete(0, END)
    tel_entry.delete(0, END)
    user_entry.delete(0, END)
    pass_entry.delete(0, END)

def reg_data():
    fname_entry_info = firstname.get()
    lname_entry_info = lastname.get()
    tel_entry_info = phone.get()
    user_entry_info = username.get()
    pass_entry_info = password1.get()
    #pass2_entry = password2.get()
    
    if firstname.get()=='' or lastname.get()=='' or phone.get()=='' or username.get()=='' or password1.get() == '':
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    
    else:
    
        user_info = (fname_entry_info, lname_entry_info, tel_entry_info, user_entry_info, pass_entry_info)
        con = sql_con('mydata.db')
        sql_table(con)
        add_data(con, user_info)
        dele()
        
        Label(scr, text = 'Successfully registered', fg='red').pack()
def login():
    global scr1
    scr1 = Toplevel(top)
    scr1.title('login')
    scr1.geometry('300x300')
    global username
    global password
    global usern_entry
    global pass_entry
    
    username= StringVar()
    password = StringVar()
    
    Label(scr1,text='Please Enter details to login').pack()
    Label(scr1,text='').pack()
    Label(scr1,text='Username').pack()
    usern_entry = Entry(scr1,textvariable=username).pack()
    Label(scr1, text='').pack()
    Label(scr1, text='Password').pack()
    pass_entry = Entry(scr1, textvariable=password, show='*').pack()
    Label(scr1, text='').pack()
    Button(scr1, text='LOGIN',command=log, width=10, height=2).pack()
    
def register():
    global firstname
    global lastname
    global phone
    global username
    global password1
    #global password2
    
    global fname_entry
    global lname_entry
    global tel_entry
    global user_entry
    global pass_entry
    #global pass2_entry
    global scr
    scr = Toplevel(top)
    scr.title("register")
    scr.geometry('500x500')
    firstname = StringVar()
    lastname =  StringVar()
    phone = IntVar()
    username= StringVar()
    password1 = StringVar()
    #password2 = StringVar()
    
    Label(scr,text='Please Enter details to register').pack()
    Label(scr,text='').pack()
    Label(scr, text='Firstname').pack()
    fname_entry = Entry(scr, textvariable=firstname).pack()
    Label(scr, text='').pack()
    Label(scr, text='Lastname').pack()
    lname_entry = Entry(scr, textvariable=lastname).pack()
    Label(scr, text='').pack()
    Label(scr, text='Phone Number').pack()
    tel_entry = Entry(scr, textvariable=phone).pack()
    Label(scr, text='').pack()
    Label(scr,text='Username').pack()
    user_entry = Entry(scr,textvariable=username).pack()
    Label(scr, text='').pack()
    Label(scr, text='Password').pack()
    pass_entry = Entry(scr, textvariable=password1, show='*').pack()
    Label(scr, text='').pack()
    #Label(scr, text='Confirm Password').pack()
    #pass2_entry = Entry(scr, textvariable=password2, show='*').pack()
    #Label(scr, text='').pack()
    Button(scr, text='REGISTER',command = reg_data, width = 10, height=2).pack()
    

def main_screen():
    global top
    top = Tk()
    top.geometry('300x300')
    lab1 =  Label(text='Test 1.0', bg='grey', fg='green', width=20, height=5, font=('arial', 15))
    lab1.pack()
    Label(text='').pack()
    but1 = Button(text='Register',command=register, width=30, height=2)
    but1.pack()
    Label(text='').pack()
    but2 = Button(text='Login',command=login, width=30, height=2)
    but2.pack()
    
    top.mainloop()
    
if __name__ == "__main__":
    main_screen()
    
