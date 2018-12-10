from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image

#--Agrega el icono de WinDj al programa--#
import os 


class Ventana:
    def __init__(self):
        self.root = Tk()
        #self.base_folder = os.path.dirname(__file__)
        #self.image_path = os.path.join(self.base_folder,'djvu_icon.gif')
        #self.img = PhotoImage(file = self.image_path)
        #self.root.tk.call('wm','iconphoto',self.root._w, self.img)
        self.ancho = self.root.winfo_screenwidth()
        self.alto = self.root.winfo_screenheight()
        self.root.geometry(str(self.ancho) + 'x' + str(self.alto))
        self.root.configure(bg = 'white')
        self.root.title('WinDjView')
        self.addMenu()
        self.addMenuIcons()
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
        self.frame_barra = Frame(self.root, bg = '#dfe6e9', bd=2,)
        self.frame_barra.configure( width = self.ancho, height = 30)
        self.frame_barra.grid_propagate(False)
        ############################# Barra de Herramientas ################################
        self.btn_open = Button(self.frame_barra, image=self.icons[16], bd = 0, bg = '#dfe6e9')
        self.btn_open.grid(row = 0, column = 0, padx= (2,2), pady=(1,1))

        self.sep1 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep1.grid(row = 0, column = 1, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_print = Button(self.frame_barra, image=self.icons[10], bd = 0, bg = '#dfe6e9')
        self.btn_print.grid(row = 0, column = 2, padx= (2,2), pady=(1,1))
        self.btn_bin = Button(self.frame_barra, image=self.icons[2], bd = 0, bg = '#dfe6e9')
        self.btn_bin.grid(row = 0, column = 3, padx= (2,2), pady=(1,1))
        self.btn_info = Button(self.frame_barra, image=self.icons[11], bd = 0, bg = '#dfe6e9')
        self.btn_info.grid(row = 0, column = 4, padx= (2,2), pady=(1,1))

        self.sep2 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep2.grid(row = 0, column = 5, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_hand = Button(self.frame_barra, image=self.icons[0], bd = 0, bg = '#dfe6e9')
        self.btn_hand.grid(row = 0, column = 6, padx= (2,2), pady=(1,1))
        self.btn_cursor = Button(self.frame_barra, image=self.icons[24], bd = 0, bg = '#dfe6e9')
        self.btn_cursor.grid(row = 0, column = 7, padx= (2,2), pady=(1,1))
        self.btn_sel = Button(self.frame_barra, image=self.icons[23], bd = 0, bg = '#dfe6e9')
        self.btn_sel.grid(row = 0, column = 8, padx= (2,2), pady=(1,1))
        self.btn_lupa = Button(self.frame_barra, image=self.icons[3], bd = 0, bg = '#dfe6e9')
        self.btn_lupa.grid(row = 0, column = 9, padx= (2,2), pady=(1,1))
        self.btn_fit = Button(self.frame_barra, image=self.icons[25], bd = 0, bg = '#dfe6e9')
        self.btn_fit.grid(row = 0, column = 10, padx= (2,2), pady=(1,1))

        self.sep3 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep3.grid(row = 0, column = 11, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_begin = Button(self.frame_barra, image=self.icons[1], bd = 0, bg = '#dfe6e9')
        self.btn_begin.grid(row = 0, column = 12, padx= (2,2), pady=(1,1))
        self.btn_left = Button(self.frame_barra, image=self.icons[12], bd = 0, bg = '#dfe6e9')
        self.btn_left.grid(row = 0, column = 13, padx= (2,2), pady=(1,1))
        self.combo_pag = ttk.Combobox(self.frame_barra, width = 10)
        self.combo_pag.grid(row = 0, column = 14, padx = (2,2), pady = (1,1))
        self.btn_right = Button(self.frame_barra, image=self.icons[18], bd = 0, bg = '#dfe6e9')
        self.btn_right.grid(row = 0, column = 15, padx= (2,2), pady=(1,1))
        self.btn_end = Button(self.frame_barra, image=self.icons[9], bd = 0, bg = '#dfe6e9')
        self.btn_end.grid(row = 0, column = 16, padx= (2,2), pady=(1,1))

        self.sep4 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep4.grid(row = 0, column = 17, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_round_left = Button(self.frame_barra, image=self.icons[19], bd = 0, bg = '#dfe6e9')
        self.btn_round_left.grid(row = 0, column = 19, padx= (2,2), pady=(1,1))
        self.btn_round_right = Button(self.frame_barra, image=self.icons[22], bd = 0, bg = '#dfe6e9')
        self.btn_round_right.grid(row = 0, column = 20, padx= (2,2), pady=(1,1))

        self.sep5 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep5.grid(row = 0, column = 21, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_continuo = Button(self.frame_barra, image=self.icons[4], bd = 0, bg = '#dfe6e9')
        self.btn_continuo.grid(row = 0, column = 22, padx= (2,2), pady=(1,1))
        self.btn_separado = Button(self.frame_barra, image=self.icons[5], bd = 0, bg = '#dfe6e9')
        self.btn_separado.grid(row = 0, column = 23, padx= (2,2), pady=(1,1))

        self.sep6 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep6.grid(row = 0, column = 24, sticky = "ns", padx= (2,2),pady=(1,1))

        self.btn_menos = Button(self.frame_barra, image=self.icons[15], bd = 0, bg = '#dfe6e9')
        self.btn_menos.grid(row = 0, column = 25, padx= (2,2), pady=(1,1))
        self.combo_view = ttk.Combobox(self.frame_barra, width = 10)
        self.combo_view.grid(row = 0, column = 26, padx = (2,2), pady = (1,1))
        self.btn_mas = Button(self.frame_barra, image=self.icons[17], bd = 0, bg = '#dfe6e9')
        self.btn_mas.grid(row = 0, column = 27, padx= (2,2), pady=(1,1))
        self.btn_pag_size= Button(self.frame_barra, image=self.icons[7], bd = 0, bg = '#dfe6e9')
        self.btn_pag_size.grid(row = 0, column = 28, padx= (2,2), pady=(1,1))
        self.btn_pag_width= Button(self.frame_barra, image=self.icons[8], bd = 0, bg = '#dfe6e9')
        self.btn_pag_width.grid(row = 0, column = 29, padx= (2,2), pady=(1,1))

        self.sep7 = ttk.Separator(self.frame_barra,orient = VERTICAL)
        self.sep7.grid(row = 0, column = 30, sticky = "ns", padx= (2,2),pady=(1,1))
        
        self.btn_rotate_l= Button(self.frame_barra, image=self.icons[20], bd = 0, bg = '#dfe6e9')
        self.btn_rotate_l.grid(row = 0, column = 31, padx= (2,2), pady=(1,1))
        self.btn_rotate_r= Button(self.frame_barra, image=self.icons[21], bd = 0, bg = '#dfe6e9')
        self.btn_rotate_r.grid(row = 0, column = 32, padx= (2,2), pady=(1,1))
        
        
        ###################################################################################
        self.frame_barra.grid(row = 0, column = 0)
        
     



windj = Ventana()
