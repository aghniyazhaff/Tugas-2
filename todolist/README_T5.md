# Tugas 5 - PBP (F)

Nama : Aghniya Zhafira
NPM : 2106654164

- [todolist page](https://tugas2pbpaghniya.herokuapp.com/todolist/)

# Menjawab Pertanyaan

1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

- Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

- Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.

- Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

Berikut tabel kelebihan dan kekurangan :
![Kelebihan dan kekurangan ](https://user-images.githubusercontent.com/93356052/194206309-378847ee-0577-4c68-ac20-a9f6f8550656.jpg)

2. Jelaskan tag HTML5 yang kamu ketahui.

Berikut merupakan beberapa contoh tag HTML 5

- <a> -> mendefenisikan sebuah hyperlink yang dimana link tersebut dapat merujuk ke halaman lain
- <b> -> membuat text menjadi bold
- <body> -> mendefenisikan isi dari suatu HTML yang akan ditampilkan pada browsernya.
- <br> -> membuat sebuah line break.
- <button> -> membuat sebuah button yang dapat di click
- <div>	->  mengelompokkan elemen atau tag agar menjadi satu group
- <form> ->	membuat sebuah form pada HTML yang dapat di-input oleh user
- <header> -> memberikan informasi tentang dokumen
- <h1> to <h6> -> headings pada html
- <input> -> mendefenisikan input untuk user
- <link> ->	mendefenisikan hubungan file html dengan file eksternal
- <ol> -> mendefenisikan sebuah  ordered list.
- <p> -> membuat sebuah paragraph
- <style> -> menambahkan design pada html seperti font,warna atau ukuran font dll
- <table> -> membuat sebuah table
- <td> -> mendefenisikan cell pada sebuah table
- <textarea> -> sebuah tempat untuk user dapat meng-input sebuah text
- <th> -> header  dari sebuah table.
- <title> -> judul dokumen HTML.
- <tr> -> mendefenisikan row dari sebuah table
- <u> -> mendefenisikan text mempunyai garis bawah
- <ul> -> mendefenisikan sebuah unordered list.

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.

Terdapat 6 selektor CSS, diantaranya :

1. Selektor Tag (Type Selector)
   Selektor ini akan memilih elemen berdasarkan nama tag.

2. Selektor Class
   Selektor class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.

3. Selektor ID
   Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja.

4. Selektor Atribut
   Selektor atribut adalah selektor yang memilik elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag.

5. Selektor Universal
   Selektor universal adalah selektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu.

6. Pseudo Selektor
   Pseudo selektor adalah selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.

7. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Untuk mengimplementasikan checklist yang ada, saya melakukan import bootstrap CSS pada html
- Tambahkan dan sesuaikan juga style bootstrap pada masing-masing file
- pada todolist.html saya membuat card pada setiap task yang ditambahkan
- untuk menjaga setiap halaman responsif, terdapat beberapa cara, salah satunya dengan menambahkan @media screen and (max-width: 700px) {
  .column {
  width: 100%;
  }
  }
  pada bagian style
