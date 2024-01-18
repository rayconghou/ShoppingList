from tkinter import *
from tkinter import messagebox
import json

def autosave():

    with open('shopping_list.json', 'w') as f:

        shopping_list = list(listboxvalues.get())
        s = json.dumps(shopping_list)
        f.write(s)

def load():

    with open('shopping_list.json', 'r') as f:

        contents = f.read()
        shopping_list = json.loads(contents)

        for item in shopping_list:
            listbox.insert('end', item)

window = Tk()
window.title('Shopping List')
window.geometry('350x350')


listboxvalues = Variable([])

listbox = Listbox(window, width=32, listvariable=listboxvalues)

listbox.grid(row=0, column=0)


addEntryBox = Entry(window)
addEntryBox.configure(width=20)
addEntryBox.grid(row=1, column=0)

def addItem():
    
    item = addEntryBox.get()
    listbox.insert('end', item)

    autosave()

addItemButton = Button(window, text='Add Item',
                       command=addItem)

addItemButton.grid(row=2, column=0)
addItemButton.configure(width=35)


def removeItem():

    selecteditems = list(listbox.curselection())

    if len(selecteditems) > 0:

        i = selecteditems[0]
        listbox.delete(str(i))

    autosave()

removeItemButton = Button(window, text='Remove Item',
                          command=removeItem)

removeItemButton.grid(row=3, column=0)
removeItemButton.configure(width=35)


def clearList():

    ok = messagebox.askokcancel(title='Clear list?',
                                message='Click on OK to clear the list, or' \
                                + ' Cancel to keep items')

    if ok:
        listbox.delete('0', 'end')

    autosave()

clearListButton = Button(window, text='Clear List',
                         command=clearList)

clearListButton.grid(row=4, column=0)
clearListButton.configure(width=35)
    
load()

window.mainloop()
