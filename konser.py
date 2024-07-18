# Import class tempat dari file tempat
from tempat import tempat

# Import class band_religi dan band_nonreligi dari file band_religi dan band_nonreligi
from Band_penyanyi.band_religi import band_religi
from Band_penyanyi.band_nonreligi import band_nonreligi

# Import class validasi dari file validasi
from validasi import validasi

# Pembuatan class konser
class konser:
    # Pembuatan constructor dengan meminta user memasukkan 7 parameter saat membuat objek dari class konser
    # Parameter tersebut adalah nama, lokasi, daftar, tanggal, jam, durasi, dan harga
    def __init__(self, nama, lokasi, daftar, tanggal, jam, durasi, harga):
        # Buat atribut nama_konser yang nilainya diambil dari constructor dan bersifat private
        self.__nama_konser = nama
        # Buat atribut tempat_konser yang nilainya diambil dari constructor dan bersifat private
        self.__tempat_konser = lokasi
        # Buat atribut band_tampil yang nilainya diambil dari constructor dan bersifat private
        self.__band_tampil = daftar
        # Buat atribut tanggal_konser yang nilainya diambil dari constructor dan bersifat private
        self.__tanggal_konser = tanggal
        # Buat atribut jam_konser yang nilainya diambil dari constructor dan bersifat private
        self.__jam_konser = jam
        # Buat atribut lama_konser yang nilainya diambil dari constructor dan bersifat private
        self.__lama_konser = durasi
        # Buat atribut harga_tiket yang nilainya diambil dari constructor dan bersifat private
        self.__harga_tiket = harga

    # Pembuatan method __str__ untuk mengembalikan string representasi dari objek konser
    def __str__(self) -> str:
        # Mengembalikan informasi tentang nama konser, lokasi, waktu konser, dan daftar band
        return f"Nama konser: {self.__nama_konser}\nLokasi: {self.tempat_konser.nama_tempat}\nWaktu konser: {self.lama_konser}\nDaftar band:\n{self.lihat_daftar_band()}"

    # Pembuatan method lihat_daftar_band untuk mengembalikan daftar band yang tampil
    def lihat_daftar_band(self):
        # Inisialisasi variabel band sebagai string kosong
        band = ""
        # Looping melalui daftar band yang tampil
        for index1, i in enumerate(self.band_tampil):
            # Menambahkan nama band ke variabel band dengan format tertentu
            band += f"{index1 + 1}. {i.nama_band}\n"
        return band

    # Pembuatan method getter untuk nama_konser agar dapat diakses nilainya
    @property
    def nama_konser(self):
        return self.__nama_konser
    
    # Pembuatan method setter untuk nama_konser agar nilai atributnya dapat diganti sesuai syarat yang berlaku
    @nama_konser.setter
    def nama_konser(self, nama):
        # Validasi panjang nama konser harus lebih dari empat huruf
        if len(nama) < 5:
            print("Nama konser harus lebih dari empat huruf\n")
        else:
            self.__nama_konser = nama

    # Pembuatan method getter untuk tempat_konser agar dapat diakses nilainya
    @property
    def tempat_konser(self):
        return self.__tempat_konser
    
    # Pembuatan method setter untuk tempat_konser agar nilai atributnya dapat diganti
    @tempat_konser.setter
    def tempat_konser(self, lokasi):
        # Validasi apakah lokasi adalah instance dari tempat
        if isinstance(lokasi, tempat):
            self.__tempat_konser = lokasi
        else:
            print("Tempat konser tidak valid\n")

    # Pembuatan method getter untuk band_tampil agar dapat diakses nilainya
    @property
    def band_tampil(self):
        return self.__band_tampil
    
    # Pembuatan method setter untuk band_tampil agar nilai atributnya dapat diganti
    @band_tampil.setter
    def band_tampil(self, band):
        # Validasi apakah band adalah instance dari band_religi atau band_nonreligi
        if isinstance(band, (band_religi, band_nonreligi)):
            self.__band_tampil.append(band)
        else:
            print("Band tidak valid!\n")

    # Pembuatan method getter untuk tanggal_konser agar dapat diakses nilainya
    @property
    def tanggal_konser(self):
        return self.__tanggal_konser
    
    # Pembuatan method setter untuk tanggal_konser agar nilai atributnya dapat diganti
    @tanggal_konser.setter
    def tanggal_konser(self, tanggal):
        # Validasi format tanggal menggunakan class validasi
        if validasi.validasi_tanggal(tanggal):
            self.__tanggal_konser = tanggal
        else:
            print("Format tanggal tidak valid!\n")

    # Pembuatan method getter untuk jam_konser agar dapat diakses nilainya
    @property
    def jam_konser(self):
        return self.__jam_konser
    
    # Pembuatan method setter untuk jam_konser agar nilai atributnya dapat diganti
    @jam_konser.setter
    def jam_konser(self, jam):
        # Validasi format jam dengan menggunakan class validasi, dengan menggunakan regex. agar data nya format nya 09:00
        if validasi.validasi_jam(jam):
            self.__jam_konser = jam
        else:
            print("Format jam tidak valid!\n")

    # Pembuatan method getter untuk lama_konser agar dapat diakses nilainya
    @property
    def lama_konser(self):
        return self.__lama_konser
    
    # Pembuatan method setter untuk lama_konser agar nilai atributnya dapat diganti
    @lama_konser.setter
    def lama_konser(self, durasi):
        # Validasi format durasi jam menggunakan class validasi, dengan menggunakan regex. agar datanya format nya 01:00-03:00
        if validasi.__durasi_jam(durasi):
            self.__lama_konser = durasi
        else:
            print("Format durasi jam tidak valid!\n")

    # Pembuatan method getter untuk harga_tiket agar dapat diakses nilainya
    @property
    def harga_tiket(self):
        return self.__harga_tiket
    
    # Pembuatan method setter untuk harga_tiket agar nilai atributnya dapat diganti
    @harga_tiket.setter
    def harga_tiket(self, harga):
        self.__harga_tiket = harga
