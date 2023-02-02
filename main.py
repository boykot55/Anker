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
    diametr = int(form.check_diametr.currentText())
    amount = int(form.input_amount.value())

    if form.check_length_standart.isChecked():
        length_calc = diametr * 10
        form.input_length.setValue(length_calc)
    length = int(form.input_length.value())

    # в формуле учтен коэф. 1,2, учитывающий заполнение клеевым составом неучтенных пустот (резба, фаска, дефекты отверстий и др.)
    volume = math.ceil(math.pi * length * 0.001 * 1.2 * ((diametr + 5) ** 2 - diametr ** 2) / 4)
    total = volume * amount
    form.total_1.setText(str(total))

    if form.volume_small.isChecked():
        volume_calc = math.ceil(total / 330)
    else:
        if form.volume_medium.isChecked():
            volume_calc = math.ceil(total / 500)
        else:
            volume_calc = math.ceil(total / 1400)
    form.total_2.setText(str(volume_calc))


form.button_reset.clicked.connect(res)
form.button_calculate.clicked.connect(calc)
app.exec_()

'''
                                                    Ссылки на материалы по PyQT5:
1. Официальная документация:    https://doc.qt.io/qt-5/qtwidgets-module.html    
2. Уроки 1-8 (Олег Шпагин):   https://www.youtube.com/watch?v=eTL25yiNpG4&list=PLxiU3nwEQ4PFYw-kaE5kAT17AtxhvLM71
3. Урок по созданию генератора паролей (IT-куб ОНТ):   https://www.youtube.com/watch?v=pMNrxE1xAfw

Форумы:  
https://ru.stackoverflow.com/questions/1188420/%d0%9a%d0%b0%d0%ba-%d0%bf%d1%80%d0%b0%d0%b2%d0%b8%d0%bb%d1%8c%d0%bd%d0%be-%d0%bf%d0%b5%d1%80%d0%b5%d0%b4%d0%b0%d1%82%d1%8c-%d0%be%d0%b1%d1%8a%d0%b5%d0%ba%d1%82-pyqt5-%d0%b8%d0%b7-%d0%be%d0%b4%d0%bd%d0%be%d0%b3%d0%be-%d0%ba%d0%bb%d0%b0%d1%81%d1%81%d0%b0-%d0%b2-%d0%b4%d1%80%d1%83%d0%b3%d0%be%d0%b9?rq=1
https://ru.stackoverflow.com/questions/1220395/%d0%9d%d1%83%d0%b6%d0%bd%d0%be-%d1%87%d1%82%d0%be%d0%b1%d1%8b-%d0%bf%d1%80%d0%b8-%d0%b2%d1%8b%d0%b1%d0%be%d1%80%d0%b5-%d0%be%d0%b4%d0%bd%d0%be%d0%b3%d0%be-%d0%b2%d0%b0%d1%80%d0%b8%d0%b0%d0%bd%d1%82%d0%b0-%d0%b8%d0%b7-qcombobox-%d0%bc%d0%b5%d0%bd%d1%8f%d0%bb%d1%81%d1%8f-%d1%82%d0%b5%d0%ba%d1%81%d1%82-%d0%b2-qlabel?rq=1
https://ru.stackoverflow.com/questions/1212044/%d0%ba%d0%b0%d0%ba-%d0%bf%d0%b5%d1%80%d0%b5%d0%b4%d0%b0%d1%82%d1%8c-%d0%b7%d0%bd%d0%b0%d1%87%d0%b5%d0%bd%d0%b8%d0%b5-%d0%b8%d0%b7-qcombobox-%d0%b2-qlabel-pyqt5?rq=1

https://qna.habr.com/q/666620?ysclid=ldkl3c90w0686089591
https://forum.qt.io/topic/122821/exit-code-1073740791-0xc0000409-when-i-input-a-string-in-qtextedit
'''

'''
                                                    Расчет без применения GUI:

import sys, math

def total(length, diametr, amount):
    print("Глубина отверстия, мм: " + str(length + 5))
    print("Диаметр отверстия, мм: " + str(diametr + 5) + "\n")
    volume = math.ceil(math.pi * length * 0.001 * ((diametr+5)**2 - diametr**2) / 4) # или округление: round (math.pi * length * 0.001 * ((diametr+5)**2 - diametr**2, 1)
    print(f"Потребность клеевого состава на одно отверстие: = " + str(volume) + " мл")
    print(f"Общая потребность клеевого состава для всего участка работ: = " + str(amount * volume) + " мл\n")
    return
print("Расчет выполнен согласно Прил. Г СП 43.13330.2012 и CTO 36554501-048-2016_Book_2_2020 \n")
anker_diametr_standart = [(12, 14, 16, 20, 24, 27, 30)]
anker_diametr_input = int(input("Введите диаметр анкера из ряда стандартных значений 12, 14, 16, 20, 24, 27 и 30 мм: "))

for i in anker_diametr_standart:
    if anker_diametr_input in i:
        print(f"Рекомендуемая длина анкера не менее: = {anker_diametr_input * 10} мм")
        anker_length_input = int(input("Введите длину анкера, мм: "))
        anker_amount_input = int(input("Введите количество анкеров/отверстий на участке работ, шт.: "))
        total(anker_length_input, anker_diametr_input, anker_amount_input)
    else:
        print('Задан некорректный диаметр анкера')
print("Химические анкера выпускаются в упаковке 330, 500 и 1400 мл")
'''