# Import ABC dan abstractmethod dari modul abc
# Gunanya supaya bisa menggunakan fungsi abstractmethod
from abc import ABC, abstractmethod

# Import class penyanyi dari file penyanyi
from .penyanyi import penyanyi

# Pembuatan class band yang menginherit dari ABC
# Gunanya menginherit dari ABC supaya kelas band ini bisa menggunakan fungsi abstractmethod
class band(ABC):
    # Pembuatan constructor dengan meminta user memasukkan 3 parameter saat membuat objek dari class band
    # Parameter tersebut adalah nama, biaya, dan daftar
    def __init__(self, nama, biaya, daftar):
        # Buat atribut nama_band yang nilainya diambil dari constructor dan bersifat private
        self.__nama_band = nama
        # Buat atribut daftar_penyanyi yang nilainya diambil dari constructor dan bersifat private
        self.__daftar_penyanyi = daftar
        # Buat atribut biaya_panggung yang nilainya diambil dari constructor dan bersifat private
        self.__biaya_panggung = biaya
        # Buat atribut total_pendapatan yang diinisialisasi dengan nilai 0 dan bersifat private
        self.__total_pendapatan = 0

    # Dekorator abstractmethod digunakan agar kelas ini bisa memiliki method abstract
    @abstractmethod
    # Pembuatan abstract method info_band
    # Kenapa harus info_band? Karena kita ingin setiap subclass dari band memiliki method ini
    def info_band(self):
        pass

    # Pembuatan method getter untuk nama_band agar dapat diakses nilainya
    @property
    def nama_band(self):
        return self.__nama_band
    
    # Pembuatan method setter untuk nama_band agar nilai atributnya dapat diganti sesuai syarat yang berlaku
    @nama_band.setter
    def nama_band(self, nama):
        # Validasi panjang nama band harus lebih dari empat huruf
        if len(nama) < 5:
            print("Nama band harus lebih dari empat huruf")
        else:
            self.__nama_band = nama

    # Pembuatan method getter untuk biaya_panggung agar dapat diakses nilainya
    @property
    def biaya_panggung(self):
        return self.__biaya_panggung
    
    # Pembuatan method setter untuk biaya_panggung agar nilai atributnya dapat diganti
    @biaya_panggung.setter
    def biaya_panggung(self, biaya):
        self.__biaya_panggung = biaya

    # Pembuatan method getter untuk total_pendapatan agar dapat diakses nilainya
    @property
    def total_pendapatan(self):
        return self.__total_pendapatan
    
    # Pembuatan method setter untuk total_pendapatan agar nilainya dapat ditambahkan
    @total_pendapatan.setter
    def total_pendapatan(self, pendapatan):
        self.__total_pendapatan += pendapatan

    # Pembuatan method getter untuk daftar_penyanyi agar dapat diakses nilainya
    @property
    def daftar_penyanyi(self):
        return self.__daftar_penyanyi
    
    # Pembuatan method setter untuk daftar_penyanyi agar nilai atributnya dapat diganti
    @daftar_penyanyi.setter
    def daftar_penyanyi(self, obj):
        # Validasi apakah obj adalah instance dari penyanyi
        if isinstance(obj, penyanyi):
            self.__daftar_penyanyi.append(penyanyi)
        else:
            print("Band tidak valid")
