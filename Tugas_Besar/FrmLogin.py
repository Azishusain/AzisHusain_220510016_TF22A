import tkinter as tk
from tkinter import messagebox
from Users import Users
from Dashboard import Dashboard

class FormLogin(tk.Tk):
    def __init__(self, update_main_window):
        super().__init__()
        self.update_main_window = update_main_window
        self.title("Aplikasi Data Login")
        self.geometry("250x150")
        self.configure(background="white")
        self.setupUI()

    def setupUI(self):
        label_username = tk.Label(self, text="Username:")
        label_username.place(x=20, y=20)
        label_password = tk.Label(self, text="Password:")
        label_password.place(x=20, y=50)

        self.txtusername = tk.Entry(self)
        self.txtusername.place(x=100, y=20)
        self.txtpassword = tk.Entry(self, show="*")
        self.txtpassword.place(x=100, y=50)

        btnSubmit = tk.Button(self, text="Submit", command=self.onSubmit)
        btnSubmit.place(x=20, y=90)
        btnCancel = tk.Button(self, text="Cancel", command=self.destroy)
        btnCancel.place(x=130, y=90)

    def onSubmit(self):
        username = self.txtusername.get()
        password = self.txtpassword.get()

        obj = Users()
        if obj.login(username, password):
            self.update_main_window(True)
            self.showDashboard()
            messagebox.showinfo("Login Berhasil", "Login berhasil!")
        else:
            messagebox.showwarning("Login Gagal", "Username atau password salah!")
            print("Percobaan gagal:", obj.validation)

    def showDashboard(self):
        self.dashboard = Dashboard()
        self.dashboard.mainloop()

if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    form_login = FormLogin(update_main_window)
    form_login.mainloop()
