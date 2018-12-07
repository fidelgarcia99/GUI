from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import *
# --Libreria que agrega el icono de WinDj al programa-- #
import os 


class Ventana:
    def __init__(self):
        self.root = Tk()
        self.base_folder = os.path.dirname(__file__)
        self.image_path = os.path.join(self.base_folder, 'djvu_icon.gif')
        self.img = PhotoImage(file=self.image_path)
        self.root.tk.call('wm', 'iconphoto', self.root._w, self.img)
        # Elementos de la ventana
        self.bar = Menu(self.root)
        self.file = Menu(self.bar, tearoff=0)
        self.edit = Menu(self.bar, tearoff=0)
        self.view = Menu(self.bar, tearoff=0)
        self.tools = Menu(self.bar, tearoff=0)
        self.window = Menu(self.bar, tearoff=0)
        self.help = Menu(self.bar, tearoff=0)
        self.submenuview = Menu(self.view, tearoff=0)
        # Geometria
        self.ancho = self.root.winfo_screenwidth()
        self.alto = self.root.winfo_screenheight()
        self.root.geometry(str(self.ancho) + 'x' + str(self.alto))
        self.root.configure(bg='dark grey')
        self.root.title('WinDjView')
        self.add_menu()
        self.interior()
        self.root.mainloop()
    
    def add_menu(self):
        # ---Barra File--- #
        self.file.add_command(label='Open...', accelerator='Ctrl+O')
        self.file.add_command(label='Save As...', accelerator='Ctrl+S')
        self.file.add_command(label='Close', accelerator='Ctrl+W')
        self.file.add_separator()
        self.file.add_command(label='Import Bookmarks...')
        self.file.add_command(label='Export Bookmarks...', state=DISABLED)
        self.file.add_command(label='Export Text...')
        self.file.add_command(label='Print...', accelerator='Ctrl+P')
        self.file.add_separator()
        self.file.add_command(label='Document Properties...')
        self.file.add_command(label='Settings...', accelerator='Ctrl+,')
        self.file.add_separator()
        self.file.add_command(label='Exit', accelerator='Ctrl+Q', command=self.root.quit)
        self.bar.add_cascade(label='File', men=self.file)

        # ---Barra de Edit--- #
        self.edit.add_command(label='Copy', accelerator='Ctrl+C', state=DISABLED)
        self.edit.add_separator()
        self.edit.add_command(label='Add Bookmark...')
        self.edit.add_separator()
        self.edit.add_command(label='Highlight Selection...', state=DISABLED)
        self.edit.add_command(label='Export Selection..', state=DISABLED)
        self.edit.add_separator()
        self.edit.add_command(label='Find', accelerator='Ctrl+F')
        self.bar.add_cascade(label='Edit', menu=self.edit)

        # ---Barra de View--- #
        self.view.add_command(label='Toolbar')
        self.view.add_command(label='Tab Bar')
        self.view.add_command(label='Status Bar')
        self.view.add_command(label='Sidebar')
        self.view.add_separator()
        self.view.add_command(label='Fullscreen', accelerator='Ctrl+L')
        self.view.add_separator()
        self.view.add_command(label='Fit Page')
        self.view.add_command(label='Fit Width')
        self.view.add_command(label='Stretch')
        self.view.add_command(label='Actual Size')

        # ---Submenu de Zoom--- #
        self.submenuview.add_command(label='Zoom In', accelerator='Ctrl+plus')
        self.submenuview.add_command(label='Zoom Out', accelerator='Ctrl+minus')
        self.submenuview.add_separator()
        self.submenuview.add_command(label='50%')
        self.submenuview.add_command(label='75%')
        self.submenuview.add_command(label='100%', accelerator='Ctrl+I')
        self.submenuview.add_command(label='200%')
        self.submenuview.add_command(label='400%')
        self.submenuview.add_separator()
        self.submenuview.add_command(label='Custom...', accelerator='Crtl+M')
        self.submenuview.add_cascade(label='Zoom', menu=self.submenuview)

        self.view.add_separator()
        self.view.add_command(label='Go To')
        self.view.add_command(label='Rotate')
        self.view.add_command(label='Layout')
        self.view.add_command(label='Display')
        self.view.add_separator()
        self.view.add_command(label='Language')
        self.bar.add_cascade(label='View', menu=self.view)

        # ---Barra de Tools--- #
        self.tools.add_command(label='Hand Tool')
        self.tools.add_command(label='Select Tool')
        self.tools.add_command(label='Rectangle Tool')
        self.tools.add_command(label='Magnifying Glass')
        self.tools.add_command(label='Marquee Zoom')
        self.bar.add_cascade(label='Tools', menu=self.tools)

        # ---Barra de Window--- #
        self.window.add_command(label='Fullscreen', accelerator='Ctrl+L')
        self.window.add_separator()
        self.bar.add_cascade(label='Window', menu=self.window)

        # ---Barra de Help--- #
        self.help.add_command(label='Check for updates...')
        self.help.add_command(label='About WinDjView...', command=self.__about)
        self.bar.add_cascade(label='Help', menu=self.help)
        self.root.config(menu=self.bar)

    def __about(self):
        self.about = Toplevel()
        self.base_folder = os.path.dirname(__file__)
        self.image_path = os.path.join(self.base_folder, 'djvu_icon.gif')
        self.logo = PhotoImage(file=self.image_path)
        self.about.tk.call('wm', 'iconphoto', self.about._w, self.logo)
        self.about.geometry('400x300')
        self.about.configure(bg='grey')
        self.about.title('About WinDjView')
        self.about.mainloop()

    def interior(self):
        ancho = self.ancho
        alto = self.alto
        frame1 = Frame(self.root)
        frame1.configure(width=ancho * 0.147, height=alto*0.855)
        frame1.grid(row=0, column=0, padx=(ancho * 0.01, ancho * 0.003), pady=(alto * 0.01, alto * 0))
        frame1.grid_propagate(False)

        frame2 = Frame(self.root)
        frame2.configure(width=ancho * 0.827, height=alto*0.855)
        frame2.grid(row=0, column=1, padx=(ancho * 0.003, ancho * 0.01), pady=(alto * 0.01, alto * 0))
        frame2.grid_propagate(False)

        frame3 = Frame(self.root)
        frame3.configure(width=ancho, height=alto*0.02)
        frame3.grid(row=1, column=0, columnspan=2, padx=(ancho * 0, ancho * 0), pady=(alto * 0, alto * 0))
        frame3.grid_propagate(False)

        etiqueta1 = Label(frame3, text="Ready")
        etiqueta1.grid(row=0, column=0, padx=(0, ancho*0.82))

        etiqueta2 = Label(frame3, text="Page 2 of 2        27.94 x 21.59 cm")
        etiqueta2.grid(row=0, column=1)


'''
'''

windj = Ventana()
