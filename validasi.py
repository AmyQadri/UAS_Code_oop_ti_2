# Import modul re untuk menggunakan regular expression
import re

# Pembuatan class validasi
class validasi:
    # Definisikan pola regex untuk validasi jam dengan format 09:00
    __jam = r"^([0-1][0-9]|2[0-3]):[0-5][0-9]$"
    # Definisikan pola regex untuk validasi durasi jam dengan format 08:00-12:00
    __durasi_jam = r"^([0-1][0-9]|2[0-3]):[0-5][0-9]-([0-1][0-9]|2[0-3]):[0-5][0-9]$"
    # Definisikan pola regex untuk validasi tanggal dengan format 2004/01/01
    __tanggal = r"^\d{4}[- /](0[1-9]|1[012])[- /](0[1-9]|[12][0-9]|3[01])$"

    # Pembuatan method untuk validasi jam
    def validasi_jam(jam):
        # Cek apakah jam sesuai dengan pola regex __jam
        if re.match(validasi.__jam, jam):
            return True
        else:
            return False

    # Pembuatan method untuk validasi durasi jam
    def validasi_durasi_jam(durasi):
        # Cek apakah durasi sesuai dengan pola regex __durasi_jam
        if re.match(validasi.__durasi_jam, durasi):
            return True
        else:
            return False

    # Pembuatan method untuk validasi tanggal
    def validasi_tanggal(tanggal):
        # Cek apakah tanggal sesuai dengan pola regex __tanggal
        if re.match(validasi.__tanggal, tanggal):
            return True
        else:
            return False

    # Pembuatan method untuk validasi umur
    def validasi_umur(tanggal_sekarang, tanggal_lahir):
        # Pisahkan tanggal sekarang berdasarkan tanda strip (-)
        temp1 = tanggal_sekarang.split("-")
        # Pisahkan tanggal lahir berdasarkan tanda strip (-)
        temp2 = tanggal_lahir.split("-")

        # Konversi tahun, bulan, dan hari dari string ke integer untuk tanggal sekarang
        tahun = int(temp1[0])
        bulan = int(temp1[1])
        hari = int(temp1[2])

        # Konversi tahun, bulan, dan hari dari string ke integer untuk tanggal lahir
        tahun_lahir = int(temp2[0])
        bulan_lahir = int(temp2[1])
        hari_lahir = int(temp2[2])

        # Hitung umur berdasarkan perbedaan tahun
        umur = tahun - tahun_lahir
        # Kurangi umur satu tahun jika bulan atau hari sekarang lebih kecil dari bulan atau hari lahir
        if bulan < bulan_lahir or (bulan == bulan_lahir and hari < hari_lahir):
            umur -= 1
        return umur
