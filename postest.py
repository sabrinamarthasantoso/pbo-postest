class LoginKasir:
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def validasiLogin(self):
        pass

    def logout(self):
        pass


class KoneksiDatabase:
    def __init__(self, host='', database='', userName='', password=''):
        self.host = host
        self.database = database
        self.userName = userName
        self.password = password

    def membukaKoneksi(self):
        pass

    def eksekusiQuerySelect(self):
        pass

    def eksekusiQueryInsert(self):
        pass

    def eksekusiQueryUpdate(self):
        pass

    def eksekusiQueryDelete(self):
        pass

    def tutupKoneksi(self):
        pass


class HitungPembayaran:
    def __init__(self, idMenu='', namaMenu='', harga=0, jumlah=0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = harga * jumlah

    def insertPembayaran(self):
        pass

    def updatePembayaran(self):
        pass

    def deleteDataPembayaran(self):
        pass

    def cariDataPembayaranByIdMenu(self):
        pass


class PembayaranTunai:
    def hitungTotalHarga(self, total):
        pass


class PembayaranByCard:
    def hitungTotalHarga(self, total):
        pass


class CetakStruk:
    def cetakStruk(self, noStruk='', totalHarga=0):
        pass


class TcetakStruk:
    def __init__(self, noStruk='', totalHarga=0):
        self.noStruk = noStruk
        self.totalHarga = totalHarga


class TabelHitungPembayaran:
    def __init__(self, idMenu='', namaMenu='', harga=0, jumlah=0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = harga * jumlah

    def setIdMenu(self, idMenu): 
        pass
    def getIdMenu(self): 
        pass
    def setNamaMenu(self, namaMenu): 
        pass
    def getNamaMenu(self): 
        pass
    def setHarga(self, harga): 
        pass
    def getHarga(self): 
        pass
    def setJumlah(self, jumlah): 
        pass
    def getJumlah(self): 
        pass
    def setTotalHarga(self, total): 
        pass
    def getTotalHarga(self): 
        pass


class TabelPembayaranByCard:
    def __init__(self, idCard='', jenisCard='', namaBank='', totalHarga=0):
        self.idCard = idCard
        self.jenisCard = jenisCard
        self.namaBank = namaBank
        self.totalHarga = totalHarga

    def setIdCard(self, idCard): 
        pass
    def getIdCard(self): 
        pass
    def setJenisCard(self, jenisCard): 
        pass
    def getJenisCard(self): 
        pass
    def setNamaBank(self, namaBank): 
        pass
    def getNamaBank(self): 
        pass
    def setTotalHarga(self, total): 
        pass
    def getTotalHarga(self): 
        pass


class Main:
    def uiLogin(self): 
        pass
    def uiMenu(self): 
        pass
    def uiHitungPembayaran(self): 
        pass
    def uiCetakStruk(self): 
        pass
    def main(self): 
        pass


if __name__ == "__main__":
    kasir1 = LoginKasir("admin", "1234")
    db1 = KoneksiDatabase("localhost", "db_kasir", "root", "")
    pesanan1 = HitungPembayaran("M01", "Nasi Goreng", 15000, 2)
    tunai = PembayaranTunai()
    card = PembayaranByCard()
    struk = CetakStruk()
    tStruk = TcetakStruk("S001", 30000)
    tabel = TabelHitungPembayaran("M01", "Nasi Goreng", 15000, 2)
    tabelCard = TabelPembayaranByCard("C01", "Debit", "BCA", 30000)

    app = Main()
    app.main()