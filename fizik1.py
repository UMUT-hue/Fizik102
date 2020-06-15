from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt, QRect, pyqtSlot
from PyQt5.QtWidgets import *                                       #Modüller içe aktarılıyor
import time
import sys
from threading import Thread
import QT_designer.icons_rc                                         #Fotoğrafların içinde bulunduğu dosya
import math
class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.InitW()
        self.grids()
        self.labels()
        self.consols()                                          #Fonksiyonlar programın başlaasıyla başlıyorlar
        self.frames()
        self.buttonboxs()
        self.lineedits()
        self.connects()

    def InitW(self):
        self.setWindowTitle("Fizik 102")
        p = self.palette()                                          #Pencere için renk - isim veriyorum
        p.setColor(self.backgroundRole(), QtCore.Qt.color1)
        self.setPalette(p)

    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        paint.setRenderHint(QtGui.QPainter.Antialiasing)
        paint.drawRect(event.rect())

        paint.setPen(QPen(Qt.green,  8))
        paint.setBrush(QtCore.Qt.white)                             #Elektronun dönmesi için gösterilen yeşil çizgiyi tanımlıyorum
        paint.drawEllipse(QtCore.QRect(50, 50, 400, 400))

        paint.setPen(QPen(Qt.cyan,  8))
        paint.drawLine(250, 250, 450, 250)
        paint.end()

    def grids(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 500, 450, 450))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)              #Buradaki tanımladıklarım belli bir düzen oluşturmak için kulllanıyorum
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.gridLayoutWidget_2 = QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QRect(495, 500, 561, 321))          #Buradaki tanımladıklarım belli bir düzen oluşturmak için kulllanıyorum
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)



    def consols(self):
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(20)

        self.console_textbrowser = QtWidgets.QTextBrowser(self)
        self.palette = QtGui.QPalette()
        self.palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)                                   #Burada hesaplamaları gösteren konsolu tanımlıyorum
        self.console_textbrowser.setGeometry(QtCore.QRect(1080, 530, 700, 450))
        self.console_textbrowser.setPalette(self.palette)

        self.console_textbrowser.setFont(font)
        self.console_textbrowser.setObjectName("textBrowser_2")
        self.console_textbrowser.setStyleSheet('background-color: rgb(0, 0, 0)')

    def frames(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("World_Magnetic_Field_2015.pdf.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Magnetic_Field_Direction = QtWidgets.QFrame(self)
        self.Magnetic_Field_Direction.setGeometry(QtCore.QRect(500, 10, 450, 475))
        self.Magnetic_Field_Direction.setFrameShape(QtWidgets.QFrame.WinPanel)                                                      #Manyetik alanın yönünü gösteren fotoğrafı koyuyorum
        self.Magnetic_Field_Direction.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Magnetic_Field_Direction.setObjectName("frame")
        self.Magnetic_Field_Direction.setStyleSheet("""image: url(:/newPrefix/Capture.PNG);background-color : rgb(255, 255,0);""")

        self.Magnetic_Field_Map = QtWidgets.QFrame(self)
        self.Magnetic_Field_Map.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Magnetic_Field_Map.setGeometry(QtCore.QRect(960, 10, 950, 475))                                                     #Dünyada çeşitli konumlardaki manyetik alanı gösteren haritayı koyuyorum
        self.Magnetic_Field_Map.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Magnetic_Field_Map.setObjectName("frame")
        self.Magnetic_Field_Map.setStyleSheet('border-image: url(:/newPrefix/World_Magnetic_Field_2015.pdf.jpg);background-color : rgb(255, 255, 255);')


    def labels(self):
        self.electron = QLabel('-', self)
        self.electron.move(35, 235)                                                                                         #Elektron dediğim ekranın sol köşesinde dönen bir yazı aslında
        self.electron.resize(25, 25)
        self.electron.setStyleSheet("border: 10px solid red; border-radius: 10px; min-height: 10px; min-width: 10px")

        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(20)

        self.Radius_Of_Core = QtWidgets.QLabel(self)
        self.Radius_Of_Core.setObjectName("label")                                                          #Buralarda çeşitli Yazılar tanımlanıyor
        self.Radius_Of_Core.setStyleSheet("background-color: white;")
        self.Radius_Of_Core.setGeometry(350, 260, 80, 50)

        self.Velocity_Of_Electron_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Velocity_Of_Electron_label.setObjectName("hız")
        self.Velocity_Of_Electron_label.setFont(font)
        self.Velocity_Of_Electron_label.setStyleSheet('color : red')
        self.gridLayout.addWidget(self.Velocity_Of_Electron_label, 0, 0, 1, 1)

        self.Radius_Of_Core_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Radius_Of_Core_label.setObjectName("label_4")
        self.Radius_Of_Core_label.setFont(font)
        self.Radius_Of_Core_label.setStyleSheet('color : red')
        self.gridLayout.addWidget(self.Radius_Of_Core_label, 3, 0, 1, 1)

        self.Charge_Of_Electron_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Charge_Of_Electron_label.setObjectName("label_2")
        self.Charge_Of_Electron_label.setFont(font)
        self.Charge_Of_Electron_label.setStyleSheet('color : red')
        self.gridLayout.addWidget(self.Charge_Of_Electron_label, 2, 0, 1, 1)


        self.Charge_Of_Electron_label.setText("Yük(c)")
        self.Velocity_Of_Electron_label.setText("Hız(m/s)")
        self.Radius_Of_Core_label.setText("Yarıçap(m)")

        self.Electron_VS_Earth_label = QLabel(self.gridLayoutWidget_2)
        self.Electron_VS_Earth_label.setAlignment(Qt.AlignCenter)
        self.Electron_VS_Earth_label.setFont(font)
        self.Electron_VS_Earth_label.setStyleSheet('color : red')
        self.gridLayout_2.addWidget(self.Electron_VS_Earth_label, 1, 1, 1, 1)

        self.Comparison_label = QLabel(self.gridLayoutWidget_2)
        self.Comparison_label.setAlignment(Qt.AlignCenter)
        self.Comparison_label.setFont(font)
        self.Comparison_label.setStyleSheet('color : red')
        self.gridLayout_2.addWidget(self.Comparison_label, 0, 1, 1, 1)

        self.Electron_VS_Earth_label.setText("Elektron VS Dünya")
        self.Comparison_label.setText("KARŞILAŞTIRMA")

    def buttonboxs(self):
        self.buttonBox_1 = QtWidgets.QDialogButtonBox(self)
        self.buttonBox_1.setGeometry(QtCore.QRect(150, 900, 193, 71))
        self.buttonBox_1.setOrientation(QtCore.Qt.Vertical)                                                 #'Butonbox'lar aslında bizim hesaplamayı göstermek için kullandığımız butonlar
        self.buttonBox_1.setStandardButtons(QtWidgets.QDialogButtonBox.Apply | QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox_1.setObjectName("buttonBox_1")

        self.buttonBox_2 = QDialogButtonBox(self.gridLayoutWidget_2)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.gridLayout_2.addWidget(self.buttonBox_2, 2, 1, 1, 1)

    def lineedits(self):
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(20)


        self.radius_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.radius_lineEdit.setObjectName("lineEdit_4")                                            #'Lineedit'ler kullanılarak ekrandan verileri alıyoruz
        self.radius_lineEdit.setFont(font)
        self.gridLayout.addWidget(self.radius_lineEdit, 3, 2, 1, 1)

        self.charge_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.charge_lineEdit.setObjectName("lineEdit_2")
        self.charge_lineEdit.setFont(font)
        self.gridLayout.addWidget(self.charge_lineEdit, 2, 2, 1, 1)


        self.velocity_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.velocity_lineEdit.setObjectName("lineEdit_3")
        self.velocity_lineEdit.setFont(font)
        self.gridLayout.addWidget(self.velocity_lineEdit, 0, 2, 1, 1)


        self.information_lineEdit = QtWidgets.QLineEdit(self)
        self.information_lineEdit.setGeometry(1060, 500, 750, 20)
        self.information_lineEdit.setReadOnly(True)
        self.information_lineEdit.setFont(font)
        self.information_lineEdit.setText("Haritada konumlara göre manyetik alan gösterilmiştir.Değerler nT tipindedir.(50000 nT = 0.00005 T)")
        self.information_lineEdit.setObjectName("line")

        self.Magnetic_Of_Electron_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.Magnetic_Of_Electron_lineEdit.setObjectName("lineEdit")
        self.Magnetic_Of_Electron_lineEdit.setFont(font)
        self.gridLayout_2.addWidget(self.Magnetic_Of_Electron_lineEdit, 1, 0, 1, 1)

        self.Magnetic_Of_Earth_lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.Magnetic_Of_Earth_lineEdit.setObjectName("lineEdit_2")
        self.Magnetic_Of_Earth_lineEdit.setFont(font)
        self.gridLayout_2.addWidget(self.Magnetic_Of_Earth_lineEdit, 1, 2, 1, 1)


    def move_electron(self):
        while self.flag == True:
            self.electron.move(35, 235)
            time.sleep(0.3)
            self.electron.move(235, 435)                                    #Yukarıda tanımladığımız elektronun flag doğru olduğunda yani butonlara basıldığında döndürüyoruz
            time.sleep(0.3)
            self.electron.move(435, 235)
            time.sleep(0.3)
            self.electron.move(235, 35)
            time.sleep(0.3)

    def calculation(self, velocity, radius, charge):
        try:
            constant = 1.27e-06
            current =(float(charge) * float(velocity))/ (2*math.pi*float(radius))
            Magnetic_Field = (constant*current)/(2*float(radius))                                       #Burada asıl iş olan hesaplamayı yaptırıyorum yaptığım hesaplama teorik kısımdaki förmüllerdir
            self.flag = True
            return Magnetic_Field
        except ValueError:
            self.flag = False
            critical_m = QMessageBox.critical(self, "PyQt5 Mesajı","Girdiğiniz değer büyük olasılıkla bir sayı değil lütfen kontrol edin")      #Eğer kulanıcı sayı yerine harf girerse hata mesajı gösteriyor


    def texts(self, velocity, charge, radius):
        if self.flag == True:
            self.console_textbrowser.append('-------------------------------------------------------------------------------------------------------------------')
            self.console_textbrowser.append('Hesaplamaya başlıyorum ...')
            time.sleep(2)
            self.console_textbrowser.append('Hız değeri = {} {}'.format(velocity,'m/s'))
            time.sleep(1)                                                                                                                   #Burada flag doğru olduğunda konsola bilgileri yazdırıyorum
            self.console_textbrowser.append('Yük değeri = {} {}'.format(charge, 'c'))
            time.sleep(1)
            self.console_textbrowser.append('Yarıçap değeri = {} {}'.format(radius, 'm'))
            time.sleep(2)
            self.console_textbrowser.append('Manyetik Alan değeri = {} {}'.format(self.Magnetic_Field, 'T'))
            time.sleep(1)
            self.console_textbrowser.append('Hesaplama bitti.')
            self.console_textbrowser.append('-------------------------------------------------------------------------------------------------------------------')

    def connects(self):
        self.buttonBox_1.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.on_apply)                    #'buttonnbox'lara basıldığında hangi fonksiyonu çağırması gerektiğini söylüyorum
        self.buttonBox_1.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.on_cancel)

        self.buttonBox_2.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.on_ok)
        self.buttonBox_2.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.on_cancel_2)


    @pyqtSlot()
    def on_apply(self):
        if self.velocity_lineEdit.text() == ''  or self.radius_lineEdit.text() == '' or self.charge_lineEdit.text()== '':     #Eğer bir değer girilmemişse hata verdiriyorum
            critical_m = QMessageBox.critical(self, "PyQt5 Mesajı", "Lütfen tüm değerleri girdiğinizden emin olun")
        else:
            velocity = self.velocity_lineEdit.text()
            charge = self.charge_lineEdit.text()                                                       #Değerleri alıyorum
            radius = self.radius_lineEdit.text()
            self.Radius_Of_Core.setText("R = {}".format(radius))
            self.Magnetic_Field = self.calculation(velocity, radius, charge)                      #Yukarıda 'calculation' fonsiyonuna parametre geçip manyetik alanı buluyorum

            self.t1 = Thread(target=self.move_electron)                                                 #Pythonda iki işi aynı anda yapmak için threading modülü kullanılıyor bende hem elektronun dönmesi için hemda yazıarı yazdırması için bu mödülü kullandım
            self.t1.start()
            self.t2 = Thread(target=self.texts, args=(velocity, charge, radius))
            self.t2.start()


    def on_cancel(self):
        self.flag = False
        self.velocity_lineEdit.setText("")                                          #'Cancel'a basıldığında 'lineedit'leri temizliyor
        self.charge_lineEdit.setText("")
        self.radius_lineEdit.setText("")

    def on_ok(self):
        if self.Magnetic_Of_Electron_lineEdit.text() == '' or self.Magnetic_Of_Earth_lineEdit.text() == '' :                #Eğer bir değer girilmemişse hata verdiriyorum
            critical_m = QMessageBox.critical(self, "PyQt5 Mesajı", "Lütfen tüm değerleri girdiğinizden emin olun")
        else:
            try:
                MagneticF_Of_Electron = self.Magnetic_Of_Electron_lineEdit.text()
                MagneticF_Of_Earth = self.Magnetic_Of_Earth_lineEdit.text()                                                 #Burda karşılaştırma yapmak için hem dünyanın hemde elektronun manyetik alanını alıyorum
                self.kat_1 = float(MagneticF_Of_Electron) / float(MagneticF_Of_Earth)                                       #Aralarında kaç kat var onu buluyorum
                self.kat_2 = float(MagneticF_Of_Earth)/float(MagneticF_Of_Electron)
                self.console_textbrowser.append('-------------------------------------------------------------------------------------------------------------------')
                if float(MagneticF_Of_Electron) > float(MagneticF_Of_Earth):
                    self.console_textbrowser.append('Elektronun oluşturduğu manyetik alan Dünyanın oluşturduğu manyetik alandan fazladır.')
                    self.console_textbrowser.append('Elektronun oluşturduğu manyetik alan Dünyanın oluşturduğu manyetik alanın {} katıdır'.format(self.kat_1))
                elif float(MagneticF_Of_Electron) < float(MagneticF_Of_Earth):
                    self.console_textbrowser.append('Dünyanın oluşturduğu manyetik alan Elektronun oluşturduğu manyetik alandan fazladır.')
                    self.console_textbrowser.append('Dünyanın oluşturduğu manyetik alan Elektronun oluşturduğu manyetik alanın {} katıdır'.format(self.kat_2))
                else:
                    self.console_textbrowser.append('Dünyanın oluşturduğu manyetik alan ve  Elektronun oluşturduğu manyetik alan birbirlerine eşittir')
                self.console_textbrowser.append('-------------------------------------------------------------------------------------------------------------------')
            except ValueError:
                self.critical_m = QMessageBox.critical(self, "PyQt5 Mesajı","Girdiğiniz değer büyük olasılıkla bir sayı değil lütfen konrtol edin")

    def on_cancel_2(self):
        self.Magnetic_Of_Electron_lineEdit.setText("")                      #'Cancel'a basıldığında 'lineedit'leri temizliyor
        self.Magnetic_Of_Earth_lineEdit.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = window()
    w.showMaximized()
    sys.exit(app.exec_())
