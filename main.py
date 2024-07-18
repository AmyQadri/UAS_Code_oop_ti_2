from sistem_konser import sistem_konser

# Inisialisasi objek sistem_konser
my_sistem = sistem_konser()

# Definisi menu utama
menu = 0
while menu != 9:
    print("===============================")
    print("    Sistem Informasi Konser    ")
    print("===============================")
    print(" 1. Tampilkan data umum konser  ")
    print(" 2. Atur tanggal                ")
    print(" 3. Tambah tempat               ")
    print(" 4. Tambah band                 ")
    print(" 5. Tambah konser               ")
    print(" 6. Pemesanan tiket             ")
    print(" 7. Statistik penonton          ")
    print(" 8. Kredit                      ")
    print(" 9. Keluar                      ")
    print("===============================")
    try:
        menu = int(input("Masukan menu: "))
    except ValueError:
        print("Menu tidak valid!\n")
    else:
        if menu == 1:
            my_sistem.lihat_info_konser()
        elif menu == 2:
            my_sistem.atur_tanggal()
        elif menu == 3:
            my_sistem.tambah_tempat()
        elif menu == 4:
            my_sistem.tambah_band()
        elif menu == 5:
            my_sistem.tambah_konser()
        elif menu == 6:
            my_sistem.pemesanan_tiket()
        elif menu == 7:
            my_sistem.statistik_penonton()
        elif menu == 8:
            my_sistem.kredit()
        elif menu == 9:
            print("Terimakasih telah menggunakan aplikasi ini")
        else:
            print("Menu tidak valid!\n")
