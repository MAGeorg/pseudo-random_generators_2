from lrs import *
from analysis_lrs import *
from hankel import *


if __name__ == "__main__":
    print("===========================================")
    print("Выберите действие:\n\t1 - генерация ЛРП\n"
          "\t2 - оценить параметры ЛРП")
    print("===========================================")
    choose = int(input("<< "))
    if choose == 1:
        # ===== вариант ====
        # x = 76859 # хар-кий многочлен
        # s = 50115 # начальное заполнение S-0
        # L = 65536 # длина последовательности
        # ===== задание ====
        x = 11
        L = 32
        s = 5
        LRS = LinearRecurrentSequence(x, s, L)
        LRS.generate()
    elif choose == 2:
        k = int(input("Введите k: "))
        L = int(input("Введите L: "))
        if L < 2 * k:
            print("Невозможно проанализировать последовательность, так как не выполенено"
                  "условие k < L, по отрезку 2k")
            exit()

        matrix = Hankel(L)
        matrix.analysis()
        # matrix.create_matrix(0)

        analysis = AnalysisLRS(k, L)
        analysis.calculate_Berle_Kemp()
    else:
        print("\n --- Wrong choice ---")
