url web -> https://refki-septian-footballshop.pbp.cs.ui.ac.id/

TUGAS II

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    a. Membuat sebuah proyek Django baru.
    penjelasan: saya membuat direktori baru, setelah itu mengaktifkan virtual environment. Pada tahap ini analoginya ketika saya ingin memasak nasi saya akan menyiapkan nasi alat - alat yang saya butuhkan, dalam kasus ini seperti requirments.txt (install dependencies), .env dan .env.prod (menyiapkan kunci untuk data base saya), dan beberapa pengaturan terkait siapa saja yang dapat mengakses web saya atau lainnya di settings.py

    b. Membuat aplikasi dengan nama main pada proyek tersebut.
    penjelasan: saya membuat direktori baru (menggunakan terminal dan otomatis akan menerapkan MVT) di dalam proyek utama hal ini bertujuan untuk membuat aplikasi yang khusus menghandle main (tampilan utama dari web saya) dan mendaftarkannya di file settings.py pada direktori utama (Django mengetahui bahwa aplikasi tersebut ada dan harus diproses). Pada tahap ini saya melakukan perubahan pada file - file yang berkaitan dengan MVT.
        Models -> Pada tahap ini saya membuat class baru dengan field - field yang diperlukan atau yang sesuai dengan instruksi tugas. Models adalah bagian yang berhubungan dengan data, dengan menyiapkan class baru dengan fieldnya saya membuat meta data untuk aplikasi ini.
        views -> views adalah jembatan antara models (data) dengan template (tampilan kepada user). Saya membuat sebuah fungsi yang akan menghanlde input(permintaan) pengguna untuk menampilkan halaman utama. views kemudian mengirimkan/mencocokan dari data yang ada dengan template (dalam kasus ini html)
        template -> template adalah tampilan (hasil akhir) dari apps yang telah saya buat

    c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    penjelasan: Routing di level proyek mengatur distribusi URL ke berbagai aplikasi menggunakan fungsi include(). Hal ini berperan sebagai koordinator utama yang mengarahkan traffic ke aplikasi yang tepat, analoginya seperti penunjuk arah ke provinsi atau kota.

    d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
    penjelasan: pada tahap ini saya membuat meta data atau rancangan bagaimana setiap informasi disimpan ke database. Mulai dari nama produk (maksimal panjangnya berapa) dan lain informasi - informasi lainnya yang nantinya akan dibutuhkan. Saya mengikuti ketentuan yang telah dituliskan saja.

    e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    penjelasan: pada tahap ini saya membuat fungsi yang berguna untuk menghandle request dari user dan menampilkan html yang sesuai dengan request tersebut. Seperti yang telah saya jelaskan sebelumnya, views.py menjadi penghubung antara models.py dan template. Namun, untuk saat ini data masih statis (belum mengambil dari data base) sehingga menuliskannya secara manual dan dimasukkan ke dalam placeholder pada html.

    f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    penjelasan: Routing di level aplikasi menentukan path URL spesifik dan menghubungkannya dengan fungsi view yang akan dijalankan. Ini seperti alamat detail dalam kompleks - menentukan jalan dan nomor rumah yang tepat. Setiap path di urls.py (main) langsung mengatur fitur mana yang akan diproses ketika user mengakses URL dengan path tertentu.
    
    g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    penjelasan: Masuk ke halaman Pws dan membuat projek baru kemudian menambahkan allowed host pada settings.py dengan url web yang kita (supaya dapat diakses orang lain). Setelah itu melakukan git push pws master pada terminal untuk melakukan push ke pws

    h. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
penjelasan:  Client Request yang diterima oleh urls.py Level Proyek Django untuk melakukan pemeriksaan pola endpoint URL yang diminta. Jika pola URL cocok, request akan diteruskan melalui include('main.urls') ke views.py untuk diproses, namun jika tidak ditemukan akan menampilkan 404 Not Found. Di dalam views.py, fungsi akan memproses business logic dan dapat berinteraksi dengan models.py untuk mengambil atau memanipulasi data dari database, kemudian menggabungkan data tersebut dengan Template (file HTML) untuk menghasilkan response yang akan dikembalikan ke client. 
![Bagan Client Request Django](Bagan%20Client%20Request%20Django.png)


3. Jelaskan peran settings.py dalam proyek Django!

