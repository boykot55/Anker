import sys, math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("anker_form.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def res():
    form.check_diametr.setCurrentIndex(0)
    form.input_amount.setValue(0)
    form.input_length.setValue(0)
    form.check_length_standart.setChecked(False)
    form.volume_small.setChecked(True)

def calc():
    #if form.check_length_standart.isChecked():
    #print("1")
        #form.input_length.value(diametr * 10)
    diametr = int(form.check_diametr.currentText())
    amount = int(form.input_amount.value())
    length = int(form.input_length.value()) # исключить при реализации цикла с выбором длины анкера
    print(diametr, amount, length)
    volume = math.ceil(math.pi * length * 0.001 * 1.2 * ((diametr + 5) ** 2 - diametr ** 2) / 4)
    total = volume * amount
    print(volume, total)
'''
    Для функции "calc" не реализован выбор стандартной длины анкекера. 
    Выдается ошибка: Process finished with exit code -1073740791 (0xC0000409)

        if check_length_standart.isChecked():
            length = int(diametr * 10)
            print("Стандарная длина анкера")
        else:
            length = int(self.input_length.value())
            print("Длина анкера задана пользователем")

    def calc(self):
'''

form.button_reset.clicked.connect(res)
form.button_calculate.clicked.connect(calc)
app.exec_()

'''
Ссылки на материалы с аналогичными проектами:
    https://www.youtube.com/watch?v=eTL25yiNpG4&list=PLxiU3nwEQ4PFYw-kaE5kAT17AtxhvLM71
    https://www.youtube.com/watch?v=pMNrxE1xAfw
    https://qna.habr.com/q/666620?ysclid=ldkl3c90w0686089591

'''''