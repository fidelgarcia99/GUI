from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Ventana:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap('./icons/djvu_icon.ico')
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
        self.file.add_cascade(label = 'File', menu = self.file)
        self.file.add_command(label = 'Open...', accelerator = 'Ctrl+O')
        self.file.add_command(label = 'Save As...', accelerator = 'Ctrl+S')
        self.file.add_command(label = 'Close', accelerator = 'Ctrl+W')
        self.file.add_separator()
        self.file.add_command(label = 'Import Bookmarks...')
        self.file.add_command(label = 'Export Bookmarks...')
        self.file.add_command(label = 'Export Text...')
        self.file.add_command(label = 'Print...', accelerator = 'Ctrl+P')
        self.file.add_separator()
        self.file.add_command(label = 'Document Properties...')
        self.file.add_command(label = 'Settings...', accelerator = 'Ctrl+,')
        self.file.add_separator()
        self.file.add_command(label = 'Exit', accelerator = 'Ctrl+Q', command = self.root.quit)

        self.edit = Menu(self.bar, tearoff = 0)
        self.edit.add_cascade(label = 'Edit', menu = self.edit)
        self.edit.add_command(label = 'Copy', accelerator = 'Ctrl+C')
        self.file.add_separator()
        self.edit.add_command(label = 'Add Bookmark...')
        self.file.add_separator()
        self.edit.add_command(label = 'Highlight Selection...')
        self.edit.add_command(label = 'Export Selection..')
        self.file.add_separator()
        self.edit.add_command(label = 'Find', accelerator = 'Ctrl+F')



windj = Ventana()