from tkinter import Menu


class MenuBar:
    def __init__(self, master):
        master.option_add('*tearOff', False)
        menubar = Menu(master)
        master.config(menu=menubar)
        file = Menu(menubar)
        edit = Menu(menubar)
        help_ = Menu(menubar)
        menubar.add_cascade(menu=file, label='File')
        menubar.add_cascade(menu=edit, label='Edit')
        menubar.add_cascade(menu=help_, label='Help')
        file.add_command(label="New", command=lambda: print("New File"))
        file.entryconfig('New', accelerator='CTRL + N')

        save = Menu(file)
        file.add_cascade(menu=save, label="Save")
        save.add_command(label="Save As", command=lambda: print("Saving as..."))
        save.add_command(label="Save In", command=lambda: print("Saving in..."))