# Pembuatan class penyanyi
class penyanyi:
    # Pembuatan constructor dengan meminta user memasukkan 1 parameter saat membuat objek dari class penyanyi
    # Parameter tersebut adalah nama
    def __init__(self, nama):
        # Buat atribut nama_penyanyi yang nilainya diambil dari constructor dan bersifat private
        self.__nama_penyanyi = nama

    # Pembuatan method getter untuk nama_penyanyi agar dapat diakses nilainya
    @property
    def nama_penyanyi(self):
        return self.__nama_penyanyi
    
    # Pembuatan method setter untuk nama_penyanyi agar nilai atributnya dapat diganti sesuai syarat yang berlaku
    @nama_penyanyi.setter
    def nama_penyanyi(self, nama):
        # Validasi panjang nama penyanyi harus lebih dari empat huruf
        if len(nama) < 5:
            print("Nama penyanyi harus lebih dari empat huruf")
        else:
            self.__nama_penyanyi = nama
