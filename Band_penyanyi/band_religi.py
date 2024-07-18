# Import class band dari file band
from .band import band

# Pembuatan class band_religi yang menginherit nilai dari class band
# Jadi, class band_religi ini memiliki method dan atribut dari class band
class band_religi(band):
    # Pembuatan constructor dengan meminta user memasukkan 4 parameter saat membuat objek dari class band_religi
    # Parameter tersebut adalah nama, biaya, daftar, dan agama
    def __init__(self, nama, biaya, daftar, agama):
        # Method super() digunakan agar class band_religi dapat mengakses constructor dari class induknya yaitu band
        # Di sini kita mengirimkan lagi 3 nilai sesuai yang ada di class band, yang nilainya diambil dari constructor band_religi
        super().__init__(nama, biaya, daftar)
        # Buat atribut agama yang nilainya diambil dari constructor dan bersifat private
        self.__agama = agama

    # Buat method info_band, karena di class band ada abstract method ini
    # Jadi, kita harus menuliskan ulang method ini
    # Di sini, method ini mengembalikan nilai atribut agama
    def info_band(self):
        return self.__agama

    # Buat method getter untuk agama agar dapat diakses nilainya
    @property
    def agama(self):
        return self.__agama

    # Buat method setter agar atribut agama dapat diganti nilainya sesuai syarat yang berlaku
    @agama.setter
    def agama(self, agama):
        self.__agama = agama
