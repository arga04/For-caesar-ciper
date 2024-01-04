#contoh enkripsi sederhana dengan caesar chiper
abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chipher = 2
teks = "tekmik informatika"
hasil_enkripsi = ""
for t in teks:
    if t != " ":
      indeks_lama = abjad.index(t)
      indeks_baru = indeks_lama + chipher
      hasil_enkripsi = hasil_enkripsi + abjad[indeks_baru]
else:
  hasil_enkripsi = hasil_enkripsi + " "

print(hasil_enkripsi)
