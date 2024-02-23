from tkinter import Frame,Label, Entry, Button,YES,BOTH,END,Tk,W,font

class FrmMahasiswa:
    def _init_(self,parent,title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELET_WINDOW",self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self)
        mainFrame = Frame(self.parent,bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        label = label(mainFrame, text="Mahasiswa Content", font=font.Font(size=40))
        label.pack(padx=20,pady=20)

    def onKeluar(self,event=None)
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if_name='main_':
    def update_main_window(result):
        print(result)

root = Tk()
aplikasi = FrmMahasiswa(root, "Windows Mahasiswa")
root.mainloop()