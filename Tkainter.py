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
 
 # ---------- Label judul ----------
label_judul = tk.Label(
    root, text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"), fg="#1a4f8b",
)
label_judul.pack(pady=(20, 10))

frame_input = tk.LabelFrame(root, text=" Masukkan Nilai Mata Pelajaran ",
                            font=("Arial", 11), padx=15, pady=10)
frame_input.pack(padx=20, pady=10)


entries = []
for i, mapel in enumerate(MAPEL):
    baris = i % 5
    kolom = (i // 5) * 2  # kolom 0-1 dan 2-3
    tk.Label(frame_input, text=mapel, font=("Arial", 10), anchor="w",
             width=16).grid(row=baris, column=kolom, padx=(5, 2), pady=6, sticky="w")
             e = ttk.Entry(frame_input, width=8, justify="center")
    e.grid(row=baris, column=kolom + 1, padx=(2, 15), pady=6)
    entries.append(e)

    tombol = tk.Button(
    root, text="Tampilkan Hasil Prediksi", command=prediksi,