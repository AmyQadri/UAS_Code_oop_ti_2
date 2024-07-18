# Pembuatan class tempat
class tempat:
    # Pembuatan constructor dengan meminta user memasukkan 3 parameter saat membuat objek dari class tempat
    # Parameter tersebut adalah nama, alamat, dan kapasitas
    def __init__(self, nama, alamat, kapasitas):
        # Buat atribut nama_tempat yang nilainya diambil dari constructor dan bersifat private
        self.__nama_tempat = nama
        # Buat atribut alamat_lengkap yang nilainya diambil dari constructor dan bersifat private
        self.__alamat_lengkap = alamat
        # Buat atribut kapasitas yang nilainya diambil dari constructor dan bersifat private
        self.__kapasitas = kapasitas

    # Pembuatan method getter untuk nama_tempat agar dapat diakses nilainya
    @property
    def nama_tempat(self):
        return self.__nama_tempat
    
    # Pembuatan method setter untuk nama_tempat agar nilai atributnya dapat diganti sesuai syarat yang berlaku
    @nama_tempat.setter
    def nama_tempat(self, nama):
        # Validasi panjang nama tempat harus lebih dari empat huruf
        if len(nama) < 5:
            print("Nama tempat harus lebih dari empat huruf")
        else:
            self.__nama_tempat = nama

    # Pembuatan method getter untuk alamat_lengkap agar dapat diakses nilainya
    @property
    def alamat_lengkap(self):
        return self.__alamat_lengkap
    
    # Pembuatan method setter untuk alamat_lengkap agar nilai atributnya dapat diganti sesuai syarat yang berlaku
    @alamat_lengkap.setter
    def alamat_lengkap(self, alamat):
        # Validasi panjang alamat lengkap harus lebih dari empat huruf
        if len(alamat) < 5:
            print("Nama alamat harus lebih dari empat huruf")
        else:
            self.__alamat_lengkap = alamat

    # Pembuatan method getter untuk kapasitas agar dapat diakses nilainya
    @property
    def kapasitas(self):
        return self.__kapasitas
    
    # Pembuatan method setter untuk kapasitas agar nilai atributnya dapat diganti
    @kapasitas.setter
    def kapasitas(self, kapasitas):
        self.__kapasitas = kapasitas
