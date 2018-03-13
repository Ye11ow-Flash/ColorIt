# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SemiFinal2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Prediction import predict
from skimage.io import imsave
import random

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(805, 582)
        Form.setAutoFillBackground(True)
        self.Menu = QtGui.QWidget(Form)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 281, 581))
        self.Menu.setAutoFillBackground(False)
        self.Menu.setStyleSheet(_fromUtf8("background-color:rgb(29,29,29);"))
        self.Menu.setObjectName(_fromUtf8("Menu"))
        self.home_cmb = QtGui.QCommandLinkButton(self.Menu)
        self.home_cmb.setGeometry(QtCore.QRect(40,330, 211, 51))
        self.home_cmb.setAutoFillBackground(False)
        self.home_cmb.setStyleSheet(_fromUtf8("background-color: rgb(122,117,116);\n"
"font: 75 20pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/2d9c25ee1fbffdae2909164e858648d1-instagram-home-button-by-vexels.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_cmb.setIcon(icon)
        self.home_cmb.setIconSize(QtCore.QSize(30, 30))
        self.home_cmb.setAutoDefault(False)
        self.home_cmb.setObjectName(_fromUtf8("home_cmb"))
        self.app_name = QtGui.QLabel(self.Menu)
        self.app_name.setGeometry(QtCore.QRect(0, -1, 281, 181))
        self.app_name.setText(_fromUtf8(""))
        self.app_name.setPixmap(QtGui.QPixmap(_fromUtf8(":/WhatsApp Image 2018-03-11 at 1.27.09 AM.jpeg")))
        self.app_name.setScaledContents(True)
        self.app_name.setObjectName(_fromUtf8("app_name"))
        self.up_pic = QtGui.QWidget(Form)
        self.up_pic.setGeometry(QtCore.QRect(299, -1, 511, 581))
        self.up_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.up_pic.setAutoFillBackground(False)
        self.up_pic.setStyleSheet(_fromUtf8("\n"
""))
        self.up_pic.setObjectName(_fromUtf8("up_pic"))
        self.upload = QtGui.QPushButton(self.up_pic)
        self.upload.setGeometry(QtCore.QRect(185, 150, 161, 91))
        self.upload.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.upload.setAutoFillBackground(False)
        self.upload.setStyleSheet(_fromUtf8("background-color: rgb(27,161,226);"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/input_black_192x192.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload.setIcon(icon2)
        self.upload.setIconSize(QtCore.QSize(50, 50))
        self.upload.setAutoDefault(False)
        self.upload.setFlat(True)
        self.upload.setObjectName(_fromUtf8("upload"))
        self.color = QtGui.QPushButton(self.up_pic)
        self.color.setGeometry(QtCore.QRect(175, 480, 171, 91))
        self.color.setAutoFillBackground(False)
        self.color.setStyleSheet(_fromUtf8("background-color: rgb(27,161,226);\n"
""))
        self.color.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/painting-03-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.color.setIcon(icon3)
        self.color.setIconSize(QtCore.QSize(50, 50))
        self.color.setFlat(True)
        self.color.setObjectName(_fromUtf8("color"))
        self.photo = QtGui.QLabel(self.up_pic)
        self.photo.setGeometry(QtCore.QRect(30, 40, 441, 381))
        self.photo.setAutoFillBackground(False)
        self.photo.setText(_fromUtf8(""))
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName(_fromUtf8("photo"))
        self.upload_label = QtGui.QLabel(self.up_pic)
        self.upload_label.setGeometry(QtCore.QRect(190, 220, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setBold(True)
        font.setWeight(75)
        self.upload_label.setFont(font)
        self.upload_label.setAutoFillBackground(False)
        self.upload_label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.upload_label.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_label.setObjectName(_fromUtf8("upload_label"))
        self.color_label = QtGui.QLabel(self.up_pic)
        self.color_label.setGeometry(QtCore.QRect(220, 550, 71, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setBold(True)
        font.setWeight(75)
        self.color_label.setFont(font)
        self.color_label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_label.setObjectName(_fromUtf8("color_label"))
        self.photo.raise_()
        self.upload.raise_()
        self.color.raise_()
        self.upload_label.raise_()
        self.color_label.raise_()
        self.up_pic.raise_()
        self.back_image = QtGui.QWidget(Form)
        self.back_image.setGeometry(QtCore.QRect(300, 0, 501, 581))
        self.back_image.setStyleSheet(_fromUtf8("background-image: url(:/Android-L-Material-Design-Wallpapers-5.png);"))
        self.back_image.setObjectName(_fromUtf8("back_image"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(300, -1, 501, 581))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 256, 256))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(120, 290, 256, 256))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.back_image.raise_()
        self.Menu.raise_()
        self.widget.raise_()
        self.up_pic.raise_()

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.home_cmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.up_pic.show)
        QtCore.QObject.connect(self.home_cmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upload.show)
        QtCore.QObject.connect(self.home_cmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upload_label.show)
        QtCore.QObject.connect(self.home_cmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.photo.hide)
        QtCore.QObject.connect(self.home_cmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.color.hide)
        QtCore.QObject.connect(self.home_cmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.color_label.hide)
        QtCore.QObject.connect(self.upload, QtCore.SIGNAL(_fromUtf8("clicked()")), self.color.show)
        QtCore.QObject.connect(self.upload, QtCore.SIGNAL(_fromUtf8("clicked()")), self.color_label.show)
        QtCore.QObject.connect(self.color, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget.show)
        QtCore.QObject.connect(self.home_cmb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.widget.hide)
        QtCore.QObject.connect(self.color, QtCore.SIGNAL(_fromUtf8("clicked()")), self.up_pic.hide)
        QtCore.QObject.connect(self.upload, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upload.hide)
        QtCore.QObject.connect(self.upload, QtCore.SIGNAL(_fromUtf8("clicked()")), self.upload_label.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ColorIt!!", None))
        self.home_cmb.setText(_translate("Form", "New Image", None))
        self.upload_label.setText(_translate("Form", "Select a file from computer", None))
        self.color_label.setText(_translate("Form", "Colorise", None))
        self.color.hide()
        self.color_label.hide()
        self.widget.hide()
        self.upload.clicked.connect(self.getPic)
        self.color.clicked.connect(self.func)

    def func(self):
        destination = 'C:/Users/tanis/Desktop/ColoredImage/'+str((random.random()*100000))+'.jpg'
        imsave(destination,predict(name))
        pixmap = QtGui.QPixmap(name)
        self.label_2.setPixmap(pixmap)
        pixmap = QtGui.QPixmap(destination)
        self.label_3.setPixmap(pixmap)
        #self.label_2.show()


    def getPic(self):
        global name
        name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        print(name)
        pixmap = QtGui.QPixmap(name)
        self.photo.setPixmap(pixmap)
        self.photo.show()


import new1_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

