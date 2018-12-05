from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#--Agrega el icono de WinDj al programa--#
import os 


class Ventana:
    def __init__(self):
        self.root = Tk()
        self.base_folder = os.path.dirname(__file__)
        self.image_path = os.path.join(self.base_folder,'djvu_icon.gif')
        self.img = PhotoImage(file = self.image_path)
        self.root.tk.call('wm','iconphoto',self.root._w, self.img)
        self.ancho = self.root.winfo_screenwidth()
        self.alto = self.root.winfo_screenheight()
        self.root.geometry(str(self.ancho) + 'x' + str(self.alto))
        self.root.configure(bg = 'white')
        self.root.title('WinDjView')
        self.addMenu()
        self.root.mainloop()
    
    def addMenu(self):
        self.bar = Menu(self.root)
        self.file = Menu(self.bar, tearoff = 0)
        self.file.add_command(label = 'Open...', accelerator = 'Ctrl+O')
        self.file.add_command(label = 'Save As...', accelerator = 'Ctrl+S')
        self.file.add_command(label = 'Close', accelerator = 'Ctrl+W')
        self.file.add_separator()
        self.file.add_command(label = 'Import Bookmarks...')
        self.file.add_command(label = 'Export Bookmarks...', state = DISABLED)
        self.file.add_command(label = 'Export Text...')
        self.file.add_command(label = 'Print...', accelerator = 'Ctrl+P')
        self.file.add_separator()
        self.file.add_command(label = 'Document Properties...')
        self.file.add_command(label = 'Settings...', accelerator = 'Ctrl+,')
        self.file.add_separator()
        self.file.add_command(label = 'Exit', accelerator = 'Ctrl+Q', command = self.root.quit)
        self.bar.add_cascade(label = 'File', menu = self.file)

        self.edit = Menu(self.bar, tearoff = 0)
        self.edit.add_command(label = 'Copy', accelerator = 'Ctrl+C', state = DISABLED)
        self.edit.add_separator()
        self.edit.add_command(label = 'Add Bookmark...')
        self.edit.add_separator()
        self.edit.add_command(label = 'Highlight Selection...', state = DISABLED)
        self.edit.add_command(label = 'Export Selection..', state = DISABLED)
        self.edit.add_separator()
        self.edit.add_command(label = 'Find', accelerator = 'Ctrl+F')
        self.bar.add_cascade(label = 'Edit', menu = self.edit)

        self.view = Menu(self.bar, tearoff = 0)
        self.view.add_command(label = 'Toolbar')
        self.view.add_command(label = 'Tab Bar')
        self.view.add_command(label = 'Status Bar')
        self.view.add_command(label = 'Sidebar')
        self.view.add_separator()
        self.view.add_command(label = 'Fullscreen', accelerator = 'Ctrl+L')
        self.view.add_separator()
        self.view.add_command(label = 'Fit Page')
        self.view.add_command(label = 'Fit Width')
        self.view.add_command(label = 'Stretch')
        self.view.add_command(label = 'Actual Size')
        self.view.add_command(label = 'Zoom')
        self.view.add_separator()
        self.view.add_command(label = 'Go To')
        self.view.add_command(label = 'Rotate')
        self.view.add_command(label = 'Layout')
        self.view.add_command(label = 'Display')
        self.view.add_separator()
        self.view.add_command(label = 'Language')
        self.bar.add_cascade(label = 'View', menu = self.view)


        self.root.config(menu = self.bar)



windj = Ventana()