# Sistem Manajemen Koleksi Buku Pribadi

Aplikasi web untuk mengelola koleksi buku pribadi menggunakan Django dan SQLite.

## Fitur Utama

- Manajemen Buku (CRUD)
- Manajemen Penulis
- Manajemen Penerbit
- Manajemen Rak Buku
- Penempatan Buku di Rak
- Pencarian dan Filter Buku
- Antarmuka Admin Django

## Struktur Database

Aplikasi menggunakan 5 model utama:

1. **Buku**
   - Judul, Penulis, Tahun Terbit, Penerbit
   - Genre, Jumlah Halaman, Sinopsis
   - Relasi dengan Rak Buku

2. **Penulis**
   - Nama Depan, Nama Belakang
   - Tanggal Lahir, Asal Negara

3. **Penerbit**
   - Nama Penerbit
   - Alamat, Kota

4. **RakBuku**
   - Nama Rak
   - Lokasi Rak

5. **PenempatanBuku**
   - Model perantara untuk relasi Buku-Rak
   - Tanggal Penempatan

## Cara Setup dan Menjalankan Proyek

1. Buat virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # atau
   .\venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan migrasi database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Buat superuser untuk akses admin:
   ```bash
   python manage.py createsuperuser
   ```

5. Jalankan server development:
   ```bash
   python manage.py runserver
   ```

6. Akses aplikasi di browser:
   - Aplikasi: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Teknologi yang Digunakan

- Django 5.0.2
- SQLite (Database)
- Bootstrap 5 (Frontend)
- Django Crispy Forms
- Python 3.x 