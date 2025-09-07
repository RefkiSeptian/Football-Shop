url web -> https://refki-septian-footballshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    a. Membuat sebuah proyek Django baru.
    penjelasan: saya membuat direktori baru, setelah itu mengaktifkan virtual environment. Pada tahap ini analoginya ketika saya ingin memasak nasi saya akan menyiapkan nasi alat - alat yang saya butuhkan, dalam kasus ini seperti requirments.txt (install dependencies), .env dan .env.prod (menyiapkan kunci untuk data base saya), dan beberapa pengaturan terkait siapa saja yang dapat mengakses web saya atau lainnya di settings.py

    b. Membuat aplikasi dengan nama main pada proyek tersebut.
    penjelasan: saya membuat direktori baru (menggunakan terminal dan otomatis akan menerapkan MVT) di dalam proyek utama hal ini bertujuan untuk membuat aplikasi yang khusus menghandle main (tampilan utama dari web saya) dan mendaftarkannya di file settings.py pada direktori utama (Django mengetahui bahwa aplikasi tersebut ada dan harus diproses). Pada tahap ini saya melakukan perubahan pada file - file yang berkaitan dengan MVT.
        Models -> Pada tahap ini saya membuat class baru dengan field - field yang diperlukan atau yang sesuai dengan instruksi tugas. Models adalah bagian yang berhubungan dengan data, dengan menyiapkan class baru dengan fieldnya saya membuat meta data untuk aplikasi ini.
        views -> views adalah jembatan antara models (data) dengan template (tampilan kepada user). Saya membuat sebuah fungsi yang akan menghanlde input(permintaan) pengguna untuk menampilkan halaman utama. views kemudian mengirimkan/mencocokan dari data yang ada dengan template (dalam kasus ini html)
        template -> template adalah tampilan (hasil akhir) dari apps yang telah saya buat

    c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    penjelasan: Routing di level aplikasi menentukan path URL spesifik dan menghubungkannya dengan fungsi view yang akan dijalankan. Ini seperti alamat detail dalam kompleks - menentukan jalan dan nomor rumah yang tepat. Setiap path di urls.py (main) langsung mengatur fitur mana yang akan diproses ketika user mengakses URL dengan path tertentu.

    d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
    penjelasan: pada tahap ini saya membuat meta data atau rancangan bagaimana setiap informasi disimpan ke database. Mulai dari nama produk (maksimal panjangnya berapa) dan lain informasi - informasi lainnya yang nantinya akan dibutuhkan. Saya mengikuti ketentuan yang telah dituliskan saja.

    e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    penjelasan: pada tahap ini saya membuat fungsi yang berguna untuk menghandle request dari user dan menampilkan html yang sesuai dengan request tersebut. Seperti yang telah saya jelaskan sebelumnya, views.py menjadi penghubung antara models.py dan template. Namun, untuk saat ini data masih statis (belum mengambil dari data base) sehingga menuliskannya secara manual dan dimasukkan ke dalam placeholder pada html.

    f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    penjelasan: Routing di level proyek mengatur distribusi URL ke berbagai aplikasi menggunakan fungsi include(). Hal ini berperan sebagai koordinator utama yang mengarahkan traffic ke aplikasi yang tepat, analoginya seperti penunjuk arah ke provinsi atau kota.
    
    g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    penjelasan: Masuk ke halaman Pws dan membuat projek baru kemudian menambahkan allowed host pada settings.py dengan url web yang kita (supaya dapat diakses orang lain). Setelah itu melakukan git push pws master pada terminal untuk melakukan push ke pws

    h. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
penjelasan:  Client Request yang diterima oleh urls.py Level Proyek Django untuk melakukan pemeriksaan pola endpoint URL yang diminta. Jika pola URL cocok, request akan diteruskan melalui include('main.urls') ke views.py untuk diproses, namun jika tidak ditemukan akan menampilkan 404 Not Found. Di dalam views.py, fungsi akan memproses business logic dan dapat berinteraksi dengan models.py untuk mengambil atau memanipulasi data dari database, kemudian menggabungkan data tersebut dengan Template (file HTML) untuk menghasilkan response yang akan dikembalikan ke client. 
![Bagan Client Request Django](<image\Bagan%20Client%20Request%20Django.png>)


3. Jelaskan peran settings.py dalam proyek Django!

penjelasan: settings.py adalah file konfigurasi utama dalam proyek Django yang berfungsi sebagai "pusat kendali" seluruh aplikasi. File ini menentukan hal-hal penting seperti database mana yang akan digunakan untuk menyimpan data (SQLite, MySQL, dll), aplikasi apa saja yang boleh berjalan di website (seperti daftar fitur yang diaktifkan), pengaturan keamanan (password rahasia, mode development atau production), bahasa dan zona waktu website, serta lokasi file-file seperti gambar dan CSS.

4. Bagaimana cara kerja migrasi database di Django?
penjelasan: Migrasi database di Django seperti "sistem update otomatis" untuk struktur database. Tiap kali ada perubahan pada berkas model.py Django tidak langsung mengubahnya di database maka dari itu perlu menjalankan perintah python manage.py makemigrations terlebih dahulu yang akan membuat "rencana perubahan" dalam bentuk file migrasi, kemudian jalankan python manage.py migrate untuk benar-benar menerapkan perubahan tersebut ke database. 

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
penjelasan: Django mudah dipahami untuk pemula. Konsep pemisahan tugas (MVT) membatu membangun website menjadi lebih mudah. Pada semester satu kita sudah mempelajari bahasa pemrogaraman python yang sintaksnya cukup mudah untuk dipahami dan ini juga linier dengan Django yang menggunakan bahasa pemrograman yang sama. 

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
feedback: Penjelasan di tutorial sudah sangat baik, tetapi memang sebaiknya dilakukan secara offline karena interaksi dengan para asdos menjadi lebih mudah