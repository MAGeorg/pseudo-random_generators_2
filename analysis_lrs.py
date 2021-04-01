# анализ сгенерированной последовательности ЛРП
import numpy as np


class AnalysisLRS:
    def __init__(self, k, L):
        self.k = k
        self.data = list()
        with open("result.txt", "r") as file:
            self.data = file.read()
        self.data = self.data.split(" ")[0:L]
        self.data = [int(i) for i in self.data]
        # print(self.data)

    def create_matrix(self, begin):
        end = begin + self.k - 1
        self.mas = np.array(self.data[begin: end + 1])
        i = 0
        while begin + i < begin + self.k - 1:
            i += 1
            new_line = np.array(self.data[begin + i: end + 1 + i])
            self.mas = np.vstack((self.mas, new_line))
        print("===========================================")
        print("\t\tГанкелева матрица\n", self.mas)
        print("===========================================")

    @staticmethod
    def __to_list(data):
        return [int(i) for i in bin(data)[2:]][::-1]

    @staticmethod
    def __from_list(data):
        val = 0
        for i in range(0, len(data) - 1):
            val += data[i]
            val *= 2
        val += data[-1]
        return val

    def calculate_Berle_Kemp(self):
        print("===========================================")
        print("Определитель Генкелевой матрицы: ", np.linalg.det(self.mas))
        print("===========================================\n")
        m, l, N = list(), list(), int()
        m.append(1)
        l.append(0)
        if len(self.data) % 2 == 1:
            N = 2 * self.k + 1
        else:
            N = 2 * self.k
        for t in range(N):
            m_t = self.__to_list(m[t])[::-1]
            e_t = self.data[t]
            for i in range(1, l[t] + 1):
                if i >= len(m_t):
                    break
                e_t ^= m_t[i] * self.data[t - i]
            if e_t == 1:
                lam = -1
                while lam <= t - 1:
                    if l[lam + 1] >= l[t]:
                        break
                    lam += 1
                m_lam = 1
                if lam >= 0:
                    m_lam = m[lam]
                m_lam = self.__to_list(m_lam)[::-1]
                deg = t - lam
                for j in range(0, deg):
                    m_lam.insert(0, 0)
                for j in range(0, len(m_t)):
                    if j >= len(m_lam):
                        m_lam.append(m_t[j])
                        continue
                    m_lam[j] ^= m_t[j]
                m.append(self.__from_list(m_lam))
            elif e_t == 0:
                m.append(m[t])
            if e_t == 1 and l[t] <= t / 2:
                l.append(t + 1 - l[t])
            else:
                l.append(l[t])
        degree = l[-1]
        polynom = self.__to_list(m[-1])[::-1]
        print("Минимальный многочлен:")
        for i in range(0, len(polynom) - 1):
            if polynom[i] != 0:
                print("x^{} + ".format(degree), end="")
            degree -= 1
        print("{}".format(polynom[-1]))