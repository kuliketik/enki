# Tentang

Proyek ini bertujuan untuk mendapatkan pengetahuan mengenai *engagement* seperti *like*, *comment* pada media online. 


# Media online target

- detik.com

- tribunews.com

- tirto.id 

- theconversation.com

- merdeka.com

- kompas.com 

# Instalasi 

- Pasang dependensi

```
$ virtualenv env --python=3.6
$ source env/bin/activate # *nix
$ env\Scripts\activate.bat # windows
$ pip install -r requirements.txt
```

- Buat file config.py di enki/config.py

```
$ vim enki/config.py

config = dict(
	consumer_key = "YOUR_CONSUMER_KEY",
	consumer_secret = "YOUR_CONSUMER_SECRET",
	token_key = "YOUR_TOKEN_KEY",
	token_secret = "YOUR_TOKEN_SECRET"
	)
```

- Jalankan Enki

```
$ python enki/enki.py
```

# Milestone

1. Dapatkan url dari tweet dengan engagement paling banyak [SELESAI]
2. Buat fitur ekstraksi konten dari URL menggunakan BeautifulSoup [ON GOING]
3. Knowledge base target konten (lihat base.py:47) [TODO]
4. Simpan konten ke database sementara [TODO] Skema tabel SQL untuk menyimpan konten
```
id, media_name, twitter_handle, rt_count, fav_count, parsed_content
``` 
5. Buat pipeline untuk pembersihan konten (bersihkan stopwords, dan tanda baca) [TODO]
6. Simpan konten yang sudah dibersihkan ke database [TODO]
7. Buat visualisasi [TODO]
8. Buat analisis terhadap konten yang sudah dibersihkan [TODO]
9. Tulis hasil analisis [TODO]

# Keluaran

- Kode Enki

Diharapkan kodebase Enki bisa digunakan sebagai dasar untuk penelitian terkait.


- Data Enki

Diharapkan data yang telah dikumpulkan dari project Enki dapat digunakan untuk penelitian terkait.

- Whitepaper/artikel

# FAQ

- Kenapa diberi nama *Enki*?
 > Enki adalah dewa pengetahuan dan kebijaksanaan (wisdom) bangsa Mesopotania. Nama *enki* sesuai dengan tujuan proyek ini yaitu untuk mendapatkan pengetahuan tentang ketertarikan dan minat netizen di Indonesia  

- Bolehkan saya menggunakan basis kode Enki untuk penelitian yang sedang saya lakukan? 
> Boleh, namun kamu harus mencantumkan repositori proyek ini di bagian referensi atau daftar pustaka 


