from tkinter import *
import tkinter.filedialog

def about(*args):
    root2=Tk()
    root2.title('About')
    root2.geometry('200x40')
    frame2 = Frame(root2)
    frame2.grid()
    lab4 = Label(frame2, text = "Simple contact list manager")
    lab4.grid(row = 0, sticky = W)

def add_data(*args):
    
    def massage(*args):
        text.config(state = 'normal')
        txt = ent.get()
        txt2 = ent2.get()
        txt3 = text2.get('0.0', END)
        sps = '\t\t'
        data = ' '*10 + txt + sps + ' '*19 + txt2 +sps+'\t' + ' '*13 + txt3
        text.insert(END, data)
        root3.destroy()
        text.config(state = 'disable')
            
    root3 = Tk()
    root3.title('Adding new data')
    root3.geometry('565x415')
    root3.minsize(565, 415)
    frame3 = Frame(root3)
    frame3.grid()
    lab5 = Label(frame3, text = "Enter name:")
    lab5.grid(row = 0, column = 2)
    lab6 = Label(frame3, text = "Adress:")
    lab6.grid(row = 1, column = 2)
    ent = Entry(frame3, width = 20)
    ent.grid(row = 0, column = 6)
    ent2 = Entry(frame3, width = 20)
    ent2.grid(row = 1, column = 6)
    lab7 = Label(frame3, text = "Comment:")
    lab7.grid(row = 2, column = 5)
    text2 = Text(frame3, width = 70, height = 20)
    text2.grid(row = 3, column = 0, columnspan = 10, sticky = W)
    bttn2 = Button(frame3, text = "Ok", bg = 'green', command = massage)
    bttn2.grid(row = 4, column = 3)
    bttn2 = Button(frame3, text = "Cancel", bg = 'red', command = root3.destroy)
    bttn2.grid(row = 4, column = 6)

def new_file():
    text.delete('1.0', 'end')
    text.config(state = 'normal')
def open_file(*args):
    text.config(state = 'normal')
    fn = tkinter.filedialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    text.delete('1.0', 'end') 
    text.insert('1.0', open(fn, 'rt').read())
    text.config(state = 'disable')
        
def save_file(*args):
    fn = tkinter.filedialog.SaveAs(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn+=".txt"
    open(fn, 'wt').write(text.get('1.0', 'end'))

   

# main window root
root = Tk()
root.title('Contact list')

# frame in root
frame = Frame(root)
frame.grid()

lab1 = Label(frame, text = "Name", font = "arial 16")
lab1.grid(row = 0, column = 1)

lab2 = Label(frame, text = "Adress", font = "arial 16")
lab2.grid(row = 0, column = 5)

lab3 = Label(frame, text = "Comment", font = "arial 16")
lab3.grid(row = 0, column = 9)

# Text field in root
text = Text(frame, width = 60, height = 12, bg = '#40e0d0', font='Arial 16', wrap = WORD)

text.grid(row = 1, column = 0, columnspan = 11, sticky = W)


bttn1 = Button(frame, text = "add data", font='Arial 10', command = add_data)
bttn1.grid(row = 2, column = 5)


# menu appearance in root
main_menu = Menu(root)  
filemenu = Menu(main_menu, tearoff = 0)
filemenu.add_command(label = "New", command = new_file)
filemenu.add_command(label = "Open...", command = open_file)
filemenu.add_command(label = "Save", command = save_file)
filemenu.add_separator()  # split menu
filemenu.add_command(label = "Exit", command = root.destroy)

main_menu.add_cascade(menu = filemenu, label = "File")

helpmenu = Menu(main_menu, tearoff = 0)
helpmenu.add_command(label = "About", command = about)
main_menu.add_cascade(menu = helpmenu, label = "Help" )

root.config(menu = main_menu)
root.maxsize(1200, 750)




root.mainloop()
