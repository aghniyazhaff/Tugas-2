# Tugas 2 - PBP (F)
Nama : Aghniya Zhafira
NPM  : 2106654164

## Link App Heroku
* [MyWatchList Page - HTML](https://tugas2pbpaghniya.herokuapp.com/mywatchlist/html/)
* [MyWatchList Page - JSON](https://tugas2pbpaghniya.herokuapp.com/mywatchlist/json/)
* [MyWatchList Page - XML](https://tugas2pbpaghniya.herokuapp.com/mywatchlist/xml/)

## Pertanyaan Tugas 3
1. Jelaskan perbedaan antara Json, XML, dan HTML

* Json (JavaScript Object Notation) merupakan sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Json terdiri dari dua struktur, diantaranya kumpulan value yang saling berpasangan seperti object dan kumpulan value yang berurutan seperti array.

* XML (Extensive Markup Language) adalah format data berbasis teks yang berasal dari SGML (ISO 8879) dan ditulis dengan cara yang sama diikuti oleh HTML. Pada dasarnya XML akan mengalihdayakan data. Ini menyimpan data dalam format teks biasa daripada mengintegrasikannya ke dalam dokumen HTML yang membuatnya ideal untuk mewakili data hierarkis seperti dokumen, transaksi, faktur, buku, dan banyak lagi. Keuntungan utama XML adalah platform itu independen yang berarti pengguna dapat mengambil data dari program lain seperti SQL dan mengubahnya menjadi XML kemudian membagikan data dengan platform lain

* HTML (Hypertext Markup Language) bahasa markup yang digunakan untuk membuat halaman website. HTML terdiri dari kombinasi teks dan simbol yang disimpan dalam sebuah file. Dalam membuat file HTML, terdapat standar atau format khusus yang harus diikuti. Format tersebut telah tertuang dalam standar kode internasional atau ASCII (American Standard Code for Information Interchange). 

JSON, XML, dan HTML adalah sebuah data delivery yang memiliki perbedaan antara satu sama lain. Ketiganya memiliki fungsi masing masing yang saling berkaitan. Perbedaannya antara lain :
![Tabel Perbedaan](https://user-images.githubusercontent.com/93356052/191655700-bb493bb8-a034-4f94-b91e-74fc4f7ca5a8.jpg)

Beberapa contohnya adalah: HTML : 1. Di pasaran didukung oleh banyak browser 2. Bisa ditambahkan comments XML : 1. Tidak terlalu didukung oleh browser. Terkadang untuk melakukan parse XML terasa sulit. 2. Bisa ditambahkan comments 3. Mendukung Array JSON : 1. Didukung oleh banyak browser 2. Tidak bisa ditambahkan comments 3. Tidak mendukung array

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Karena data delivery berguna sebagai suatu format penyimpanan data. Hal ini penting dalam pengimplementasian sebuah platform karena dalam membuat platform kita akan mengakses database. Kita akan sering melakukan pengiriman atau transmisi data dari web aplikasi yang kita buat. Contohnya ketika ingin mentransmisikan data antara server dan web aplikasi.

Selain itu Data delivery merupakan hal yang dapat mempermudah dalam proses pengiriman data dari stack ke stack saat ingin diimplementasi ke suatu platform

3.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas?

Dalam mengimplementasikan tugas 3 ini, saya melakukan langkah-langkah berikut :
1. Pembuatan aplikasi mywatchlist dengan perintah python manage.py startapp mywatchlist
2. Mendaftarkan aplikasi wishlist ke dalam proyek django dengan cara akses INSTALLED_APPS yang ada pada berkas settings.py pada folder django, kita tambahkan 'mywatchlist'
3. Selanjutnya dengan membuat model MyWatchList. Lalu implementasikan kode berupa menambahkan atribut watched, title, rating, release_date, dan review.
4. Lakukan perintah python manage.py makemigrations lalu python manage.py migrate. untuk mempersiapkan migrasi skema model yang kemudian akan diterapkan dalam database Django lokal.
5. Membuat sebuah berkas bernama watchlist_data.json yang akan memiliki isi list movie. Berkas ini akan memiliki format data delivery json.
6. Kemudian, dengan perintah python manage.py loaddata watchlist_data.json berguna untuk memasukkan data tersebut ke dalam database Django lokal.
7. Dalam folder mywatchlist tambahkan lagi folder templates dan tambahkan berkas watchlist.html yang akan menampilkan data json yang diubah ke html.
8. Pembuatan routing. Pembuatan routing bertujuan agar data yang sudah dibuat dapat diakses melalui URL yang sesuai. Hal ini dilakukan dengan menambahkan path() ke dalam variabel urlpatterns pada urls.py pada folder mywatchlist. penambahan yang dilakukan seperti : path('html/', show_mywatchlist, name='show_mywatchlist') path('xml/', show_xml, name='show_xml') path('json/', show_json, name='show_json')
9. Deployment ke Heroku. Kita perlu mendeploy ke HeroKu agar aplikasi mywatchlist yang sudah dibuat dapat diakses melalui internet bukan hanya dari local saja. Karena pada tugas sebelumnya deployment sudah dilakukan, maka pada tugas kali ini tinggal menyesuaikan saja procfilenya dengan menambahkan " ...python manage.py loaddata initial_mywatchlist_data.json" pada bagian "release: " di procfile.
10. Penambahan unit test pada test.py. Hal ini bertujuan untuk melakukan pengujian URL dapat mengembalikan respon HTTP 200 OK.


4. Akses URL menggunakan Postman
![Postman_HTML](https://user-images.githubusercontent.com/93356052/191636782-341084e6-17c6-40f2-9cb8-ceabf5f4ceca.jpg)

![Postman_JSON](https://user-images.githubusercontent.com/93356052/191636827-286b3f95-e0c5-408b-ad99-925fe977597e.jpg)

![Postman_XML](https://user-images.githubusercontent.com/93356052/191636850-febd8fe1-43ad-4644-b90d-fb796bd7538d.jpg)


5. Menambahkan unit test pada test.py 
Sudah Menambahkan unit test 



