import tkinter as tk
from tkinter import ttk
 
# Daftar 10 mata pelajaran
MAPEL = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Sejarah", "Geografi", "Ekonomi", "Sosiologi",
]

def prediksi():
    """Menampilkan prodi Teknologi Informasi apapun masukan yang diberikan."""
    label_hasil.config(text="Teknologi Informasi")

    # ---------- Jendela utama ----------
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.resizable(False, False)
 
 # Posisikan jendela di tengah layar
lebar, tinggi = 520, 520
x = (root.winfo_screenwidth() - lebar) // 2
y = (root.winfo_screenheight() - tinggi) // 2
root.geometry(f"{lebar}x{tinggi}+{x}+{y}")
 