import tkinter as tk

Jokowi = tk.Tk()
Jokowi.title("Aplikasi Prediksi Prodi")

tk.Label(Jokowi, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 11, "bold")).pack(pady=5)

for i in range(10):
    f = tk.Frame(Jokowi)
    f.pack(fill="x", padx=10, pady=2)
    tk.Label(f, text=f"Nilai Mapel {i+1}:", width=15, anchor="w").pack(side=tk.LEFT)
    tk.Entry(f).pack(side=tk.RIGHT, expand=True, fill="x")

def prediksi():
    luaran.config(text="Hasil Prediksi: Teknologi Informasi")

tk.Button(Jokowi, text="Hasil Prediksi", command=prediksi).pack(pady=5)
luaran = tk.Label(Jokowi, text="Hasil Prediksi: -", font=("Arial", 10, "bold"))
luaran.pack(pady=5)
Jokowi.mainloop()