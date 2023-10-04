import os, secrets

import pyAesCrypt, easygui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QMessageBox

import font_resources_rc


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):

        fontId = QFontDatabase.addApplicationFont(":/Fonts/RobotoSlab-Medium.ttf")

        if fontId == 0:
            fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
            self.font_1 = QFont(fontName, 11)
        else:
            self.font_1 = QFont()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 320)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setFont(self.font_1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Py_Projects/Crypto/bac.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#FCF6EA;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.operation_choice = QtWidgets.QComboBox(self.centralwidget)
        self.operation_choice.setGeometry(QtCore.QRect(120, 185, 220, 25))
        self.operation_choice.setAcceptDrops(False)
        self.operation_choice.setStyleSheet("background-color: #343440;\n"
"color: #FFFFFF;")
        self.operation_choice.setFont(self.font_1)
        self.operation_choice.setObjectName("opretation_choice")
        self.operation_choice.addItem("Зашифровать файл") 
        self.operation_choice.addItem("Дешифровать файл")

        self.filepath_input = QtWidgets.QLineEdit(self.centralwidget)
        self.filepath_input.setGeometry(QtCore.QRect(20, 30, 320, 30))
        self.filepath_input.setFont(self.font_1)
        self.filepath_input.setStyleSheet("background-color: #343440;\n"
"color: #FFFFFF;")
        self.filepath_input.setInputMask("")
        self.filepath_input.setText("")
        self.filepath_input.setObjectName("filepath_input")

        self.filepath_choice = QtWidgets.QPushButton(self.centralwidget)
        self.filepath_choice.setGeometry(QtCore.QRect(350, 30, 28, 30))
        self.filepath_choice.setFont(self.font_1)
        self.filepath_choice.setStyleSheet("color: #FFFFFF;\n"
"background-color: #343440;\n" "background-image: url(C:/Py_Projects/Crypto/fp_icon.png)")                 #вписать абсолютный путь для иконки проводника
        self.filepath_choice.setObjectName("filepath_choice")
        self.filepath_choice.clicked.connect(self.fp_choice_ret)

        self.operation_text = QtWidgets.QLabel(self.centralwidget)
        self.operation_text.setGeometry(QtCore.QRect(20, 180, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Amiri")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.operation_text.setFont(self.font_1)
        self.operation_text.setStyleSheet("color:#202026;")
        self.operation_text.setObjectName("operation_text")

        self.key_input = QtWidgets.QLineEdit(self.centralwidget)
        self.key_input.setGeometry(QtCore.QRect(20, 90, 320, 30))
        self.key_input.setFont(self.font_1)
        self.key_input.setStyleSheet("background-color: #343440;\n"
"color: #FFFFFF;")
        self.key_input.setInputMask("")
        self.key_input.setText("")
        self.key_input.setObjectName("key_input")

#         self.keypath_choice = QtWidgets.QPushButton(self.centralwidget)
#         self.keypath_choice.setGeometry(QtCore.QRect(350, 30, 30, 30))
#         self.keypath_choice.setFont(self.font_1)
#         self.keypath_choice.setStyleSheet("color: #FFFFFF;\n"
# "background-color: #343440;")
#         self.keypath_choice.setObjectName("keypath_choice")
#         self.keypath_choice.clicked.connect(self.)

        self.crypting_button = QtWidgets.QPushButton(self.centralwidget)
        self.crypting_button.setGeometry(QtCore.QRect(85, 240, 190, 40))
        self.crypting_button.setFont(self.font_1)
        self.crypting_button.setStyleSheet("color: #FFFFFF;\n"
"background-color: #343440;")
        self.crypting_button.setObjectName("crypting_button")
        self.crypting_button.clicked.connect(self.is_button_pressed)



        self.chek_for_file_del = QtWidgets.QCheckBox(self.centralwidget)
        self.chek_for_file_del.setGeometry(QtCore.QRect(20, 150, 260, 17))
        self.chek_for_file_del.setFont(self.font_1)
        self.chek_for_file_del.setStyleSheet("color: #202026;")
        self.chek_for_file_del.setObjectName("cher_for_file_del")

        self.check_for_auto_key = QtWidgets.QCheckBox(self.centralwidget)
        self.check_for_auto_key.setGeometry(QtCore.QRect(20, 130, 280, 17))
        self.check_for_auto_key.setFont(self.font_1)
        self.check_for_auto_key.setStyleSheet("color:#202026;\n")
        self.check_for_auto_key.setObjectName("check_for_auto_key")


        self.filepath_input.raise_()
        self.operation_choice.raise_()
        self.operation_text.raise_()
        self.key_input.raise_()
        self.crypting_button.raise_()
        self.chek_for_file_del.raise_()
        self.check_for_auto_key.raise_()
        self.filepath_choice.raise_()
        #self.keypath_choice.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифровальщик 3000"))
        self.filepath_input.setPlaceholderText(_translate("MainWindow", "Введите путь к файлу"))
        self.operation_text.setText(_translate("MainWindow", "Операция:"))
        self.key_input.setPlaceholderText(_translate("MainWindow", "Введите ключ шифрования"))
        self.crypting_button.setText(_translate("MainWindow", "Выполнить"))
        self.filepath_choice.setText(_translate("MainWindow", ""))
        #self.keypath_choice.setText(_translate("MainWindow", "12"))
        self.chek_for_file_del.setText(_translate("MainWindow", "Удалить исходный файл"))
        self.check_for_auto_key.setText(_translate("MainWindow", "Cгенерировать надежный ключ"))

    def fp_choice_ret(self):
        x = easygui.fileopenbox(filetypes=["*.txt", "*.aes"])
        self.filepath_input.setText(x)

    def return_the_path(self):
        t = self.filepath_input.text()
        return t
    
    f = True

    def is_button_pressed(self, f):
        k = self.key_input.text()
        if self.check_for_auto_key.isChecked():
            k = cr.creating_secure_key()
        if self.operation_choice.currentText() == "Зашифровать файл" and self.check_for_auto_key.isChecked():
            Crypto.encrypting(self, self.return_the_path(), k)
            if self.chek_for_file_del.isChecked() and f:
                os.remove(self.return_the_path())
        elif self.operation_choice.currentText() == "Дешифровать файл":    
            Crypto.decrypting(self, self.return_the_path(), self.key_input.text())

    def raise_err_window(self):
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Введены некорректные данные, проверьте путь к файлу и ключ")

        error.exec_()
        f = False
        return f


class Crypto:
    
    def encrypting(self, file_path, key):
        self.file_path = file_path
        self.key = key
        buffer_size = 128 * 1024
        file_path = file_path.replace("\\", "/")
        if file_path.endswith(".txt"):
            file_path = file_path.replace(".txt", "")
        try:
            pyAesCrypt.encryptFile(file_path + ".txt",file_path  + ".aes", key, buffer_size)
        except: 
            ui.raise_err_window()

    def decrypting(self, file_path, key):
        self.file_path = file_path
        self.key = key
        buffer_size = 128 * 1024
        file_path = file_path.replace("\\", "/")
        if file_path.endswith(".aes"):
            file_path = file_path.replace(".aes", "")
        try:
            pyAesCrypt.decryptFile(file_path + ".aes",file_path   + ".txt", key, buffer_size)
        except:  
            ui.raise_err_window()

    def creating_secure_key(self):
        ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]:;?/>.<,"
        new_file = open("Secret_Key.txt", "w")
        len_of_key = 2**5
        my_key = ''.join(secrets.choice(ALPHA) for i in range(len_of_key))
        new_file.write(my_key)
        new_file.close()
        return my_key
    


if __name__ == "__main__":
    import sys
    print(len(sys.modules))
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # cr = Crypto()
    # # pyinstaller.exe --onefile --windowed --icon=icon.ico myapp.py
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
