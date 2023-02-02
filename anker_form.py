# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Anker\anker_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 491)
        MainWindow.setSizeIncrement(QtCore.QSize(630, 480))
        MainWindow.setBaseSize(QtCore.QSize(630, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Projects\\Anker\\icons.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(205, 221, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(10, 10, 221, 341))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("C:\\Projects\\Anker\\image.jpg"))
        self.picture.setObjectName("picture")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 170, 381, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.note_form = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.note_form.setContentsMargins(0, 0, 0, 0)
        self.note_form.setObjectName("note_form")
        self.label_3_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3_1.setFont(font)
        self.label_3_1.setObjectName("label_3_1")
        self.note_form.addWidget(self.label_3_1)
        self.label_3_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3_2.setFont(font)
        self.label_3_2.setObjectName("label_3_2")
        self.note_form.addWidget(self.label_3_2)
        self.label_3_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3_3.setFont(font)
        self.label_3_3.setObjectName("label_3_3")
        self.note_form.addWidget(self.label_3_3)
        self.label_3_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3_4.setFont(font)
        self.label_3_4.setObjectName("label_3_4")
        self.note_form.addWidget(self.label_3_4)
        self.button_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.button_calculate.setGeometry(QtCore.QRect(240, 270, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_calculate.setFont(font)
        self.button_calculate.setStyleSheet("background-color: rgb(140, 175, 255);\n"
"color: rgb(255, 255, 255);")
        self.button_calculate.setObjectName("button_calculate")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(240, 10, 381, 146))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.data_form_1 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.data_form_1.setContentsMargins(0, 0, 0, 0)
        self.data_form_1.setObjectName("data_form_1")
        self.label_1_1 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1_1.setFont(font)
        self.label_1_1.setObjectName("label_1_1")
        self.data_form_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1_1)
        self.check_diametr = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_diametr.setFont(font)
        self.check_diametr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.check_diametr.setObjectName("check_diametr")
        self.check_diametr.addItem("")
        self.check_diametr.addItem("")
        self.check_diametr.addItem("")
        self.check_diametr.addItem("")
        self.check_diametr.addItem("")
        self.check_diametr.addItem("")
        self.check_diametr.addItem("")
        self.data_form_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.check_diametr)
        self.label_1_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1_2.setFont(font)
        self.label_1_2.setObjectName("label_1_2")
        self.data_form_1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_1_2)
        self.input_amount = QtWidgets.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_amount.setMaximum(1000)
        self.input_amount.setDisplayIntegerBase(10)
        self.input_amount.setObjectName("input_amount")
        self.data_form_1.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_amount)
        self.label_1_3_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1_3_2.setFont(font)
        self.label_1_3_2.setObjectName("label_1_3_2")
        self.data_form_1.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_1_3_2)
        self.input_length = QtWidgets.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_length.setFont(font)
        self.input_length.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_length.setMaximum(500)
        self.input_length.setDisplayIntegerBase(10)
        self.input_length.setObjectName("input_length")
        self.data_form_1.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_length)
        self.label_1_3_1 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_1_3_1.setFont(font)
        self.label_1_3_1.setObjectName("label_1_3_1")
        self.data_form_1.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_1_3_1)
        self.check_length_standart = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.check_length_standart.setText("")
        self.check_length_standart.setObjectName("check_length_standart")
        self.data_form_1.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.check_length_standart)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.data_form_1.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 130, 381, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.data_form_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.data_form_2.setContentsMargins(0, 0, 0, 0)
        self.data_form_2.setObjectName("data_form_2")
        self.volume_small = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.volume_small.setFont(font)
        self.volume_small.setAcceptDrops(False)
        self.volume_small.setToolTipDuration(-1)
        self.volume_small.setChecked(True)
        self.volume_small.setObjectName("volume_small")
        self.data_form_2.addWidget(self.volume_small)
        self.volume_medium = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.volume_medium.setFont(font)
        self.volume_medium.setObjectName("volume_medium")
        self.data_form_2.addWidget(self.volume_medium)
        self.volume_large = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.volume_large.setFont(font)
        self.volume_large.setObjectName("volume_large")
        self.data_form_2.addWidget(self.volume_large)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 380, 611, 51))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.total_form = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.total_form.setContentsMargins(0, 0, 0, 0)
        self.total_form.setObjectName("total_form")
        self.text_1 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.text_1.setFont(font)
        self.text_1.setObjectName("text_1")
        self.total_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.text_1)
        self.text_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.text_2.setFont(font)
        self.text_2.setObjectName("text_2")
        self.total_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.text_2)
        self.total_1 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.total_1.setFont(font)
        self.total_1.setText("")
        self.total_1.setObjectName("total_1")
        self.total_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.total_1)
        self.total_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.total_2.setFont(font)
        self.total_2.setText("")
        self.total_2.setObjectName("total_2")
        self.total_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.total_2)
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(440, 270, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_reset.setFont(font)
        self.button_reset.setStyleSheet("background-color: rgb(140, 175, 255);\n"
"color: rgb(255, 255, 255);")
        self.button_reset.setObjectName("button_reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.menu.addAction(self.save)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчет химического анкеров"))
        self.label_3_1.setText(_translate("MainWindow", " Примечание:"))
        self.label_3_2.setText(_translate("MainWindow", "1. Расчет выполняется согласно Прил. Г СП 43.13330.2012 и"))
        self.label_3_3.setText(_translate("MainWindow", "  CTO 36554501-048-2016;"))
        self.label_3_4.setText(_translate("MainWindow", "2. Длину анкера рекомендуется принять не менее 10*d."))
        self.button_calculate.setText(_translate("MainWindow", "Расчет"))
        self.label_1_1.setText(_translate("MainWindow", "1. Выберете диаметр анкера (d), мм:"))
        self.check_diametr.setItemText(0, _translate("MainWindow", "12"))
        self.check_diametr.setItemText(1, _translate("MainWindow", "14"))
        self.check_diametr.setItemText(2, _translate("MainWindow", "16"))
        self.check_diametr.setItemText(3, _translate("MainWindow", "20"))
        self.check_diametr.setItemText(4, _translate("MainWindow", "24"))
        self.check_diametr.setItemText(5, _translate("MainWindow", "27"))
        self.check_diametr.setItemText(6, _translate("MainWindow", "30"))
        self.label_1_2.setText(_translate("MainWindow", "2. Укажите количество  анкеров, шт:"))
        self.label_1_3_2.setText(_translate("MainWindow", "3. Длина анкера, мм:"))
        self.label_1_3_1.setText(_translate("MainWindow", "     Принять длину анкера по умолчанию (10*d)"))
        self.label_2.setText(_translate("MainWindow", "4. Выберете объем картриджа:"))
        self.volume_small.setText(_translate("MainWindow", "330 мл"))
        self.volume_medium.setText(_translate("MainWindow", "500 мл"))
        self.volume_large.setText(_translate("MainWindow", "1400 мл"))
        self.text_1.setText(_translate("MainWindow", "Расчетная потребность клеевого состава химического анкера, мл.:"))
        self.text_2.setText(_translate("MainWindow", "Количество картриджей выбранного объема, шт.:"))
        self.button_reset.setText(_translate("MainWindow", "Сброс"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.save.setText(_translate("MainWindow", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
