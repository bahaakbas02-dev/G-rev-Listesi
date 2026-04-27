import tkinter as tk
from tkinter import messagebox

def ekle():
    gorev = giris.get()
    if gorev != "":
        liste.insert(tk.END, gorev)
        giris.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen Önce Yazı Yazınız!")    

def sil():
    try:
        secili = liste.curselection()[0]
        liste.delete(secili)
    except:
        messagebox.showwarning("Uyarı", "Silmek İçin Bir Görev Seç")    

pencere = tk.Tk()
pencere.title("Görev Listesi")
pencere.geometry("1000x600")
pencere.configure(bg="#E5EF8C")

baslik = tk.Label(pencere, text="Görev Listesi", font=("Arial", 15, "bold"), bg="#E5EF8C", fg="#000000")
baslik.pack(pady=10)

giris = tk.Entry(pencere, width=60)
giris.pack(pady=10)

ekle_butonu = tk.Button(pencere, text="Ekle", command=ekle, bg="#28A745", fg="#FFFFFF", font=("Arial", 10, "bold"),  activebackground="#0F3D19", cursor="hand2", width=20)
ekle_butonu.pack(pady=10)

liste = tk.Listbox(pencere, width=40)
liste.pack(pady=10)

sil_butonu = tk.Button(pencere, text="Sil", command=sil, bg="tomato", fg="#FFFFFF", font=("Arial", 10, "bold"), activebackground="#7B1313", cursor="hand2", width=20)
sil_butonu.pack(pady=10)

pencere.mainloop()