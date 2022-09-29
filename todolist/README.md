# Tugas 4 - PBP (F)
Nama : Aghniya Zhafira
NPM  : 2106654164

* [todolist page](https://tugas2pbpaghniya.herokuapp.com/todolist/)

# Menjawab Pertanyaan
1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Cross-Site Request Forgery (CSRF) merupakan sebuah serangan eksploitasi web yang membuat pengguna tanpa sadar mengirim sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu. Hal ini terjadi karena terkadang user menginput data credential ke suatu website yang terpercaya namun ketika mengunjungi website yang tidak aman, data yang tersimpan akan bocor akibat manipulasi request dari cookies session. Oleh karenanya django menyediakan CSRF Token yang merupakan kode rahasia acak yang unik untuk setiap situs tertentu.

 CSRF Token bersifat rahasia dan ditangani dengan cara yang aman sepanjang life cicley program. Kegunaan CSRF pada form yaitu untuk membandingan key csrf ketika sebuah end-user ingin melakukan method post atau get, form tersebut akan merespons OK jika form disubmit atau diakses dengan user_session yang tepat.

Jika kita tidak menggunakan csrf token, website yang kita miliki tetap akan berjalan dengan baik, akan tetapi mungkin ada beberapa route link sensitif yang bisa diakses secara umum oleh oknum lain. CRSF token ini harus ada agar menambah proteksi data dengan menyulitkan penyerang untuk meniru request yang sama karena CSRF Token sangat panjang. Tanpa CSRF Token, user akan mendapatkan 403 error.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Tentu kita dapat membuat atau merender elemen <form> secara manual dengan cara menambahkan <input><\input> sesuai dengan isi form yang diinginkan pada bagian antara atart tag dan end tag form. Setelahnya tambahkan juga <input> yang memiliki type submit untuk mensubmit form tersebut

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

    1. User menginput data melalui HTML page (./todolist/create-task)
    2. Melalui fungsi create_task di views.py, form membuat object Task baru.
    3. Laman ./todolist akan menampilkan tabel yang berisi task khusus milik tersebut. Hal ini dilakukan dengan mem-filter kumpulan object Task yang ada dengan Task objects.filter(user=req.user) dan disimpan ke suatu variabel (untuk kasus saya task).
    4. Variabel task tadi ditambahkan ke variabel context dengan key sebagai berikut 'tasks' : task
    5. Key 'tasks' yang menyimpan kumpulan task milik user akan diiterasi untuk ditampilkan di tabel pada file todolist.html (laman ./todolist)

4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    1. Menjalankan python manage.py startapp todolist di folder root.
    2. Menambahkan path('todolist/', include('todolist.urls')), di urls.py. .project django agar route dengan url yang ada di todolist dan menjalankan fungsi show_todolist yang ada di todolist/views.py.
    3. Membuat class di Todolist/models.py dan membuatnya field sesuai yang diperintahkan pada tugas.
    4. Membuat fungsi login, logout, register yang masing masing terhubung dengan login.html dan register.html dan membuat restriksi agar user harus login dahulu dengan menambahkan @login_required(login_url='/todolist/login/') diatas fungsi yang merupakan main dari project.
    5. Mengedit bagian html agar menampikan user dengan mengakses variable yang ada di contexx ({{username}}) dan membuat dua buah button yang masing-masing memiliki logical command untuk logout, tambah task baru, dan membuat tabel untuk menampilkan data-data todolist yang sudah disubmit ke database.
    6. Ketika user memencet tombol tambah task, user akan diarahkan ke halaman baru todolist/create-task dan akan membuat form yang berisi task dan description yang akan dikirim ke fungsi create di views.py untuk ditambahkan ke database.
    7. Membuat route agar terhubung dengan fungsi fungsi yang ada di views py ketika mengakses link todolist/register, login, create-task, delete, change, dan lain-lain.
    8. Deploy ke heroku dan membuat 2 user dengan masing-masing 3 dummy list to do.
