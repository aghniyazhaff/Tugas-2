# Tugas 2 - PBP (F)
### Nama : Aghniya Zhafira
### NPM  : 2106654164

## Link App Heroku
[Home Page](http://localhost:8000/)
[Katalog Page](https://tugas2pbpaghniya.herokuapp.com/katalog/)


## Pertanyaan Tugas 2
1. Terdapat keterkaitan antara urls.py, views.py, models.py, dan berkas html antara lain sebagaimana yang tertera pada bagan berikut :
![untitled@1 25x(1)](https://user-images.githubusercontent.com/93356052/190232041-b3aa4c8e-cda1-4552-bc2d-dd6535c6c3e6.png)


2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

* Alasan mengapa menggunakan _virtual environment_ yaitu karena _virtual environment_ merupakan suatu wadah yang sudah terotomatis dalam menginstalasi packages dan dependencies yang diperlukan dalam framework django yang tidak terinstalasi secara global di local. Dengan begitu _virtual environment_  memungkinkan developer untuk membuat project yang berbeda-beda dengan dependencies yang berbeda-beda dalam suatu device atau sistem operasi. 

 _Virtual environment_  ini akan membuat environment masing-masing untuk tiap project atau app, sehingga akan menghindari konflik dengan sistem operasi utama yang sedang digunakan. Dengan virtual environtment kita juga dapat membuat lingkungan kerja python yang terisolasi sehingga tidak menganggu ketika kita memiliki project yang banyak.

 _Virtual environment_ juga memudahkan mobilisasi atau perpindahan project antar device. Jadi, seorang developer dapat dengan mudah mengerjakan projectnya tanpa melakukan konfigurasi ulang.

 * Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment namun tentunya akan rawan terjadi konflik dan agak sulit untuk melakukan mobilisasi seperti yang saya jelaskan pada pertanyaan sebelumnya

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

    1. Langkah pertama yaitu dengan membuat fungsi (show_catalog(request)) yang terdapat pada views.py, dimana fungsi tersebut melakukan query data dari .json dengan menggunakan syntax data_barang_katalog = CatalogItem.objects.all(). Data yang telah diambil akan direturn ke .html dengan menggunakan fungsi render()

    2. Langkah selanjutnya yaitu dengan memetakan fungsi yang terletak pada views.py dimana fungsi tersebut akan mulai memetakan apabila fungsi routing sudah dibuat.
    
    Fungsi routing dibuat dengan cara menambahkan/memasukkan path pada folder katalog file urls.py dan project_django.
    - Pada Katalog
        urlpatterns = [
            path('', show_catalog, name='show_catalog'),
        ]
    - Pada project_django
        urlpatterns = [
            . . .
            path('katalog/', include('katalog.urls')),
        ]
    Hal ini dilakukan agar ketika client mengirimkan request terhadap URL katalog, fungsi show_katalog(request) akan dipanggil.

    3. Data yang telah di render dipetakan ke HTML dengan melakukan iterasi data sesuai template. Setelahnya, untuk dapat menjalankan app pada lokal, kita perlu melakukan command makemgration untuk membuat suatu wadah yang selanjutnya dilakukan migrate agar tersedianya wadah yang belum terisi. Lalu kita melakukan loaddata agar wadah tersebut terisi data yang telah diberikan secara template. Agar lebih rapih dan readable, ditambahkan sebuah table pada style.css

    4. Proses selanjutnya adalah melakukan commit dan push pada repositori lokal github, lalu melakukan deployment pada Heroku. Membuat repository secret lalu menambahkan App Name dan API key. Lakukan kembali add, commit, dan push, lalu pada menu Actions pun dapat dilihat aktivitas deploy dari app.
