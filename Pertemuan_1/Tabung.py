print("Program menghitung luas dan Volume Tabung")
"""
Programmer : Azis Husain
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

# Nilai
Jarijari = 10
Tinggi = 15

# Rumus
LuasSelimutTabung = 2 * 3.14 * Jarijari * Tinggi
LuasPermukaanTabung = LuasSelimutTabung + 2 * 3.14 * Jarijari **2
VolumeTabung = 3.14 * Jarijari **2 * Tinggi

# Output
print("Luas Selimut Tabung:", LuasSelimutTabung)
print("Luas Permukaan Tabung:", LuasPermukaanTabung)
print("Volume Tabung:", VolumeTabung)