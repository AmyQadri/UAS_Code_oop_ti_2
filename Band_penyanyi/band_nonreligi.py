# Import class band dari file band
from .band import band

# Pembuatan class band_nonreligi yang menginherit nilai dari class band
# Jadi, class band_nonreligi ini memiliki method dan atribut dari class band
class band_nonreligi(band):
    # Pembuatan constructor dengan meminta user memasukkan 4 parameter saat membuat objek dari class band_nonreligi
    # Parameter tersebut adalah nama, biaya, daftar, dan genre
    def __init__(self, nama, biaya, daftar, genre):
        # Method super() digunakan agar class band_nonreligi dapat mengakses constructor dari class induknya yaitu band
        # Di sini kita mengirimkan lagi 3 nilai sesuai yang ada di class band, yang nilainya diambil dari constructor band_nonreligi
        super().__init__(nama, biaya, daftar)
        # Buat atribut genre_band yang nilainya diambil dari constructor dan bersifat private
        self.__genre_band = genre
    
    # Buat method info_band, karena di class band ada abstract method ini
    # Jadi, kita harus menuliskan ulang method ini
    # Di sini, method ini mengembalikan nilai atribut genre_band
    def info_band(self):
        return self.__genre_band
    
    # Buat method getter untuk genre_band agar dapat diakses nilainya
    @property
    def genre_band(self):
        return self.__genre_band
    
    # Buat method setter agar atribut genre_band dapat diganti nilainya sesuai syarat yang berlaku
    @genre_band.setter
    def genre_band(self, genre):
        self.__genre_band = genre
