'''
Ссылки на полезные материалы:
    https://www.youtube.com/watch?v=pMNrxE1xAfw
    
Исправление ошибок:
    https://www.youtube.com/watch?v=fEgTujWQ5Wk
'''''
import sys, math # импорт библиотеки Python
from PyQt5 import uic # подключаем доступ к объектам из формы *.uic
from PyQt5.QtWidgets import QApplication, QMainWindow # поключаем необходимые виджеты


class App(QMainWindow): # создаем класс для работы формы с наследованием от QMainWindow
    def __init__(self): # при инициализации ничего не отправляется в родительский класс
        super().__init__()
        uic.loadUi('anker_form.ui', self)
        self.button_reset.clicked.connect(self.res)
        self.button_calculate.clicked.connect(self.calc)


    def res(self):
        self.input_amount.setValue(0)
        self.length.setValue(0)
        self.check_length_standart.setChecked(False)
        self.volume_small.setChecked(True)
        # self.check_diametr.setValue(0)



    def calc(self):
        print("1.")
        #print(f"1." + str(check_diametr))
        #print(f"2." + str(input_amount))
        #print(f"3." + str(check_length_standart))
        #print(f"4." + str(input_length))
        #print(f"5." + bool(volume_small) + ", " + bool(volume_medium) + ", " + bool(volume_large))

'''
        if check_length_standart.isChecked():
        #     length = diametr * 10
        #     self.length.setText() = str(length)
        volume = math.ceil(math.pi * length * 0.001 * ((check_diametr.value + 5) ** 2 - diametr ** 2) / 4)
        # или округление: round (math.pi * length * 0.001 * ((diametr+5)**2 - diametr**2, 1)
'''

if __name__ == '__main__': # проверяем запущена ли программа и если запущена, то открывается окно
    app = QApplication(sys.argv) # создаем новый экземпляр QApplication
    ex = App() # создаем экземпляр класса App
    ex.show() # показать экземпляр класса App на экране
    sys.exit(app.exec_()) # закрыть форму


'''
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