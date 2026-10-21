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
 