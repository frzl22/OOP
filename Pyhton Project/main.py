"""
Program utama demonstrasi OOP
Menerapkan: Inheritance, Enkapsulasi, Instansiasi
"""

from models.kendaraan import Kendaraan, Mobil

def main():
    print("=== APLIKASI DEMONSTRASI OOP ===\n")
    
    # ========================
    # 1. INSTANSIASI OBJEK
    # ========================
    print("1. INSTANSIASI OBJEK")
    print("-" * 30)
    
    # Instansiasi dari Kelas Induk
    print("a) Objek dari Kelas Induk (Kendaraan):")
    motor = Kendaraan("Honda", 2022, "Merah", 0, "Bensin")
    print(f"✓ Berhasil membuat objek: {motor.info_kendaraan()}")
    
    # Instansiasi dari Kelas Anak  
    print("\nb) Objek dari Kelas Anak (Mobil - Inheritance):")
    mobil_saya = Mobil("Toyota", 2023, "Hitam", 0, "Bensin", 4, "SUV")
    print(f"✓ Berhasil membuat objek: {mobil_saya.info_lengkap()}")
    
    # ========================
    # 2. DEMONSTRASI METHOD
    # ========================
    print("\n2. DEMONSTRASI METHOD")
    print("-" * 30)
    
    print("a) Method dari Kelas Induk:")
    print(f"   - Klakson: {motor.klakson()}")
    print(f"   - Percepat: {motor.percepat(40)}")
    print(f"   - Rem: {motor.rem()}")
    
    print("\nb) Method dari Kelas Anak:")
    print(f"   - Buka pintu: {mobil_saya.buka_pintu(1)}")
    print(f"   - Nyalakan AC: {mobil_saya.nyalakan_ac(22)}")
    print(f"   - Set kapasitas: {mobil_saya.set_kapasitas_mesin(1500)}")
    print(f"   - Info lengkap: {mobil_saya.info_lengkap()}")
    
    # ========================
    # 3. DEMONSTRASI ENKAPSULASI
    # ========================
    print("\n3. DEMONSTRASI ENKAPSULASI")
    print("-" * 30)
    
    mobil_demo = Mobil("Honda", 2024, "Biru", 0, "Bensin", 5, "Sedan")
    
    print("a) Public attribute (bisa diakses langsung):")
    print(f"   - Warna: {mobil_demo.warna}")
    
    print("\nb) Protected attribute (seharusnya tidak diakses langsung):")
    print(f"   - Merk: {mobil_demo._merk}")
    
    print("\nc) Private attribute (TIDAK bisa diakses langsung):")
    try:
        print(f"   - Tahun: {mobil_demo.__tahun_produksi}")
    except AttributeError as e:
        print(f"   ✗ Error: {e}")
    
    print("\nd) Akses private attribute melalui getter/setter:")
    print(f"   - Get tahun: {mobil_demo.get_tahun_produksi()}")
    print(f"   - Set tahun: {mobil_demo.set_tahun_produksi(2025)}")
    print(f"   - Tahun sekarang: {mobil_demo.get_tahun_produksi()}")
    
    # ========================
    # 4. SCENARIO REAL WORLD
    # ========================
    print("\n4. SCENARIO REAL WORLD")
    print("-" * 30)
    
    mobil_keluarga = Mobil("Toyota", 2023, "Putih", 0, "Bensin", 4, "MPV")
    
    print("Aktivitas sehari-hari dengan mobil keluarga:")
    activities = [
        "Pergi ke kantor...",
        mobil_keluarga.klakson(),
        mobil_keluarga.percepat(20),
        "Macet...",
        mobil_keluarga.rem(),
        "Sampai di kantor",
        mobil_keluarga.buka_pintu(1),
        mobil_keluarga.nyalakan_ac(23),
        "Pulang ke rumah...",
        mobil_keluarga.percepat(15),
        mobil_keluarga.rem()
    ]
    
    for activity in activities:
        print(f"   • {activity}")
    
    # ========================
    # 5. SUMMARY
    # ========================
    print("\n5. SUMMARY KONSEP OOP YANG DITERAPKAN")
    print("-" * 40)
    print("✓ INHERITANCE: Mobil mewarisi dari Kendaraan")
    print("✓ ENKAPSULASI: Public, protected, private attributes") 
    print("✓ INSTANSIASI: Pembuatan objek dari kelas")
    print("✓ METHOD: Behavior/fungsi dalam kelas")
    print("✓ ATTRIBUTE: Data/properti dalam kelas")
    
    print(f"\nTotal objek yang dibuat: 4 objek")
    print("Program selesai!")

if __name__ == "__main__":
    main()