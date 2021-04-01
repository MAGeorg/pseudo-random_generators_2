from lrs import *
from analysis_lrs import *


if __name__ == "__main__":
    print("===========================================")
    print("Выберите действие:\n\t1 - генерация ЛРП\n"
          "\t2 - оценить параметры ЛРП")
    print("===========================================")
    choose = int(input("<< "))
    if choose == 1:
        x = 76859
        s = 50115
        L = 65536
        # x = 13
        # s = 10
        # L = 10
        LRS = LinearRecurrentSequence(x, s, L)
        LRS.generate()
    elif choose == 2:
        k = int(input("Введите k: "))
        L = int(input("Введите L: "))
        if L < 2 * k:
            print("Невозможно проанализировать последовательность, так как не выполенено"
                  "условие k < L, по отрезку 2k")
            exit()
        analysis = AnalysisLRS(k, L)
        analysis.create_matrix(0)
        analysis.calculate_Berle_Kemp()
    else:
        print("\n --- Wrong choice ---")
