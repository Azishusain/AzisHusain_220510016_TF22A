import mysql.connector as mc

class DBConnection:

    def __init__(self):
        

        self.host = 'sql.freedb.tech' #Isi Dengan Host Anda sesuai yang ada di freedb
        self.port = 3306
        self.name = 'freedb_d32022pbo' #Isi databasename Anda sesuai yang ada di freedb
        self.user = 'freedb_azishusain' #Isi Username Anda sesuai yang ada di freedb
        self.password = 'B@vhzjk$hF6xGV9' #Isi Password Anda sesuai yang ada di freedb
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()
        
    @property
    def connection_status(self):
        return self.connected
    
    def connect(self):
        try:
            self.conn = mc.connect(host = self.host,
                                    port = self.port,
                                    database = self.name,
                                    user = self.user,
                                    password = self.password)

            self.connected = True
            self.cursor=self.conn.cursor()
        except mc.Error as e:
            self.connected = False
        return self.conn

    def disconnect(self):
        if(self.connected==True):
            self.conn.close
        else:
            self.conn = None

    def findOne(self, sql, val=None):
        self.connect()
        if val:
            self.cursor.execute(sql, val)
        else:
            self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result


    def findAll(self, sql, val=None):
        self.connect()
        if val:
            self.cursor.execute(sql, val)
        else:
            self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result


    def insert(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def update(self, sql, val):
        self.connect()  
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def delete(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def show(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    @property
    def info(self):
        if(self.connected==True):
            return "Server is running on " + self.host + ' using port ' + str(self.port)
        else:
            return "Server is offline."
A = DBConnection()
B = A.info
print(B)