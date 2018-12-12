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
        self.view.add_cascade(label = 'Zoom', menu = self.submenuview)

        self.view.add_separator()
        #----Submenu de Go To----#
        self.submenuview1 = Menu(self.view, tearoff = 0)
        self.submenuview1.add_command(label = 'First Page', accelerator = 'Ctrl+Home')
        self.submenuview1.add_command(label = 'Previous Page', accelerator = 'Ctrl+PgUp')
        self.submenuview1.add_command(label = 'Next Page', accelerator = 'Ctrl+PgDown')
        self.submenuview1.add_command(label = 'Last Page', accelerator = 'Ctrl+End')
        self.submenuview1.add_command(label = 'Page...', accelerator = 'Ctrl+G')
        self.submenuview1.add_separator()
        self.submenuview1.add_command(label = 'Previous View', accelerator = 'Alt + Left Arrow')
        self.submenuview1.add_command(label = 'Next View', accelerator = 'Alt + Right Arrow', state = DISABLED)
        self.view.add_cascade(label = 'Go To', menu = self.submenuview1)

        #----Submenu de Rotate----#
        self.submenuview2 = Menu(self.view, tearoff = 0)
        self.submenuview2.add_command(label = 'Left', accelerator = 'Ctrl+Shift+LeftArrow')
        self.submenuview2.add_command(label = 'Right', accelerator = 'Ctrl+Shift+RightArrow')
        self.submenuview2.add_command(label = "180º", accelerator = 'Ctrl+Shift+DownArrow')
        self.view.add_cascade(label = 'Rotate', menu = self.submenuview2)

        #----Submenu de Layout----#
        self.submenuview3 = Menu(self.view, tearoff = 0)
        self.submenuview3.add_checkbutton(label = 'Continuous', onvalue = 1, offvalue = 0, accelerator = 'Ctrl+Alt+1')
        self.submenuview3.add_checkbutton(label = 'Facing Pages', onvalue = 1, offvalue = 0, accelerator = 'Ctrl+Alt+2')
        self.submenuview3.add_separator()
        self.submenuview3.add_checkbutton(label = 'First Page Alone', onvalue = 1, offvalue = 0, accelerator = 'Ctrl+E')
        self.submenuview3.add_checkbutton(label = 'Right-to-left Order', onvalue = 1, offvalue = 0, accelerator = 'Ctrl+R')
        self.view.add_cascade(label = 'Layout', menu = self.submenuview3)

        #----Submenu de Display----#
        self.submenuview4 = Menu(self.view, tearoff = 0)
        self.submenuview4.add_checkbutton(label = 'Color', onvalue = 1, offvalue = 0, accelerator = 'Ctrl+Shift+1')
        self.submenuview4.add_checkbutton(label = 'Black & White', onvalue = 1, offvalue = 0, accelerator = 'Ctrl+Shift+2')
        self.submenuview4.add_checkbutton(label = 'Background', onvalue = 1, offvalue = 0, accelerator = 'Ctrl+Shift+3')
        self.submenuview4.add_checkbutton(label = 'Foreground', onvalue = 1, offvalue = 0, accelerator = 'Ctrl+Shift+4')
        self.view.add_cascade(label = 'Display', menu = self.submenuview4)
        
        self.view.add_separator()
        #----Submenu de Language----#
        self.submenuview5 = Menu(self.view, tearoff = 0)
        self.submenuview5.add_checkbutton(label = 'English', onvalue = 1, offvalue = 0)
        self.view.add_cascade(label = 'Language', menu = self.submenuview5)
        
        self.bar.add_cascade(label = 'View', menu = self.view)

        #---Barra de Tools---#
        self.tools = Menu(self.bar, tearoff = 0)
        self.tools.add_checkbutton(label = 'Hand Tool', onvalue = 1, offvalue = 0)
        self.tools.add_checkbutton(label = 'Select Tool', onvalue = 1, offvalue = 0)
        self.tools.add_checkbutton(label = 'Rectangle Tool', onvalue = 1, offvalue = 0)
        self.tools.add_checkbutton(label = 'Magnifying Glass', onvalue = 1, offvalue = 0)
        self.tools.add_checkbutton(label = 'Marquee Zoom', onvalue = 1, offvalue = 0)
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
        self.about.geometry('390x290')
        self.about.configure(bg = 'light grey')
        self.about.title('About WinDjView')

        #---Abre el archivo que contiene el logo del about---#
        self.image_path2 = os.path.join(self.base_folder,'djvu_iconabout.gif')
        self.logoabout = PhotoImage(file = self.image_path2)
        self.labellogo = Label(self.about, image = self.logoabout)
        self.labellogo.grid(row = 0, column = 0)
        
        self.labelabout = Label(self.about, text = 'WinDJView 2.1', font = ('Helvetica', '9'))
        self.labelabout.grid(row = 1, column = 0)
        
        self.copyrights = 'Copyright © 2004-2015 Andrew Zhezherun' + '\n' + 'Copyright © 2012-2015 Leonid Zhezherun'
        self.labelCR = Label(self.about, text = self.copyrights, font = ('Helvetica', '8'))
        self.labelCR.grid(row = 2, column = 0)

        self.links = 'Project homepage: https://windjview.sourceforge.io/' + '\n' + 'DjVuLibre homepage: http://djvu.sourceforge.net/'
        self.labellinks = Label(self.about, text = self.links, font = ('Helvetica', '7'))
        self.labellinks.grid(row = 3, column = 0)

        self.text = "This program is free software; you can redistribute it and/or modify under the terms of the" + '\n' + "GNU General Public License as published by the Free Software Foundation; either version 2" + '\n' + "of the License, or (at you opinion) any later version."
        self.labelabout1 = Label(self.about, text = self.text, font = ('Helvetica', '7'))
        self.labelabout1.grid(row = 4, column = 0)

        self.text2 = "You can support further development of this program by donating through PayPal."
        self.labelabout2 = Label(self.about, text = self.text2 , font = ('Helvetica', '7'))
        self.labelabout2.grid(row = 5, column = 0)

        self.button = Button(self.about, text = 'Close', command = self.about.destroy)
        self.button.grid(row = 6, column=0)
                
        self.about.mainloop()



windj = Ventana()