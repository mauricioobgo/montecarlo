from managerDb import dbManager
from tkinter import filedialog
from tkinter import messagebox
import tkinter
class flatManager(dbManager):
    #"""docstring for flatManager"""
    def __init__(self):
        self.directory=""

#    def openFile():
    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def frameImport(self):
        win = tkinter.Tk()
        win.geometry("200x120")
        win.title("FILE_PICKER")
        butt=tkinter.Button(win,text="Archivo",command=self.fileDirectory)
        butt1=tkinter.Button(win,text="Continuar",command=lambda: self.quit_pressed(win))
        butt.config(height=2, width=15)
        butt1.config(height=2, width=15)
        butt.place(x=40,y=20)
        butt1.place(x=40,y=80)
        self.center(win)
        win.mainloop()

    def fileDirectory(self):
        result = filedialog.askopenfilename()
        self.directory=result
        msg=messagebox.showinfo( "Directorio", self.directory)

    def quit_pressed(self,ventana):
        ventana.destroy()
        msg=messagebox.askyesnocancel( "Security", "ruta seleccionada"+self.directory)
        print(msg)
        if(msg==True):
            self.fileReader()

    def fileReader(self):
        try:
            mi_archivo=open(self.directory)
            conn=mi_archivo.readlines()
            self.createTable()
            print("tabla creada")
            counter=0
            for line in conn:
                   if(len(line)>87):
                        counter+=1
                        line.strip()
                        fecha_archivo=line[49:53]+'-'+line[53:55]+'-'+line[55:57]
                        nemo=line[5:18]
                        isin=line[18:30]
                        tipo=line[48:49]
                        fecha_emision=line[57:61]+'-'+line[61:63]+'-'+line[63:65]
                        fecha_vencimiento=line[65:69]+'-'+line[69:71]+'-'+line[71:73]
                        fondo=line[73:79]
                        moneda=line[79:82]
                        tipo_tasa=line[82:88]
                        digits2=float(line[89:113])
                        precio_limpio=float(line[113:127])
                        precio_sucio=float(line[166:185])



                        if(counter==1):

                            validator=self.queryDate(fecha_archivo)

                            if(validator==True):
                                self.closeConnection()
                                messagebox.showerror("EXISTING", "ESTE ARCHIVO YA EXISTE")
                                break
                        else:
                            self.insertInfo(nemo,isin,tipo,fecha_archivo,fecha_emision,
                                        fecha_vencimiento,fondo,moneda,tipo_tasa,digits2,
                                        precio_limpio,precio_sucio)




            messagebox.showinfo("END","Process terminated")
            self.closeConnection()

        except IOError:
            messagebox.showerror( "ERROR", "NO SELECCIONO NINGÚN ARCHIVO")
        finally:
                mi_archivo.close()