import tkinter as tk
from tkinter import ttk, messagebox
from apotek import Apotek

class FormApotek:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("800x800")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = ttk.Frame(self.parent, borderwidth=10)  # Use 'borderwidth' instead of 'bd'
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        
        # Label
        entries = [
            ('no_inv:', 0),
            ('nama_obat:', 1),
            ('jumlah_pembelian:', 2),
            ('harga:', 3),
        ]

        self.widgets = {}
        for label, row in entries:
            ttk.Label(mainFrame, text=label).grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
            entry = ttk.Entry(mainFrame)
            entry.grid(row=row, column=1, padx=5, pady=5)
            self.widgets[label.strip(':')] = entry

        # Button
        buttons = [('Simpan', 0, self.onSimpan), ('Clear', 1, self.onClear), ('Hapus', 2, self.onDelete)]
        for text, row, command in buttons:
            button = ttk.Button(mainFrame, text=text, command=command, width=10)
            button.grid(row=row, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'no_inv', 'nama_obat', 'jumlah_pembelian', 'harga')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        for widget in self.widgets.values():
            widget.delete(0, tk.END)
        self.onReload()
        self.ditemukan = False
        
    def onReload(self):
        # get data apotek
        a = Apotek()
        result = a.getAllData()
        self.tree.delete(*self.tree.get_children())
        for row_data in result:
            self.tree.insert('', tk.END, values=row_data)
    
                 
    def onSimpan(self):
        data = {key: widget.get() for key, widget in self.widgets.items()}
        a = Apotek()
        a.no_inv = data['no_inv']
        a.nama_obat = data['nama_obat']
        a.jumlah_pembelian = data['jumlah_pembelian']
        a.harga = data['harga']
        
        ket = 'Diperbarui' if self.ditemukan else 'Disimpan'
        res = a.updateByno_inv(a.no_inv) if self.ditemukan else a.simpan()
        rec = a.affected
        if rec > 0:
            messagebox.showinfo("showinfo", f"Data Berhasil {ket}")
        else:
            messagebox.showwarning("showwarning", f"Data Gagal {ket}")
        self.onClear()

    def onDelete(self):
        no_inv = self.widgets['no_inv'].get()
        a = Apotek()
        a.no_inv = no_inv
        res = a.deleteByno_inv(no_inv)
        rec = a.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        else:
            messagebox.showinfo("showinfo", "Data tidak ditemukan atau gagal dihapus")
        
        self.onClear()

    
    def onKeluar(self):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormApotek(root, "Aplikasi Data Apotek")
    root.mainloop()




