print("Program menghitung luas dan Volume Prisma Segitiga")
"""
Programmer : Azis Husain
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

# Nilai
Sisi = 7
LuasAlas = 15
TinggiPrisma = 5
TinggiSegitiga = 4
LuasSegitiga = 18

# Rumus
LuasSelimutPrismaSegitiga = ( Sisi + Sisi + Sisi ) * TinggiPrisma
LuasPermukaanPrismaSegitiga = LuasSelimutPrismaSegitiga + 2 * LuasSegitiga
VolumePrismaSegitiga = 1/2 * LuasAlas * TinggiPrisma * TinggiSegitiga

# Output
print("Luas Selimut Prisma Segitiga :", LuasSelimutPrismaSegitiga)
print("LuasPermukaanPrismaSegitiga :", LuasPermukaanPrismaSegitiga)
print("Volume Prisma Segitiga :", VolumePrismaSegitiga)