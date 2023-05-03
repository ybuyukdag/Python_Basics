import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayı1 = QtWidgets.QLabel(self)
        self.lbl_sayı1.setText("Sayı 1: ")
        self.lbl_sayı1.move(50,30)

        self.txt_sayı1 = QtWidgets.QLineEdit(self)
        self.txt_sayı1.move(150,30)
        self.txt_sayı1.resize(200,32)

        self.lbl_sayı2 = QtWidgets.QLabel(self)
        self.lbl_sayı2.setText("Sayı 2: ")
        self.lbl_sayı2.move(50,80)

        self.txt_sayı2 = QtWidgets.QLineEdit(self)
        self.txt_sayı2.move(150,80)
        self.txt_sayı2.resize(200,32)

        self.btn_toplama = QtWidgets.QPushButton(self)
        self.btn_toplama.setText("Toplama")
        self.btn_toplama.move(150,130)
        self.btn_toplama.clicked.connect(self.hesapla)

        self.btn_cikarma = QtWidgets.QPushButton(self)
        self.btn_cikarma.setText("Çıkarma")
        self.btn_cikarma.move(150,170)
        self.btn_cikarma.clicked.connect(self.hesapla)

        self.btn_carpma = QtWidgets.QPushButton(self)
        self.btn_carpma.setText("Çarpma")
        self.btn_carpma.move(150,210)
        self.btn_carpma.clicked.connect(self.hesapla)

        self.btn_bolme = QtWidgets.QPushButton(self)
        self.btn_bolme.setText("Bölme")
        self.btn_bolme.move(150,250)
        self.btn_bolme.clicked.connect(self.hesapla)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Sonuç: ")
        self.lbl_result.move(150,290)

    def hesapla(self):
        sender = self.sender().text()

        if sender == "Toplama":
            result = int(self.txt_sayı1.text()) + int(self.txt_sayı2.text())
        elif sender == "Çıkarma":
            result = int(self.txt_sayı1.text()) - int(self.txt_sayı2.text())
        elif sender == "Çarpma":
            result = int(self.txt_sayı1.text()) * int(self.txt_sayı2.text())
        elif sender == "Bölme":
            result = int(self.txt_sayı1.text()) / int(self.txt_sayı2.text())

        self.lbl_result.setText("Sonuç: " + str(result))

    
    # def toplama(self):
    #     result = int(self.txt_sayı1.text()) + int(self.txt_sayı2.text())
    #     self.lbl_result.setText("Sonuç: "+ str(result))
    
    # def cikarma(self):
    #     result = int(self.txt_sayı1.text()) - int(self.txt_sayı2.text())
    #     self.lbl_result.setText("Sonuç: "+ str(result))

    # def carpma(self):
    #     result = int(self.txt_sayı1.text()) * int(self.txt_sayı2.text())
    #     self.lbl_result.setText("Sonuç: "+ str(result))
    
    # def bolme(self):
    #     result = int(self.txt_sayı1.text()) / int(self.txt_sayı2.text())
    #     self.lbl_result.setText("Sonuç: "+ str(result))

   

def app():
    app = QApplication(sys.argv)
    win = MainForm()

    win.show()
    sys.exit(app.exec_())

app()
