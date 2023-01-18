text = "Hello World"

# Menghitung jumlah karakter
jumlah_karakter = len(text)
print("Jumlah karakter:", jumlah_karakter)

# Ambil karakter terakhir
karakter_terakhir = text[-1]
print("Karakter terakhir:", karakter_terakhir)

# Ambil karakter index ke-2
karakter_index_ke2 = text[2:5]
print("Karakter index ke-2:", karakter_index_ke2)

# Hilangkan spasi pada text
text_tanpa_spasi = text.replace(" ", "")
print("Text tanpa spasi:", text_tanpa_spasi)

# Ubah text menjadi huruf besar
text_huruf_besar = text.upper()
print("Text huruf besar:", text_huruf_besar)

# Ubah text menjadi huruf kecil
text_huruf_kecil = text.lower()
print("Text huruf kecil:", text_huruf_kecil)

# Ganti karakter dengan karakter lain
text_ganti_karakter = text.replace("H", "j")
print("Text setelah diganti karakter:", text_ganti_karakter)