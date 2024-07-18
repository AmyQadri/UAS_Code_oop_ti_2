# Mengimpor class 'validasi' dari modul 'validasi' untuk melakukan validasi data menggunakan regular expression.
from validasi import validasi

# Mengimpor class 'konser' dari modul 'konser'.
from konser import konser

# Definisikan class 'penonton' untuk merepresentasikan objek penonton.
class penonton:
    """
    Kelas 'penonton' digunakan untuk menyimpan informasi tentang penonton konser.

    Attributes:
    - nama_penonton (str): Nama lengkap dari penonton.
    - tanggal_lahir (str): Tanggal lahir penonton dalam format 'YYYY-MM-DD'.
    - tanggal_pemesanan (str): Tanggal saat penonton memesan tiket dalam format 'YYYY-MM-DD'.
    - daftar_tiket (list): Daftar tiket konser yang telah dibeli oleh penonton.

    Methods:
    - nama_penonton.setter: Setter untuk mengatur nama penonton dengan validasi panjang nama minimal lima karakter.
    - tanggal_lahir.setter: Setter untuk mengatur tanggal lahir penonton dengan validasi menggunakan fungsi 'validasi_tanggal'.
    - daftar_tiket.setter: Setter untuk menambahkan tiket ke daftar tiket penonton, dengan validasi bahwa tiket adalah instance dari kelas 'konser'.
    """

    def __init__(self, nama, tgl_lhr, tgl_pemesanan):
        """
        Inisialisasi objek 'penonton' dengan nama, tanggal lahir, tanggal pemesanan, dan daftar tiket kosong.

        Args:
        - nama (str): Nama lengkap dari penonton.
        - tgl_lhr (str): Tanggal lahir penonton dalam format 'YYYY-MM-DD'.
        - tgl_pemesanan (str): Tanggal saat penonton memesan tiket dalam format 'YYYY-MM-DD'.
        """
        self.__nama_penonton = nama
        self.__tanggal_lahir = tgl_lhr
        self.__tanggal_pemesanan = tgl_pemesanan
        self.__daftar_tiket = []

    @property
    def nama_penonton(self):
        """
        Metode getter untuk mengembalikan nama penonton.
        """
        return self.__nama_penonton 

    @nama_penonton.setter
    def nama_penonton(self, nama):
        """
        Metode setter untuk mengatur nama penonton. Memvalidasi bahwa nama memiliki minimal lima karakter.

        Args:
        - nama (str): Nama lengkap dari penonton.
        """
        if len(nama) < 5:
            print("Nama penonton harus lebih dari empat huruf")
        else:
            self.__nama_penonton = nama

    @property
    def tanggal_lahir(self):
        """
        Metode getter untuk mengembalikan tanggal lahir penonton.
        """
        return self.__tanggal_lahir

    @tanggal_lahir.setter
    def tanggal_lahir(self, tanggal):
        """
        Metode setter untuk mengatur tanggal lahir penonton. Memvalidasi format tanggal menggunakan fungsi 'validasi_tanggal' dari modul 'validasi'.

        Args:
        - tanggal (str): Tanggal lahir penonton dalam format 'YYYY-MM-DD'.
        """
        if validasi.validasi_tanggal(tanggal):
            print("Format tanggal lahir tidak valid!\n")
        else:
            self.__tanggal_lahir = tanggal

    @property
    def daftar_tiket(self):
        """
        Metode getter untuk mengembalikan daftar tiket yang dimiliki penonton.
        """
        return self.__daftar_tiket

    @daftar_tiket.setter
    def daftar_tiket(self, tiket):
        """
        Metode setter untuk menambahkan tiket ke daftar tiket penonton. Memvalidasi bahwa tiket merupakan instance dari kelas 'konser'.

        Args:
        - tiket (konser): Objek tiket konser yang akan ditambahkan ke daftar.
        """
        if isinstance(tiket, konser):
            self.__daftar_tiket.append(tiket)
        else:
            print("Tiket tidak valid!\n")


        