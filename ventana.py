from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from PIL import *


#--Libreria que agrega el icono de WinDj al programa--#
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
        self.addMenuIcons()
        self.interior()
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

    def getIconos(self):
      iconos = []
      #Accede a la carpeta icons y obtiene el directorio, los subdirectorios y los archivos en ella
      dir, subdir,archivos = next(os.walk('./icons'))
      #Convertimos los archivos a formato de imagen para ser usados
      for archivo in archivos:
          image_path = os.path.join(dir,archivo)
          im = Image.open(image_path)
          icon = ImageTk.PhotoImage(im)
          iconos.append(icon)
      return iconos

    def addMenuIcons(self):
        self.icons = self.getIconos()
        self.frame_barra = Frame(self.root, bg = '#c8d6e5', bd=2, relief = GROOVE)
        self.frame_barra.configure( width = self.ancho, height = 32)
        self.frame_barra.grid_propagate(False)
        ############################# Barra de Herramientas ################################
        self.btn_open = Button(self.frame_barra, image=self.icons[16], bd = 0, bg = '#c8d6e5')
        self.btn_open.grid(row = 0, column = 0, padx= (2,2), pady=(1,1))

        self.sep1 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep1.grid(row = 0, column = 1, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_print = Button(self.frame_barra, image=self.icons[10], bd = 0, bg = '#c8d6e5')
        self.btn_print.grid(row = 0, column = 2, padx= (2,2), pady=(1,1))
        self.btn_bin = Button(self.frame_barra, image=self.icons[2], bd = 0, bg = '#c8d6e5')
        self.btn_bin.grid(row = 0, column = 3, padx= (2,2), pady=(1,1))
        self.btn_info = Button(self.frame_barra, image=self.icons[11], bd = 0, bg = '#c8d6e5')
        self.btn_info.grid(row = 0, column = 4, padx= (2,2), pady=(1,1))

        self.sep2 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep2.grid(row = 0, column = 5, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_hand = Button(self.frame_barra, image=self.icons[0], bd = 0, bg = '#c8d6e5')
        self.btn_hand.grid(row = 0, column = 6, padx= (2,2), pady=(1,1))
        self.btn_cursor = Button(self.frame_barra, image=self.icons[24], bd = 0, bg = '#c8d6e5')
        self.btn_cursor.grid(row = 0, column = 7, padx= (2,2), pady=(1,1))
        self.btn_sel = Button(self.frame_barra, image=self.icons[23], bd = 0, bg = '#c8d6e5')
        self.btn_sel.grid(row = 0, column = 8, padx= (2,2), pady=(1,1))
        self.btn_lupa = Button(self.frame_barra, image=self.icons[3], bd = 0, bg = '#c8d6e5')
        self.btn_lupa.grid(row = 0, column = 9, padx= (2,2), pady=(1,1))
        self.btn_fit = Button(self.frame_barra, image=self.icons[25], bd = 0, bg = '#c8d6e5')
        self.btn_fit.grid(row = 0, column = 10, padx= (2,2), pady=(1,1))

        self.sep3 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep3.grid(row = 0, column = 11, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_begin = Button(self.frame_barra, image=self.icons[1], bd = 0, bg = '#c8d6e5')
        self.btn_begin.grid(row = 0, column = 12, padx= (2,2), pady=(1,1))
        self.btn_left = Button(self.frame_barra, image=self.icons[12], bd = 0, bg = '#c8d6e5')
        self.btn_left.grid(row = 0, column = 13, padx= (2,2), pady=(1,1))
        self.combo_pag = ttk.Combobox(self.frame_barra, width = 10, state = 'readonly')
        self.combo_pag.grid(row = 0, column = 14, padx = (2,2), pady = (1,1))
        self.btn_right = Button(self.frame_barra, image=self.icons[18], bd = 0, bg = '#c8d6e5')
        self.btn_right.grid(row = 0, column = 15, padx= (2,2), pady=(1,1))
        self.btn_end = Button(self.frame_barra, image=self.icons[9], bd = 0, bg = '#c8d6e5')
        self.btn_end.grid(row = 0, column = 16, padx= (2,2), pady=(1,1))

        self.sep4 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep4.grid(row = 0, column = 17, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_round_left = Button(self.frame_barra, image=self.icons[19], bd = 0, bg = '#c8d6e5')
        self.btn_round_left.grid(row = 0, column = 19, padx= (2,2), pady=(1,1))
        self.btn_round_right = Button(self.frame_barra, image=self.icons[22], bd = 0, bg = '#c8d6e5')
        self.btn_round_right.grid(row = 0, column = 20, padx= (2,2), pady=(1,1))

        self.sep5 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep5.grid(row = 0, column = 21, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_continuo = Button(self.frame_barra, image=self.icons[4], bd = 0, bg = '#c8d6e5')
        self.btn_continuo.grid(row = 0, column = 22, padx= (2,2), pady=(1,1))
        self.btn_separado = Button(self.frame_barra, image=self.icons[5], bd = 0, bg = '#c8d6e5')
        self.btn_separado.grid(row = 0, column = 23, padx= (2,2), pady=(1,1))

        self.sep6 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep6.grid(row = 0, column = 24, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_menos = Button(self.frame_barra, image=self.icons[15], bd = 0, bg = '#c8d6e5')
        self.btn_menos.grid(row = 0, column = 25, padx= (2,2), pady=(1,1))
        self.combo_view = ttk.Combobox(self.frame_barra, width = 10, state = 'readonly')
        self.combo_view.grid(row = 0, column = 26, padx = (2,2), pady = (1,1))
        self.combo_view['values'] = ['50%','75%','100%','200%','400%','Fit Width', 'Fit Height','Fit Page', 'Actual Size','Stretch']
        self.combo_view.current(7)
        self.btn_mas = Button(self.frame_barra, image=self.icons[17], bd = 0, bg = '#c8d6e5')
        self.btn_mas.grid(row = 0, column = 27, padx= (2,2), pady=(1,1))
        self.btn_pag_size= Button(self.frame_barra, image=self.icons[7], bd = 0, bg = '#c8d6e5')
        self.btn_pag_size.grid(row = 0, column = 28, padx= (2,2), pady=(1,1))
        self.btn_pag_width= Button(self.frame_barra, image=self.icons[8], bd = 0, bg = '#c8d6e5')
        self.btn_pag_width.grid(row = 0, column = 29, padx= (2,2), pady=(1,1))

        self.sep7 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep7.grid(row = 0, column = 30, sticky = "ns", padx= (2,2),pady=(1,1))
        
        self.btn_rotate_l= Button(self.frame_barra, image=self.icons[20], bd = 0, bg = '#c8d6e5')
        self.btn_rotate_l.grid(row = 0, column = 31, padx= (2,2), pady=(1,1))
        self.btn_rotate_r= Button(self.frame_barra, image=self.icons[21], bd = 0, bg = '#c8d6e5')
        self.btn_rotate_r.grid(row = 0, column = 32, padx= (2,2), pady=(1,1))
        
        
        ###################################################################################
        self.frame_barra.grid(row = 0, column = 0)
    
    def interior(self):
        # Frame para el interior
        self.center = Frame(self.root, width = self.ancho, height = self.alto*0.9)
        self.center.grid(row=1, sticky=N+S+E+W)
        self.center.grid_propagate(False)
        # Necesario para mantener tamaños
        self.center.grid_rowconfigure(1, weight = 1)
        self.center.grid_columnconfigure(0, weight = 1)

        ancho = self.ancho

        #Crear tabs
        self.tabMenu = Frame(self.center, height = 30)
        self.tabMenu.grid(row = 0, column = 0, columnspan = 2, sticky = W+E)
        self.nb = ttk.Notebook(self.tabMenu)
        self.nb.grid(row = 1, column = 0, columnspan = 2, sticky=N+E+W+S)
        self.tabNames = ["Pestaña 1", "Pestaña 2",'Pestaña 3']
        self.tabs = []
        for i, name in enumerate(self.tabNames):
            self.tabs.append(ttk.Frame(self.nb))
            self.nb.add(self.tabs[i], text = name)

        # Crea seccion para los thumbnails
        self.side = Frame(self.center, bg = 'white' ,width = ancho*(1/12), height = self.alto*0.9)
        self.side.grid(row = 1, column = 0, sticky = W+N+S+E)
        self.side.config(highlightbackground = '#c8d6e5', highlightthickness = 8)
        
        self.btn_cog = Button(self.side, bg = 'white', image = self.icons[26], bd = 0)
        self.btn_cog.grid(row = 0, column = 0, sticky = E, padx = (4,4), pady = (4,4))
        self.btn_x = Button(self.side, bg = 'white', image = self.icons[27], bd = 0)
        self.btn_x.grid(row = 0, column = 1, sticky = E, padx = (4,4), pady = (4,4))
        

        # Mantiene el tamaño de side
        self.side.grid_columnconfigure(0, weight = 1)

        # Sección para el pdf
        self.content = Frame(self.center, bg="#576574", width = ancho*(9/12), height = self.alto*0.9)
        self.content.grid(row = 1, column = 1, sticky=E+N+S+E)
        self.content.config(highlightbackground = 'gray', highlightcolor = 'black',highlightthickness = 4)
        # Barra inferior
        self.footer = Frame(self.center, height = self.alto*0.035)
        self.footer.grid(row = 2, column = 0, columnspan = 2, sticky=E+W+S)
        self.footer.grid_columnconfigure(0, weight = 1)
        self.footer.grid_columnconfigure(1, weight = 1)
        self.footer.grid_propagate(False)

        # Etiquetas    
        self.ready = Label(self.footer, text="Ready")
        self.ready.grid(row = 0, column = 0, sticky = W)

        self.page = Label(self.footer, text="Page 2 of 2")
        self.page.grid(row = 0, column = 1, sticky = E)
        self.sep8 = ttk.Separator(self.footer,orient = VERTICAL)
        self.sep8.grid(row = 0, column = 2, sticky = "ns", padx= (2,2),pady=(1,1))
        self.medida = Label(self.footer, text = '27.94 x 21.59 cm')
        self.medida.grid(row = 0, column = 3, sticky = E)

         
     



windj = Ventana()
