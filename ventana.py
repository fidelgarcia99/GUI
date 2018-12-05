from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import *

#--Libreria que grega el icono de WinDj al programa--#
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
        self.root.configure(bg = 'dark grey')
        self.root.title('WinDjView')
        self.addMenu()
        self.root.mainloop()
    
    def addMenu(self):
        self.bar = Menu(self.root)

        #---Barra File---#
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

        #---Barra de Edit---#
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

        #---Barra de View---#
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

        #---Submenu de Zoom---#
        self.submenuview = Menu(self.view, tearoff = 0)
        self.submenuview.add_command(label = 'Zoom In', accelerator = 'Ctrl+plus')
        self.submenuview.add_command(label = 'Zoom Out', accelerator = 'Ctrl+minus')
        self.submenuview.add_separator()
        self.submenuview.add_command(label = '50%')
        self.submenuview.add_command(label = '75%')
        self.submenuview.add_command(label = '100%', accelerator = 'Ctrl+I')
        self.submenuview.add_command(label = '200%')
        self.submenuview.add_command(label = '400%')
        self.submenuview.add_separator()
        self.submenuview.add_command(label = 'Custom...', accelerator = 'Crtl+M')
        self.submenuview.add_cascade(label = 'Zoom', menu = self.submenuview)

        self.view.add_separator()
        self.view.add_command(label = 'Go To')
        self.view.add_command(label = 'Rotate')
        self.view.add_command(label = 'Layout')
        self.view.add_command(label = 'Display')
        self.view.add_separator()
        self.view.add_command(label = 'Language')
        self.bar.add_cascade(label = 'View', menu = self.view)

        #---Barra de Tools---#
        self.tools = Menu(self.bar, tearoff = 0)
        self.tools.add_command(label = 'Hand Tool')
        self.tools.add_command(label = 'Select Tool')
        self.tools.add_command(label = 'Rectangle Tool')
        self.tools.add_command(label = 'Magnifying Glass')
        self.tools.add_command(label = 'Marquee Zoom')
        self.bar.add_cascade(label = 'Tools', menu = self.tools)

        #---Barra de Window---#
        self.window = Menu(self.bar, tearoff = 0)
        self.window.add_command(label = 'Fullscreen', accelerator = 'Ctrl+L')
        self.window.add_separator()
        self.bar.add_cascade(label = 'Window', menu = self.window)

        #---Barra de Help---#
        self.help = Menu(self.bar, tearoff = 0)
        self.help.add_command(label = 'Check for updates...')
        self.help.add_command(label = 'About WinDjView...', command = self.__about)
        self.bar.add_cascade(label = 'Help', menu = self.help)

        self.root.config(menu = self.bar)
    
    def __about(self):
        self.about = Toplevel()
        self.base_folder = os.path.dirname(__file__)
        self.image_path = os.path.join(self.base_folder,'djvu_icon.gif')
        self.logo = PhotoImage(file = self.image_path)
        self.about.tk.call('wm','iconphoto',self.about._w, self.logo)
        self.about.geometry('400x300')
        self.about.configure(bg = 'grey')
        self.about.title('About WinDjView')


        self.about.mainloop()




windj = Ventana()