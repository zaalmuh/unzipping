# unzipping
Aplikasi sederhana untuk mengekstrak compressed file (zip dan rar) dari beberapa folder sekaligus, dapat digunakan untuk mengekstrak file terkompres pada beberapa folder di dalam satu folder utama, contoh:
$ ./tree-md .
 * [Pekerjaan Rumah 2](./tree-md)
 * [PR2_Mahasiswa A](./dir2)
   * [PR2_Mahasiswa A.zip](./dir2/file21.ext)
 * [PR2_Mahasiswa B](./dir2)
   * [PR2_Mahasiswa B.rar](./dir2/file21.ext)

menjadi
$ ./tree-md .
 * [Pekerjaan Rumah 2](./tree-md)
 * [PR2_Mahasiswa A](./dir2)
   * [PR2_Mahasiswa A.zip](./dir2/file21.ext)
   * [PR2_Mahasiswa A.pdf](./dir2/file21.ext)
 * [PR2_Mahasiswa B](./dir2)
   * [PR2_Mahasiswa B.rar](./dir2/file21.ext)
   * [PR2_Mahasiswa B.pdf](./dir2/file21.ext)

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
