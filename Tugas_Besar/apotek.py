from db import DBConnection as mydb

class Apotek:

    def __init__(self):
        self.__id = None
        self.__no_inv = None
        self.__nama_obat = None
        self.__jumlah_pembelian = None
        self.__harga = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def no_inv(self):
        return self.__no_inv

    @no_inv.setter
    def no_inv(self, value):
        self.__no_inv = value

    @property
    def nama_obat(self):
        return self.__nama_obat

    @nama_obat.setter
    def nama_obat(self, value):
        self.__nama_obat = value

    @property
    def jumlah_pembelian(self):
        return self.__jumlah_pembelian

    @jumlah_pembelian.setter
    def jumlah_pembelian(self, value):
        self.__jumlah_pembelian = value
    
    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__no_inv, self.__nama_obat, self.__jumlah_pembelian, self.__harga)
        print(val)
        sql = "INSERT INTO apotek (no_inv, nama_obat, jumlah_pembelian, harga) VALUES"+ str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__no_inv, self.__nama_obat, self.__jumlah_pembelian, self.__harga, id)
        sql = "UPDATE apotek SET no_inv = %s, nama_obat = %s, qty = %s WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateByno_inv(self, no_inv):
        self.conn = mydb()
        val = (self.__nama_obat, self.__jumlah_pembelian, self.__harga, no_inv)
        sql = "UPDATE apotek SET nama_obat = %s, jumlah_pembelian = %s, harga = %s WHERE no_inv = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM apotek WHERE id = %s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def deleteByno_inv(self, no_inv):
        self.conn = mydb()
        sql = "DELETE FROM apotek WHERE no_inv='" + str(no_inv) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def getById(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM apotek WHERE id = %s"
        self.result = self.conn.findOne(sql, (id,))
        self.__no_inv = self.result[1]
        self.__nama_obat = self.result[2]
        self.__jumlah_pembelian = self.result[3]
        self.__harga = self.result[4]
        self.conn.disconnect()
        return self.result

    def getByno_inv(self, no_inv):
        a = str(no_inv)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM apotek WHERE no_inv = %s"
        self.result = self.conn.findOne(sql, (b,))
        if self.result is not None:
            self.__no_inv = self.result[1]
            self.__nama_obat = self.result[2]
            self.__jumlah_pembelian = self.result[3]
            self.__harga = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__no_inv = ''
            self.__nama_obat = ''
            self.__jumlah_pembelian = ''
            self.__harga = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM apotek"
        self.result = self.conn.findAll(sql)
        return self.result

    def insert(self, sql, val):
        try:
            # Mengeksekusi kueri SQL untuk memasukkan data ke dalam database
            self.cursor.execute(sql, val)
            # Melakukan commit perubahan ke database
            self.conn.commit()
            # Mengembalikan jumlah baris yang terpengaruh oleh operasi insert
            return self.cursor.rowcount
        except mysql.connector.Error as err:
            # Menangani kesalahan jika terjadi
            print("Error:", err)
            # Mengembalikan nilai negatif untuk menunjukkan bahwa operasi insert gagal
            return -1


A = Apotek()
no_inv = '4444'
A.deleteByno_inv(no_inv)
B = A.getAllData()
print(B)