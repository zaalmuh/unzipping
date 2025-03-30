# unzipping
Aplikasi sederhana untuk mengekstrak compressed file (zip dan rar) dari beberapa folder sekaligus, dapat digunakan untuk mengekstrak file terkompres pada beberapa folder di dalam satu folder utama, contoh:
```
├── Folder PR2
│   ├── PR2_Mahasiswa A
│   │   ├── PR2_Mahasiswa A.zip
│   ├── PR2_Mahasiswa B
│   │   ├── PR2_Mahasiswa B.zip
```
menjadi
```bash
├── Folder PR2
│   ├── PR2_Mahasiswa A
│   │   ├── PR2_Mahasiswa A.zip
│   │   ├── PR2_Mahasiswa A.pdf
│   ├── PR2_Mahasiswa B
│   │   ├── PR2_Mahasiswa B.zip
│   │   ├── PR2_Mahasiswa B.pdf
```

## Setup
1. Clone repository ke local computer anda
2. Tempatkan unzipping.py dan unzipping.bat pada satu folder
3. edit path pada aslab.bat dengan path yang diinginkan, default: "C:\aslab.py"
4. Untuk menjalankan program, pergi ke windows run, dapat dengan menggunakan shortcut Windows + R, kemudian ketikkan path untuk unzipping.bat, seperti "C:\unzipping.bat" diikuti dengan nama folder yang berisi kumpulan folder utama, contoh (berdasarkan folder di atas):
> C:\unzipping.bat "D:\Folder PR2"
atau jika default di C maka tidak perlu menggunakan path:
> unzipping "D:\Folder PR2"
4. Terdapat notifikasi bahwa proses ekstraksi telah selesai.

Selamat Mencoba!
