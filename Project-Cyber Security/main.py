from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb


#Frame
win = Tk()
win.geometry('700x480')
win.config(bg='black')

#Button Function
def open_img():
    #open file directory
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select File type',
                                           filetypes=(('PNG file', '*.png') ,('JPG file', '*.jpg'),
                                                      ('All file','*.txt')))

    #image Select
    img = Image.open(open_file)
    img = ImageTk.PhotoImage(img)

    lf1.config(image=img)
    lf1.image=img

def hide():
    global hide_msg
    password = code.get()
    if password == '12345':
        msg = lf2.get(1.0,END)
        hide_msg = lsb.hide(str(open_file),msg)
        messagebox.showinfo('Success', 'Your Msg is sucessfully hidden in image, please save your image')

    elif password == '':
        messagebox.showerror('Error','Please Enter Secret key')
    else:
        messagebox.showerror('Error','Wrong Secret key')
        code.set('')

def save_img():
    hide_msg.save('Secret file.png')
    messagebox.showinfo(('save','Image has been sucessfully saved'))

def show():
    password = code.get()
    if password == '12345':
        show_msg = lsb.reveal(open_file)
        lf2.delete(1.0,END)
        lf2.insert(END,show_msg)

    elif password == '':
        messagebox.showerror('Error','Please Enter Secret key')
    else:
        messagebox.showerror('Error','Wrong Secret key')
        code.set('')

#logo
logo = PhotoImage(file='')
Label(win,image=logo, bd=0, ).place(x=190, y=0)


#Heading
Label(win, text='Stegnography' ,font='impack 40 bold' , bg='black', fg='red').place(x=220,y=12)

#Frame 1
f1 = Frame(win, width=250, height=220, bd=5, bg='white')
f1.place(x=50, y=100)
lf1 = Label(f1, bg='blue')
lf1.place(x=0,y=0)


#Frame 2
f2 = Frame(win, width=320, height=220, bd=5, bg='white')
f2.place(x=330, y=100)
lf2 = Text(f2, font='ariel 15 bold',wrap=WORD, )
lf2.place(x=0,y=0, width=310, height=200)

#label for secret key
Label(win, text='Enter Secret key', font='10', bg='black', fg='yellow').place(x=270,y=330)

#Enter widget for secret key
code = StringVar()
e = Entry(win,textvariable=code , bd=2, font='imapct 10 bold ',show='*').place(x=245, y=360)

#Buttons
open_button = Button(win,text='Open Image', bg='blue', fg='white', font='ariel 12 bold ', cursor='hand2', command=open_img).place(x=60, y=417)

save_button = Button(win,text='Save Image', bg='green', fg='white', font='ariel 12 bold ', cursor='hand2', command=save_img).place(x=190, y=417)

hide_button = Button(win,text='Hide Data', bg='red', fg='white', font='ariel 12 bold ', cursor='hand2', command=hide).place(x=380, y=417)

show_button = Button(win,text='Show Data', bg='orange', fg='white', font='ariel 12 bold ', cursor='hand2', command=show).place(x=510, y=417)

mainloop()
