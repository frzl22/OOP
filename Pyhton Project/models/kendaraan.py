"""
Modul berisi kelas Kendaraan dan Mobil
Menerapkan konsep OOP: Inheritance, Enkapsulasi, Instansiasi
"""

class Kendaraan:
    """
    Kelas induk untuk representasi kendaraan umum
    
    Attributes:
        _merk (str): Merek kendaraan (protected)
        __tahun_produksi (int): Tahun produksi (private) 
        warna (str): Warna kendaraan (public)
        _kecepatan (int): Kecepatan saat ini (protected)
        bahan_bakar (str): Jenis bahan bakar (public)
    """
    
    def __init__(self, merk, tahun, warna, kecepatan, bahan_bakar):
        # 5 Attribut dengan Enkapsulasi
        self._merk = merk              # protected
        self.__tahun_produksi = tahun  # private
        self.warna = warna             # public
        self._kecepatan = kecepatan    # protected
        self.bahan_bakar = bahan_bakar # public
    
    # 4 Method (Behavior)
    def klakson(self):
        """Method untuk membunyikan klakson"""
        return "Beep! Beep!"
    
    def percepat(self, tambahan_kecepatan):
        """Method untuk menambah kecepatan"""
        self._kecepatan += tambahan_kecepatan
        return f"Kecepatan bertambah: {self._kecepatan} km/jam"
    
    def rem(self):
        """Method untuk mengerem"""
        self._kecepatan = 0
        return "Kendaraan berhenti"
    
    def info_kendaraan(self):
        """Method untuk menampilkan info kendaraan"""
        return f"Merk: {self._merk}, Warna: {self.warna}, Bahan Bakar: {self.bahan_bakar}"
    
    # Getter dan Setter untuk Enkapsulasi
    def get_tahun_produksi(self):
        """Getter untuk tahun produksi (private attribute)"""
        return self.__tahun_produksi
    
    def set_tahun_produksi(self, tahun_baru):
        """Setter untuk tahun produksi dengan validasi"""
        if tahun_baru > 1885:  # Validasi tahun
            self.__tahun_produksi = tahun_baru
            return f"Tahun produksi diupdate: {tahun_baru}"
        else:
            return "Tahun tidak valid!"


class Mobil(Kendaraan):
    """
    Kelas anak untuk representasi mobil
    Mewarisi dari kelas Kendaraan (Inheritance)
    
    Attributes tambahan:
        jumlah_pintu (int): Jumlah pintu mobil
        tipe_mobil (str): Tipe mobil (SUV, Sedan, dll)
        _kapasitas_mesin (int): Kapasitas mesin dalam CC (protected)
        transmisi (str): Jenis transmisi (manual/otomatis)
        sunroof (bool): Apakah memiliki sunroof
    """
    
    def __init__(self, merk, tahun, warna, kecepatan, bahan_bakar, jumlah_pintu, tipe_mobil):
        # Memanggil constructor parent class
        super().__init__(merk, tahun, warna, kecepatan, bahan_bakar)
        
        # 5 Attribut tambahan
        self.jumlah_pintu = jumlah_pintu
        self.tipe_mobil = tipe_mobil
        self._kapasitas_mesin = 0      # protected
        self.transmisi = ""
        self.sunroof = False
    
    # 4 Method tambahan
    def buka_pintu(self, nomor_pintu):
        """Method untuk membuka pintu tertentu"""
        if 1 <= nomor_pintu <= self.jumlah_pintu:
            return f"Pintu {nomor_pintu} terbuka"
        else:
            return f"Pintu {nomor_pintu} tidak tersedia"
    
    def nyalakan_ac(self, suhu):
        """Method untuk menyalakan AC"""
        return f"AC dinyalakan pada suhu {suhu}°C"
    
    def set_kapasitas_mesin(self, kapasitas):
        """Method untuk mengatur kapasitas mesin"""
        self._kapasitas_mesin = kapasitas
        return f"Kapasitas mesin diatur: {kapasitas} CC"
    
    def info_lengkap(self):
        """Method untuk menampilkan info lengkap mobil"""
        info_dasar = self.info_kendaraan()  # Memanggil method parent
        return f"{info_dasar}, Tipe: {self.tipe_mobil}, Pintu: {self.jumlah_pintu}"