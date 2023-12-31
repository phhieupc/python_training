
# Form implementation generated from reading ui file 'Elgamal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
import sys
import math

class Ui_Elgamal_demo(object):
    def setupUi(self, Elgamal_demo):
        
        #Tạo biến
        self.Y =''
        self.p, self.y1, self.a, self.Alpha, self.Beta, self.k= 1,1,1,1,1,1
        self.prime =[ x for x in range(8*(10**3),9*(10**3)) if self.checkPrime(x)]

        Elgamal_demo.setObjectName("Elgamal_demo")
        Elgamal_demo.resize(1585, 1090)
        self.centralwidget = QtWidgets.QWidget(Elgamal_demo)
        self.centralwidget.setObjectName("centralwidget")
        self.btnGenKey = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenKey.setGeometry(QtCore.QRect(30, 40, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnGenKey.setFont(font)
        self.btnGenKey.setObjectName("btnGenKey")
        self.in_encrypt = QtWidgets.QTextEdit(self.centralwidget)
        self.in_encrypt.setGeometry(QtCore.QRect(60, 140, 551, 371))
        self.in_encrypt.setObjectName("in_encrypt")
        self.Alpha_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.Alpha_txt.setGeometry(QtCore.QRect(310, 70, 101, 51))
        self.Alpha_txt.setObjectName("Alpha_txt")
        self.out_encrypt = QtWidgets.QTextEdit(self.centralwidget)
        self.out_encrypt.setGeometry(QtCore.QRect(60, 690, 551, 281))
        self.out_encrypt.setObjectName("out_encrypt")
        self.out_decrypt = QtWidgets.QTextEdit(self.centralwidget)
        self.out_decrypt.setGeometry(QtCore.QRect(900, 690, 611, 281))
        self.out_decrypt.setObjectName("out_decrypt")
        self.in_decrypt = QtWidgets.QTextEdit(self.centralwidget)
        self.in_decrypt.setGeometry(QtCore.QRect(900, 140, 611, 371))
        self.in_decrypt.setObjectName("in_decrypt")
        self.Beta_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.Beta_txt.setGeometry(QtCore.QRect(420, 70, 91, 51))
        self.Beta_txt.setObjectName("Beta_txt")
        self.P_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.P_txt.setGeometry(QtCore.QRect(530, 70, 91, 51))
        self.P_txt.setObjectName("P_txt")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(1270, 40, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(680, 140, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(120, 560, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEncrypt.setFont(font)
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.a_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.a_txt.setGeometry(QtCore.QRect(950, 540, 161, 51))
        self.a_txt.setObjectName("a_txt")
        self.b_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.b_txt.setGeometry(QtCore.QRect(950, 610, 161, 51))
        self.b_txt.setObjectName("b_txt")
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(1150, 560, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDecrypt.setFont(font)
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(900, 540, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(900, 600, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(620, 890, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSend.setFont(font)
        self.btnSend.setObjectName("btnSend")
        self.btnRand = QtWidgets.QPushButton(self.centralwidget)
        self.btnRand.setGeometry(QtCore.QRect(690, 40, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRand.setFont(font)
        self.btnRand.setObjectName("btnRand")
        self.btnOpenFileEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFileEncrypt.setGeometry(QtCore.QRect(440, 520, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnOpenFileEncrypt.setFont(font)
        self.btnOpenFileEncrypt.setObjectName("btnOpenFileEncrypt")
        self.btnOpenFileDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFileDecrypt.setGeometry(QtCore.QRect(1340, 520, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnOpenFileDecrypt.setFont(font)
        self.btnOpenFileDecrypt.setObjectName("btnOpenFileDecrypt")
        self.btnSaveFileDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveFileDecrypt.setGeometry(QtCore.QRect(1340, 600, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSaveFileDecrypt.setFont(font)
        self.btnSaveFileDecrypt.setObjectName("btnSaveFileDecrypt")
        Elgamal_demo.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Elgamal_demo)
        self.statusbar.setObjectName("statusbar")
        Elgamal_demo.setStatusBar(self.statusbar)
        self.btnSaveFileEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveFileEncrypt.setGeometry(QtCore.QRect(440, 600, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSaveFileEncrypt.setFont(font)
        self.btnSaveFileEncrypt.setObjectName("btnSaveFileEncrypt")
        self.retranslateUi(Elgamal_demo)
        QtCore.QMetaObject.connectSlotsByName(Elgamal_demo)
        #event
        self.btnClose.clicked.connect(self.close)
        self.btnEncrypt.clicked.connect(self.encrypt)
        self.btnSend.clicked.connect(self.send)
        self.btnClear.clicked.connect(self.clear)
        self.btnDecrypt.clicked.connect(self.decrypt)
        self.btnGenKey.clicked.connect(self.genKey)
        self.btnRand.clicked.connect(self.randKey)
        self.btnOpenFileEncrypt.clicked.connect(self.openFileEncrypt)
        self.btnSaveFileEncrypt.clicked.connect(self.saveFileEncrypt)
        self.btnOpenFileDecrypt.clicked.connect(self.openFileDecrypt)
        self.btnSaveFileDecrypt.clicked.connect(self.saveFileDecrypt)

    def retranslateUi(self, Elgamal_demo):
        _translate = QtCore.QCoreApplication.translate
        Elgamal_demo.setWindowTitle(_translate("Elgamal_demo", "MainWindow"))
        self.btnGenKey.setText(_translate("Elgamal_demo", "Generation Key"))
        self.btnClose.setText(_translate("Elgamal_demo", "Close"))
        self.btnClear.setText(_translate("Elgamal_demo", "Clear"))
        self.btnEncrypt.setText(_translate("Elgamal_demo", "Encrypt"))
        self.btnDecrypt.setText(_translate("Elgamal_demo", "Decrypt"))
        self.label.setText(_translate("Elgamal_demo", "Alpha"))
        self.label_2.setText(_translate("Elgamal_demo", "Beta"))
        self.label_3.setText(_translate("Elgamal_demo", "P"))
        self.label_4.setText(_translate("Elgamal_demo", "a"))
        self.label_5.setText(_translate("Elgamal_demo", "k"))
        self.btnSend.setText(_translate("Elgamal_demo", "Send Ciphertext"))
        self.btnRand.setText(_translate("Elgamal_demo", "Random Key"))
        self.btnOpenFileEncrypt.setText(_translate("Elgamal_demo", "Open File"))
        self.btnSaveFileEncrypt.setText(_translate("Elgamal_demo", "Save File"))
        self.btnOpenFileDecrypt.setText(_translate("Elgamal_demo", "Open File"))
        self.btnSaveFileDecrypt.setText(_translate("Elgamal_demo", "Save File"))

    def openFileEncrypt(self):
        linkFile = App().initUIOpen()
        if not linkFile == '':
            f = open(linkFile,"r",encoding="utf-8")
            #readFile = f.read()
            self.in_encrypt.setText(f.read())
            f.close()

    def saveFileEncrypt(self):
        linkFile = App().initUISave()
        if linkFile:
            with open(linkFile, "w", encoding="utf-8") as f:
                f.write(self.out_encrypt.toPlainText())
    
    def openFileDecrypt(self):
        linkFile = App().initUIOpen()
        if not linkFile == '':
            f = open(linkFile,"r",encoding="utf-8")
            self.in_decrypt.setText(f.read())
            f.close()

    def saveFileDecrypt(self):
        linkFile = App().initUISave()
        if linkFile:
            with open(linkFile, "w", encoding="utf-8") as f:
                f.write(self.out_decrypt.toPlainText())

    def checkPrime(self,x ):
        if x == 2 or x == 3:
            return True

        if x == 1 or x % 2 == 0 or x % 3 == 0 :
            return False
        
        for i in range(5,int(math.sqrt(x))+1,6):
            if x % i == 0 or x % (i+2) == 0 :
                return False

        return True

    def powMod(self,x,n,m): 
        '''
        x^n mod m
        pow(x,y,z)
        '''
        def ConvertToBinary(n):
            s = ''
            while n >= 1 :
                s+= chr(ord('0') + n%2) 
                n=int(n/2)
            return s[::-1]

        p=1
        ss = ConvertToBinary(n)
        for s in ss:
            p = (p*p) % m
            if(s == '1') :
                p = (p*x) % m
        
        return p

    def modInverse(self,a,m):
        '''
        a^-1 mod m
        '''
        xa,xm,mm= 1,0,m
        while m != 0 :
            q= int(a/m)
            xr= xa - q * xm
            xa= xm
            xm= xr
            r= a % m
            a= m
            m= r
        if xa < 0 :
            xa = mm + xa
        return xa

    def calcBeta(self,p, Alpha, a):
        return self.powMod(Alpha,a,p)

    def close(self):
        sys.exit(app.exec_())

    def randKey(self):
        self.p = random.choice(self.prime)
        self.Alpha = random.randint(10,self.p - 5)
        self.a = random.randint(10,self.p - 5)
        self.k = random.randint(10,self.p - 5)
        self.Beta = self.calcBeta(self.p,self.Alpha,self.a)
        self.P_txt.setText(str(self.p))
        self.Alpha_txt.setText(str(self.Alpha))
        self.a_txt.setText(str(self.a))
        self.b_txt.setText(str(self.k))
        self.Beta_txt.setText(str(self.Beta))
        self.in_decrypt.setText('')
        self.out_decrypt.setText('')
        self.out_encrypt.setText('')


    def encrypt(self):
        # đầu vào
        if self.P_txt.toPlainText() == '':
            self.messenger('p')
            return
        pp = int(self.P_txt.toPlainText())
        if  not self.checkPrime(pp):
            self.messenger('P')
            return
        self.p = pp #số nguyên tố 

        if self.Alpha_txt.toPlainText() == '':
            self.messenger('Alpha')
            return

        self.Alpha = int(self.Alpha_txt.toPlainText()) # là phần tử nguyên thủy thuộc Zp*

        if self.a_txt.toPlainText() == '':
            self.messenger('a')
            return

        self.a = int(self.a_txt.toPlainText())  # chọn a là khóa bí mật thuộc {2,3...,p-2}
        self.Beta = self.calcBeta(self.p,self.Alpha,self.a) # Beta = Alpha^a mod p
        
        self.Beta_txt.setText(str(self.Beta))
        
        #self.Beta = int(self.Beta_txt.toPlainText())

        # Mã hóa 
        #X_ = str(input('nhập bản rõ:'))
        X_ = self.in_encrypt.toPlainText()
        if X_ == '':
            self.messenger("Bản rõ")
            return
        X = [ord(x) for x in X_]

        if self.b_txt.toPlainText() == '':
            self.messenger("k")
            return

        self.k = int(self.b_txt.toPlainText())  # 1 số ngẫu nhiên bí mật k thuộc Zp-1

        # E_Kpub(x,k)=(y1,y2): y1 = Alpha^k mod p ; y2 = (Beta^k * x) mod p
        self.y1 = pow(self.Alpha, self.k, self.p)
        y2 = [(pow(self.Beta, self.k, self.p) * x) % self.p for x in X]
        self.Y = ' '.join(str(y) for y in y2)
        self.out_encrypt.setText(self.Y)
        
    def send(self):
        self.in_decrypt.setText(self.Y)
    
    def clear(self):
        self.in_decrypt.setText('')
        self.in_encrypt.setText('')
        self.out_decrypt.setText('')
        self.out_encrypt.setText('')
        self.Alpha_txt.setText('')
        self.Beta_txt.setText('')
        self.P_txt.setText('')
        self.a_txt.setText('')
        self.b_txt.setText('')

    
    def decrypt(self):
        if self.in_decrypt.toPlainText() == '':
            self.messenger('Bản mã')
            return
        
        YY = self.in_decrypt.toPlainText()
        listYY = [int(y) for y in YY.split()]  # Chuyển chuỗi số thành danh sách các số nguyên

        # D_Kpir(y1, y2) = (y2 * ((y1^a)^-1)) mod p
        res = pow(self.y1, self.a, self.p)  # y1^a mod p
        res_inverse = self.modInverse(res, self.p)  # (y1^a mod p)^-1 mod p
        D_Kpir = [(y * res_inverse) % self.p for y in listYY]
        ans = ''.join([chr(y) for y in D_Kpir])
        self.out_decrypt.setText(ans)
    
    def genKey(self):
        if self.P_txt.toPlainText() =='':
            self.messenger('p')
            return
        if  not self.checkPrime(int(self.P_txt.toPlainText())):
            self.messenger('P')
            return
        
        self.p = int(self.P_txt.toPlainText())
        if  self.Alpha_txt.toPlainText() =='':
            self.Alpha_txt.setText(str(random.randint(1,self.p-2)))
        if  self.a_txt.toPlainText() =='':
            self.a_txt.setText(str(random.randint(1,self.p-2)))
        if  self.b_txt.toPlainText() =='':
             self.b_txt.setText(str(random.randint(1,self.p-2)))
        self.Beta_txt.setText(str(self.calcBeta(self.p,int(self.Alpha_txt.toPlainText()),int(self.a_txt.toPlainText()))))
       
    
    def messenger(self,x):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if x == 'P':
            msg.setInformativeText("P Phải là số nguyên tố")
        else :
            msg.setInformativeText("Không được để trống {}".format(x))
        msg.setWindowTitle("Thông báo")
        msg.exec_()

    
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'App'
    
    def initUIOpen(self):
        self.setWindowTitle(self.title)
        filename = self.openFileNameDialog()
        #self.show()
        return filename

    def initUISave(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Lưu tệp tin", "", "All Files (*);;Text Files (*.txt)", options=options)
        return fileName
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"OpenFile", "","All Files (*);;Text Files (*.txt)", options=options)
        return fileName
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        return fileName
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Elgamal_demo = QtWidgets.QMainWindow()
    ui = Ui_Elgamal_demo()
    ui.setupUi(Elgamal_demo)
    Elgamal_demo.show()
    sys.exit(app.exec_())