penjelasan: settings.py adalah file konfigurasi utama dalam proyek Django yang berfungsi sebagai "pusat kendali" seluruh aplikasi. File ini menentukan hal-hal penting seperti database mana yang akan digunakan untuk menyimpan data (SQLite, MySQL, dll), aplikasi apa saja yang boleh berjalan di website (seperti daftar fitur yang diaktifkan), pengaturan keamanan (password rahasia, mode development atau production), bahasa dan zona waktu website, serta lokasi file-file seperti gambar dan CSS.

4. Bagaimana cara kerja migrasi database di Django?
penjelasan: Migrasi database di Django seperti "sistem update otomatis" untuk struktur database. Tiap kali ada perubahan pada berkas model.py Django tidak langsung mengubahnya di database maka dari itu perlu menjalankan perintah python manage.py makemigrations terlebih dahulu yang akan membuat "rencana perubahan" dalam bentuk file migrasi, kemudian jalankan python manage.py migrate untuk benar-benar menerapkan perubahan tersebut ke database. 

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
penjelasan: Django mudah dipahami untuk pemula. Konsep pemisahan tugas (MVT) membatu membangun website menjadi lebih mudah. Pada semester satu kita sudah mempelajari bahasa pemrogaraman python yang sintaksnya cukup mudah untuk dipahami dan ini juga linier dengan Django yang menggunakan bahasa pemrograman yang sama. 

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
feedback: Penjelasan di tutorial sudah sangat baik, tetapi memang sebaiknya dilakukan secara offline karena interaksi dengan para asdos menjadi lebih mudah

TUGAS III

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
jawab: data adalah hal yang penting di sini, jadi ketika kita bisa mendapatkan lebih banyak data 
maka itu akan lebih baik. Oleh karena itu kita memerlukan "jembatan" agar satu mesin atau aplikasi dapat
bertukar data dengan mesin lain, di sinilah peran data delivery

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
jawab: menurut saya keduanya memiliki kekurangan dan keunggulan masing - masing, tetapi menurut saya yang lebih 
baik itu adalah JSON karena kita tidak memerlukan banyak tag didalamnya implikasinya adalah proses 
perpindahan data itu menjadi lebih cepat. Hal ini juga yang menjadi alasan mengapa json lebih populer.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
jawab: fungsi dari method is_valid() pada form Django adalah untuk memastikan setiap data yang ada itu clean
sesuai dengan tipe datanya dan kita membutuhkan ini supaya tidak menuliskan validasi yang berulang - ulang.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
jawab: kita membutuhkan crsf_token supaya menghindari adanya request yang sebenarnya bukan datang dari pengguna, yang terjadi ketika kita tidak menambahkan csrf_token pada Django adalah penyerang dapat membuat buatan request dari user yang bisa saja merugikan user seperti 
mengambil uang atau mengubah email. Hidden form + auto-submit JavaScript — buat form tersembunyi di situs penyerang yang POST ke endpoint target, lalu submit otomatis. Pengguna yang membuka halaman itu akan mengirim request ke target dengan cookie mereka.
sumber: https://owasp.org/www-community/attacks/csrf

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    a. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
    jawab: membuat fungsi yang menghandle mengirimkan semua data dalam format xml dan json (mengambil semua objek produk kemudian menggunakan
    serializers untuk mentranslate ke xml atau json ) kemudian membuat fungsi yang mengirimkan 
    data berdasarkan id dalam format json dan xml (mekanismenya sama tetapi kita menambahkan filter/get supaya mendapatkan data yang sesuai id). 

    b. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
    jawab: mengimpor fungsi - fungsi tersebut ke urls.py dan menambahkan path untuk masing - masing fungsi yang telah dibuat sebelumnya 

    c. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
    jawab: membuat file html baru untuk menangani ini di templates yang mengextend file base.html kemudian memasukkan data apa saja yang
    akan ditampilkan

    d. Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
    jawab: menambahkan file form.py (saya menuliskan field apa saja yang akan diminta) kemudian memanggil objeknya ketika membuat fungsi di view.py. Setelah itu saya membuat file html yang akan menghandle request ini.

    e. Membuat halaman yang menampilkan detail dari setiap data objek model.
    jawab: membuat fungsi baru pada views.py yang mengambil product berdasarkan id request kemudian menambahkan file html baru untuk menghandle request ini.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
jawab: sudah cukup jelas dan sangat membantu

SS postman

![SS Postman](<3 (1).png>) ![SS Postman](<3 (2).png>) ![SS Postman](<3 (3).png>) ![SS Postman](<3 (4).png>)

Tugas IV

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
    b. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
    c. Menghubungkan model Product dengan User.
    d. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.