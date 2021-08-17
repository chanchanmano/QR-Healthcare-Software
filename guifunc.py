from tkinter import *
from tkinter import messagebox
from qrcodegen import qrscan
from sqlpack import sql

accesscode=''
def selecttablegui(aadharnum):


    # this is a function to get the selected list box value
    def getListboxValue():
        itemSelected = tablelistbox.curselection()
        return itemSelected

    # this is a function to get the user input from the text input box
    def getInputBoxValue():
        userInput = retrievalpassword.get()
        return userInput

    # this is the function called when the button is clicked
    def btnClickFunction():
        tableselected = getListboxValue()
        tableselected = str(tableselected[0])
        print(tableselected)
        retrievalpassword = str(getInputBoxValue())
        checkifrright = sql.check_mrpass(retrievalpassword,accesscode)
        if checkifrright:
            datadisplgui(aadharnum,tableselected)


    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('540x480')
    root.configure(background='#F0F8FF')
    root.title('Apollo Systems')


    # This is the section of code which creates a listbox
    tablelistbox = Listbox(root, bg='#F0F8FF', font=('arial', 12, 'normal'), width=0, height=0)
    tablelistbox.insert('0', 'Patient')
    tablelistbox.insert('1', 'General Medical Information')
    tablelistbox.insert('2', 'Known Allergies')
    tablelistbox.insert('3', 'Deficiencies')
    tablelistbox.insert('4', 'Vaccinations')
    tablelistbox.insert('5', 'Previous Surgeries')
    tablelistbox.insert('6', 'Medical Conditions')
    tablelistbox.insert('7', 'Treatments')
    tablelistbox.insert('8', 'Remarks')
    tablelistbox.place(x=164, y=138)

    # This is the section of code which creates the a label
    Label(root, text='Enter Retrieval Password:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=174, y=48)

    # This is the section of code which creates a text input box
    retrievalpassword = Entry(root)
    retrievalpassword.place(x=194, y=78)

    # This is the section of code which creates the a label
    Label(root, text='Select the Table to Retrieve From', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=154,
                                                                                                            y=108)

    # This is the section of code which creates a button
    Button(root, text='Retrieve Data', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(
        x=204, y=348)

    root.mainloop()



def scanqrgui():

    def info():
        messagebox.showinfo("Apollo Systems","This window enables the scanner")


    # this is the function called when the button is clicked
    def scanqrbtnfunc():
        aadharnum = qrscan.qrscanner()
        if len(aadharnum) > 1:
            checker = sql.check_valueID(aadharnum)
            if checker:
                selecttablegui(aadharnum)
            else:
                messagebox.showerror("Apollo Systems", "NO SUCH PATIENT EXISTS!")

    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('320x220')
    root.configure(background='#F0F8FF')
    root.title('Apollo Systems')

    def areyousure():
        ask = messagebox.askyesno("Apollo Systems","Are you sure you want to quit")
        if ask == True:
            root.quit()
        else:
            pass
    menubar = Menu(root)
    menubar.add_command(label="Info", command=info)
    menubar.add_command(label="Quit", command=areyousure)
    root.config(menu=menubar)
    # This is the section of code which creates a button
    Button(root, text='Scan QR', bg='#F0F8FF', font=('arial', 22, 'normal'), command=scanqrbtnfunc).place(x=76, y=77)

    root.mainloop()


def datadisplgui(key,tableselected):


    def info():
        messagebox.showinfo("Apollo Systems", "This window requires you to enter the Retrieval Password\n Select the table from which the information is to be retreived\n from the listbox provided\n")
    lrec = sql.retreivalmgui(tableselected,key)
    tablelabel= sql.ltable[int(tableselected)]
    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('900x900')
    root.configure(background='#F0F8FF')
    root.title('Apollo Systems')

    menubar = Menu(root)
    menubar.add_command(label="Info", command=info)
    menubar.add_command(label="Quit", command=root.quit)
    root.config(menu=menubar)
    # This is the section of code which creates the a label
    Label(root, text=tablelabel, bg='#F0F8FF', font=('arial', 18, 'normal')).place(x=391, y=13)
    a = 50
    for i in range(len(lrec)):
        # This is the section of code which creates the a label
        Label(root, text=lrec[i], bg='#F0F8FF', font=('arial', 10, 'normal')).place(x=121, y=63+a)
        a += 50


    root.mainloop()

