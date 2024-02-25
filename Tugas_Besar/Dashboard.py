import tkinter as tk
from FrmApotek import FormApotek

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("500x500")

        self.label = tk.Label(self, text="Pilih Menu")
        self.label.place(x=100, y=50)

        self.FormApotek_button = tk.Button(self, text="azis", command=self.open_FormApotek)
        self.FormApotek_button.place(x=50, y=100, width=150, height=30)

    def open_FormApotek(self):
        self.Form_Apotek = FormApotek(self, "Form Apotek")
        self.Form_Apotek.mainloop()

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.mainloop()
