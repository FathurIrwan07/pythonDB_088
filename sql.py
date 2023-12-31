import tkinter as tk
import sqlite3
from tkinter import messagebox

# buat koneksi buat sqlite databasenya
conn = sqlite3.connect('perdiksi_fakultas.db')
c = conn.cursor()

# buat table nilai_siswa 
c.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY,
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )
''')

# Fungsi untuk menampilkan
def submit_data():
    nama = entry_nama.get()
    bio = int(entry_biologi.get())
    fis = int(entry_fisika.get())
    ing = int(entry_inggris.get())

    # kondisi 
    if bio > fis and bio > ing:
        prediksi = "Kedokteran"
    elif fis > bio and fis > ing:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"

    # memasukan data ke dalam tabel niali_siswa
    c.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, bio, fis, ing, prediksi))
    conn.commit()

    # Perbarui label hasil prediksi
    prediction_result.config(text=f"Prediksi Fakultasnya:  {prediksi}")

# buat jendela halaman
root = tk.Tk()
root.configure(bg="#333333")
root.title("Prediksi Fakultas")
root.geometry("500x500")
root.resizable(False,False)

# Label Judul
label_judul = tk.Label(root, text="Prediksi Fakultas", bg="#333333", fg="#FFFFFF", font=("Verdana",17,"bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(root, labelanchor="n",pady=10, padx=10)
frame_input.pack()

# Label nama siswa
label_nama = tk.Label(frame_input, text="Nama Siswa")
label_nama.grid(row=0, column=0, pady=10)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0, column=1)

# Label Nilai biologi
label_biologi = tk.Label(frame_input, text="Nilai Biologi")
label_biologi.grid(row=1, column=0, pady=10)
entry_biologi = tk.Entry(frame_input)
entry_biologi.grid(row=1, column=1)

# Label fisika
label_fisika = tk.Label(frame_input, text="Nilai Fisika")
label_fisika.grid(row=2, column=0, pady=10)
entry_fisika = tk.Entry(frame_input)
entry_fisika.grid(row=2, column=1)

# Label bahasa inggris
label_inggris = tk.Label(frame_input, text="Nilai Inggris")
label_inggris.grid(row=3, column=0, pady=10)
entry_inggris = tk.Entry(frame_input)
entry_inggris.grid(row=3, column=1)


'''fungsi ini untuk memanggil submit_data()fungsinya 
dan Akan muncul kotak pesan dengan judul "Info" dan pesan "Data berhasil disimpan".'''
def submit_wrapper():
    submit_data()
    messagebox.showinfo("Info", "Data berhasil disimpan")

#membuat tombol/butoom submit
submit_button = tk.Button(root, text="Submit", bg="#FF3399", fg="#FFFFFF", command=submit_wrapper)
submit_button.pack(pady=10)

frame_hasil = tk.LabelFrame(root,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

#untuk menampilkan hasil prediksi
prediction_result = tk.Label(root, text="", bg="#333333", fg="#FFFFFF", font=("Verdana", 13, "bold"))
prediction_result.place(x=100, y=380)

# Jalankan Aplikasi
root.mainloop()
