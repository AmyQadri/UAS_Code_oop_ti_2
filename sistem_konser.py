from validasi import validasi  # Import modul validasi untuk validasi data
from tempat import tempat  # Import kelas tempat dari modul tempat
from konser import konser  # Import kelas konser dari modul konser
from penonton import penonton  # Import kelas penonton dari modul penonton
from Band_penyanyi.penyanyi import penyanyi  # Import kelas penyanyi dari submodul Band_penyanyi
from Band_penyanyi.band_religi import band_religi  # Import kelas band_religi dari submodul Band_penyanyi
from Band_penyanyi.band_nonreligi import band_nonreligi  # Import kelas band_nonreligi dari submodul Band_penyanyi
from multimethod import multimethod  # Import modul multimethod untuk mendukung metode overloading
import os  # Import modul os untuk operasi sistem

class sistem_konser:
    def __init__(self):  # Inisialisasi objek sistem_konser
        self.__tanggal = None  # Variabel private untuk menyimpan tanggal
        self.__daftar_tempat = []  # Variabel private untuk menyimpan daftar tempat
        self.__daftar_band = []  # Variabel private untuk menyimpan daftar band
        self.__daftar_konser = []  # Variabel private untuk menyimpan daftar konser
        self.__daftar_penonton = []  # Variabel private untuk menyimpan daftar penonton
    
    def lihat_info_konser(self):  # Metode untuk melihat informasi konser
        if len(self.__daftar_konser) == 0:  # Jika tidak ada konser di daftar
            print("\nTidak ada konser untuk saat ini\n")  # Tampilkan pesan bahwa tidak ada konser
        else:
            self.lihat_daftar_konser()  # Tampilkan daftar konser
            try:
                pilih_konser = int(input("Pilih konser: "))  # Memilih konser berdasarkan input user
            except ValueError:
                print("Input tidak valid!\n")  # Pesan jika input tidak valid
            else:
                konser_dipilih = self.__daftar_konser[pilih_konser-1].nama_konser  # Ambil nama konser yang dipilih
                print(konser_dipilih)  # Tampilkan nama konser
                print(f"Total penjualan tiket: {self.jumlah_tiket_penonton(konser_dipilih)} tiket")  # Tampilkan total penjualan tiket
                print(f"Total jumlah penonton: {self.jumlah_tiket_penonton(konser_dipilih)} orang\n")  # Tampilkan total jumlah penonton

    def atur_tanggal(self):  # Metode untuk mengatur tanggal
        print("\nFormat tanggal: 2024-12-31")  # Tampilkan format tanggal yang benar
        tanggal = input("Masukan tanggal: ")  # Input tanggal dari user
        if validasi.validasi_tanggal(tanggal):  # Validasi tanggal
            self.__tanggal = tanggal  # Set tanggal jika valid
        else:
            print("Format tanggal tidak valid!\n")  # Tampilkan pesan jika format tanggal tidak valid

    def tambah_tempat(self):  # Metode untuk menambah tempat
        nama = input("\nNama tempat: ")  # Input nama tempat
        alamat = input("Alamat tempat: ")  # Input alamat tempat
        try:
            kapasitas = int(input("Kapasitas tempat: "))  # Input kapasitas tempat
        except ValueError:
            print("Input tidak valid!\n")  # Pesan jika input tidak valid
        else:
            self.daftar_tempat.append(tempat(nama,alamat,kapasitas))  # Tambah tempat ke daftar
            print("Tempat telah ditambahkan\n")  # Pesan konfirmasi tempat telah ditambahkan

    def tambah_band(self):  # Metode untuk menambah band
        temp = []  # List sementara untuk penyanyi
        try:
            nama_band = input("\nNama band: ")  # Input nama band
            jumlah_penyanyi = int(input("Jumlah penyanyi: "))  # Input jumlah penyanyi
            for i in range(jumlah_penyanyi):  # Loop untuk input nama penyanyi
                nama_penyanyi = input(f"Nama penyanyi {i+1}: ")  # Input nama penyanyi
                temp.append(penyanyi(nama_penyanyi))  # Tambah penyanyi ke list
            biaya = int(input("Biaya panggung: "))  # Input biaya panggung
            print("1.Religi\n2.Non-religi")  # Pilihan tipe band
            tipe_band = int(input("Pilih tipe band: "))  # Input pilihan tipe band
            if tipe_band == 1:
                agama = input("Agama band: ")  # Input agama band
                self.tambah_band_multi(nama_band,biaya,temp,agama)  # Tambah band religi
                print("Band telah ditambahkan\n")  # Pesan konfirmasi band telah ditambahkan
            elif tipe_band == 2:
                genre = ["Rock","Pop","Metal"]  # List genre band
                print("Genre Band:\n1.Rock\n2.Pop\n3.Metal")  # Pilihan genre band
                pilih_genre = int(input("Pilih genre: "))  # Input pilihan genre band
                if pilih_genre in [1,2,3]:
                    self.tambah_band_multi(nama_band,biaya,temp,genre[pilih_genre-1])  # Tambah band non-religi
                    print("Band telah ditambahkan\n")  # Pesan konfirmasi band telah ditambahkan
                else:
                    print("Input tidak valid!\n")  # Pesan jika input tidak valid
            else:
                print("Input tidak valid!\n")  # Pesan jika input tidak valid
        except ValueError:
            print("Input tidak valid!\n")  # Pesan jika input tidak valid
    
    def tambah_konser(self):  # Metode untuk menambah konser
        if len(self.daftar_tempat) == 0 or len(self.daftar_band) == 0:  # Cek apakah tempat dan band telah diinput
            print("\nHarap masukan tempat atau band terlebih dahulu!\n")  # Pesan untuk input tempat atau band terlebih dahulu
        else:
            try:
                temp1 = []  # List sementara untuk band
                nama_konser = input("\nNama konser: ")  # Input nama konser
                self.lihat_daftar_tempat()  # Tampilkan daftar tempat
                pilih_tempat = int(input("Pilih tempat: "))  # Input pilihan tempat
                jumlah_band = int(input("Jumlah band tampil: "))  # Input jumlah band tampil
                if jumlah_band > len(self.daftar_band):  # Cek apakah jumlah band cukup
                    print("Jumlah band pada sistem tidak mencukupi\n")  # Pesan jika jumlah band tidak mencukupi
                else:
                    self.lihat_daftar_band()  # Tampilkan daftar band
                    for i in range(jumlah_band):  # Loop untuk input band yang tampil
                        pilih_band = int(input(f"Pilih band {i+1}: "))  # Input pilihan band
                        temp1.append(self.__daftar_band[pilih_band-1])  # Tambah band ke list sementara
                    print("Format yang benar: Tanggal: 2024-12-31, Jam: 23:59, Durasi Jam: 23:59-00:00")  # Tampilkan format yang benar
                    tanggal_konser = input("Tanggal konser: ")  # Input tanggal konser
                    jam_konser = input("Jam konser: ")  # Input jam konser
                    lama_konser = input("Durasi konser: ")  # Input durasi konser
                    if (validasi.validasi_tanggal(tanggal_konser) and validasi.validasi_jam(jam_konser)) and validasi.validasi_durasi_jam(lama_konser):  # Validasi tanggal, jam, dan durasi konser
                        temp2 = 0  # Variabel sementara untuk biaya panggung
                        for i in(temp1):  # Loop untuk menghitung total biaya panggung
                            temp2 += i.biaya_panggung  # Tambah biaya panggung ke total
                            i.total_pendapatan += i.biaya_panggung  # Tambah total pendapatan band
                        harga_tiket = ((temp2/self.daftar_tempat[pilih_tempat-1].kapasitas)*20)  # Hitung harga tiket
                        self.daftar_konser.append(konser(nama_konser,self.daftar_tempat[pilih_tempat-1],temp1,tanggal_konser,jam_konser,lama_konser,harga_tiket))  # Tambah konser ke daftar konser
                        print("Konser telah ditambahkan\n")  # Pesan konfirmasi konser telah ditambahkan
                    else:
                        print("Format tanggal atau jam salah!\n")  # Pesan jika format tanggal atau jam salah
            except ValueError:
                print("Input tidak valid!\n")  # Pesan jika input tidak valid
    
    def pemesanan_tiket(self):  # Metode untuk pemesanan tiket
        if len(self.daftar_konser) == 0:  # Cek apakah ada konser di daftar
            print("\nTidak ada konser untuk saat ini\n")  # Pesan jika tidak ada konser
        else:
            try:
                if self.__tanggal:  # Cek apakah tanggal telah diatur
                    self.lihat_daftar_konser()  # Tampilkan daftar konser
                    pilih_konser = int(input("Pilih konser: "))  # Input pilihan konser
                    nama_penonton = input("Nama penonton: ")  # Input nama penonton
                    print("Format tanggal: 2024-12-31")  # Tampilkan format tanggal yang benar
                    tanggal_lahir = input("Tanggal lahir: ")  # Input tanggal lahir
                    if validasi.validasi_tanggal(tanggal_lahir):  # Validasi tanggal lahir
                        umur = validasi.validasi_umur(self.__tanggal,tanggal_lahir)  # Hitung umur penonton
                        if umur > 12 and umur < 89:  # Cek apakah umur memenuhi syarat
                            konser_dipilih = self.__daftar_konser[pilih_konser-1]  # Ambil konser yang dipilih
                            harga_tiket = konser_dipilih.harga_tiket  # Ambil harga tiket konser
                            temp = penonton(nama_penonton,tanggal_lahir,self.__tanggal)  # Buat objek penonton baru
                            temp.daftar_tiket = konser_dipilih  # Tambahkan konser ke daftar tiket penonton
                            self.__daftar_penonton.append(temp)  # Tambahkan penonton ke daftar penonton
                            self.hitung_diskon(konser_dipilih.tanggal_konser,harga_tiket)  # Hitung diskon berdasarkan tanggal konser
                        else:
                            print("Maaf umur anda tidak memenuhi persyaratan\n")  # Pesan jika umur tidak memenuhi syarat
                    else:
                        print("Format tanggal lahir salah!\n")  # Pesan jika format tanggal lahir salah
                else:
                    print("Atur tanggal terlebih dahulu!\n")  # Pesan jika tanggal belum diatur
            except ValueError:
                print("Input tidak valid!\n")  # Pesan jika input tidak valid
    
    def satistik_penonton(self):  # Metode untuk statistik penonton
        if len(self.__daftar_konser) == 0:  # Cek apakah ada konser di daftar
            print("\nTidak ada konser untuk saat ini\n")  # Pesan jika tidak ada konser
        else:
            if len(self.__daftar_penonton) == 0:  # Cek apakah ada penonton di daftar
                print("\nBelum ada tiket yang terjual saat ini\n")  # Pesan jika belum ada tiket terjual
            else:
                self.banyak_sedikit()  # Hitung konser dengan penonton paling banyak dan paling sedikit
                self.rata_rata_umur()  # Hitung rata-rata umur penonton

    def kredit(self):  # Metode untuk kredit
        with open('__pycache__/dont_touch_this.txt', 'r', encoding='utf-8') as file:  # Buka file kredit
            konten = file.read()  # Baca konten file kredit
            os.system("cls")  # Clear layar
            print(konten)  # Tampilkan konten file kredit
            n = input("\nPress enter to continue...")  # Menunggu input enter dari user
            os.system("cls")  # Clear layar setelah user menekan enter

    @property
    def tanggal(self):  # Property untuk tanggal
        return self.__tanggal  # Mengembalikan tanggal

    @tanggal.setter
    def tanggal(self,tanggal):  # Setter untuk tanggal
        if validasi.validasi_tanggal(tanggal):  # Validasi tanggal
            self.__tanggal = tanggal  # Set tanggal
            print("Tanggal telah di ganti\n")  # Pesan konfirmasi tanggal telah diubah
        else:
            print("Format tanggal tidak valid\n")  # Pesan jika format tanggal tidak valid

    @property
    def daftar_tempat(self):  # Property untuk daftar tempat
        return self.__daftar_tempat  # Mengembalikan daftar tempat

    @daftar_tempat.setter
    def daftar_tempat(self,lokasi):  # Setter untuk daftar tempat
        if isinstance(lokasi, tempat):  # Cek apakah lokasi merupakan objek tempat
            print("Tempat tidak valid!")  # Pesan jika tempat tidak valid
        else:
            self.__daftar_tempat = lokasi  # Set daftar tempat

    @property
    def daftar_band(self):  # Property untuk daftar band
        return self.__daftar_band  # Mengembalikan daftar band

    @daftar_band.setter
    def daftar_band(self,band):  # Setter untuk daftar band
        if isinstance(band, (band_religi,band_nonreligi)):  # Cek apakah band merupakan objek band_religi atau band_nonreligi
            print("Tempat tidak valid!")  # Pesan jika band tidak valid
        else:
            self.__daftar_band = band  # Set daftar band

    @property
    def daftar_konser(self):  # Property untuk daftar konser
        return self.__daftar_konser  # Mengembalikan daftar konser

    @daftar_konser.setter
    def daftar_konser(self,obj):  # Setter untuk daftar konser
        if isinstance(obj, konser):  # Cek apakah objek merupakan konser
            print("Konser tidak valid!")  # Pesan jika konser tidak valid
        else:
            self.__daftar_konser = obj  # Set daftar konser

    @property
    def daftar_penonton(self):  # Property untuk daftar penonton
        return self.__daftar_penonton  # Mengembalikan daftar penonton

    @daftar_penonton.setter
    def daftar_penonton(self,obj):  # Setter untuk daftar penonton
        if isinstance(obj,penonton):  # Cek apakah objek merupakan penonton
            print("Penonton tidak valid!")  # Pesan jika penonton tidak valid
        else:
            self.__daftar_penonton = obj  # Set daftar penonton

    @multimethod
    def tambah_band_multi(self,nama_band:str,biaya_panggung:int,penyanyi:list,agama:str):  # Metode overloading untuk menambah band religi
        self.daftar_band.append(1(nama_band,biaya_panggung,penyanyi,agama))  # Tambah band religi ke daftar band

    @multimethod
    def tambah_band_multi(self,nama_band:str,biaya_panggung:int,penyanyi:list,genre:str):  # Metode overloading untuk menambah band non-religi
        self.daftar_band.append(band_nonreligi(nama_band,biaya_panggung,penyanyi,genre))  # Tambah band non-religi ke daftar band

    def lihat_daftar_konser(self):  # Metode untuk menampilkan daftar konser
        print("\nDaftar konser:\n")  # Tampilkan judul daftar konser
        for index1, i in enumerate((self.__daftar_konser)):  # Loop untuk menampilkan daftar konser
            print(f"{index1+1}.{i.nama_konser}")  # Tampilkan nama konser dengan nomor urut

    def jumlah_tiket_penonton(self,obj):  # Metode untuk menghitung jumlah tiket penonton
        total = 0  # Variabel total tiket
        for i in self.__daftar_penonton:  # Loop untuk menghitung total tiket
            for j in i.daftar_tiket:  # Loop untuk mencari tiket dari daftar penonton
                if j.nama_konser == obj:  # Jika nama konser sama dengan yang dicari
                    total += 1  # Tambahkan jumlah tiket
        return total  # Mengembalikan total tiket

    def lihat_daftar_tempat(self):  # Metode untuk menampilkan daftar tempat
        for index1, i in enumerate(self.daftar_tempat):  # Loop untuk menampilkan daftar tempat
            print(f"{index1+1}.{i.nama_tempat}")  # Tampilkan nama tempat dengan nomor urut

    def lihat_daftar_band(self):  # Metode untuk menampilkan daftar band
        for index1, i in enumerate(self.daftar_band):  # Loop untuk menampilkan daftar band
            print(f"{index1+1}.{i.nama_band}")  # Tampilkan nama band dengan nomor urut

    def hitung_diskon(self,tanggal_konser,harga_tiket):  # Metode untuk menghitung diskon berdasarkan tanggal konser
        temp1 = self.__tanggal.split("-")  # Split tanggal saat ini
        temp2 = tanggal_konser.split("-")  # Split tanggal konser
        if ((temp1[0] == temp2[0]) and (int(temp2[1]) - int(temp1[1]) <= 1)):  # Cek apakah tahun sama dan bulan kurang dari satu
            print(f"Diskon 10%, Rp. {harga_tiket*10/100}\n")  # Diskon 10%
        elif ((temp1[0] == temp2[0]) and (int(temp2[1]) - int(temp1[1]) >= 1)):  # Cek apakah tahun sama dan bulan lebih dari satu
            print(f"Diskon 5%, Rp. {harga_tiket*5/100}\n")  # Diskon 5%
        else:
            print("Tidak ada diskon untuk anda\n")  # Tidak ada diskon

    def banyak_sedikit(self):  # Metode untuk mencari konser dengan penonton paling banyak dan paling sedikit
        index1 = 0  # Variabel sementara untuk konser dengan penonton paling banyak
        index2 = 0  # Variabel sementara untuk konser dengan penonton paling sedikit
        temp1 = 0  # Variabel sementara untuk penonton paling banyak
        temp2 = 0  # Variabel sementara untuk penonton paling sedikit
        for i in self.__daftar_konser:  # Loop untuk mencari konser dengan penonton paling banyak dan paling sedikit
            if len(self.jumlah_tiket_penonton(i.nama_konser)) > temp1:  # Jika jumlah tiket penonton lebih besar dari penonton paling banyak
                index1 = i  # Ambil konser dengan penonton paling banyak
                temp1 = len(self.jumlah_tiket_penonton(i.nama_konser))  # Update penonton paling banyak
            if len(self.jumlah_tiket_penonton(i.nama_konser)) < temp2:  # Jika jumlah tiket penonton lebih kecil dari penonton paling sedikit
                index2 = i  # Ambil konser dengan penonton paling sedikit
                temp2 = len(self.jumlah_tiket_penonton(i.nama_konser))  # Update penonton paling sedikit
        print(f"Konser dengan penonton paling banyak adalah {index1.nama_konser} dengan {temp1} penonton\n")  # Tampilkan konser dengan penonton paling banyak
        print(f"Konser dengan penonton paling sedikit adalah {index2.nama_konser} dengan {temp2} penonton\n")  # Tampilkan konser dengan penonton paling sedikit

    def rata_rata_umur(self):  # Metode untuk menghitung rata-rata umur penonton
        total = 0  # Variabel total umur
        for i in self.__daftar_penonton:  # Loop untuk menghitung total umur penonton
            total += validasi.validasi_umur(self.__tanggal,i.tanggal_lahir)  # Tambahkan umur penonton ke total
        print(f"Rata-rata umur penonton adalah {total/len(self.__daftar_penonton)} tahun\n")  # Tampilkan rata-rata umur penonton
