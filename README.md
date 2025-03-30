# unzipping
Aplikasi sederhana untuk mengekstrak compressed file (zip dan rar) dari beberapa folder sekaligus, dapat digunakan untuk mengekstrak file terkompres pada beberapa folder di dalam satu folder utama, contoh:
$ ./tree-md .
# Project tree

.
 * [tree-md](./tree-md)
 * [dir2](./dir2)
   * [file21.ext](./dir2/file21.ext)
   * [file22.ext](./dir2/file22.ext)
   * [file23.ext](./dir2/file23.ext)
 * [dir1](./dir1)
   * [file11.ext](./dir1/file11.ext)
   * [file12.ext](./dir1/file12.ext)
 * [file_in_root.ext](./file_in_root.ext)
 * [README.md](./README.md)
 * [dir3](./dir3)


## Setup
1. Clone repository ke local computer anda
2. Tempatkan unzipping.py dan unzipping.bat pada satu folder
3. edit path pada aslab.bat dengan path yang diinginkan, default: "C:\aslab.py"
4. Untuk menjalankan program, pergi ke windows run, dapat dengan menggunakan shortcut Windows + R, kemudian ketikkan path untuk unzipping.bat, seperti "C:\unzipping.bat" diikuti dengan nama folder yang berisi kumpulan folder dengan , contoh:
> C:\unzipping.bat "D:\Folder berisi kumpulan folder yang memiliki file zip di dalamnya"
atau jika default di C maka tidak perlu menggunakan path:
> unzipping "D:\Folder berisi kumpulan folder yang memiliki file zip di dalamnya"
4. Terdapat notifikasi bahwa proses ekstraksi telah selesai.

Selamat Mencoba!
