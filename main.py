"""
1. цветовое оформление;
2. интерфейс с выбором ИД.
"""


def total(length, diametr, amount):
    import math
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