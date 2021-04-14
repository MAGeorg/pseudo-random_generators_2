import copy

class Hankel:
    def __init__(self, L):
        self.L = L
        self.data = list()
        with open("result.txt", "r") as file:
            self.data = file.read()
        self.data = self.data.split(" ")[0:L]
        self.data = [int(i) for i in self.data]
        # print(self.data)

    def determinant(self, A):
        indices = list(range(len(A)))
        total = 0
        if len(A) == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val % 2

        for fc in indices:
            As = copy.deepcopy(A)
            As = As[1:]
            height = len(As)

            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc + 1:]

            sign = (-1) ** (fc % 2)
            sub_det = self.determinant(As)
            total += (sign * A[0][fc] * sub_det) % 2
        return total % 2

    def create_matrix(self, begin, len_column):
        end = begin + len_column - 1 # self.k - 1
        mas = list()
        mas.append(self.data[begin: end + 1])
        i = 0
        while begin + i < begin + len_column - 1: # self.k - 1:
            i += 1
            new_line = self.data[begin + i: end + 1 + i]
            mas.append(new_line)
        return mas

    def analysis(self):
        degree_pol, br = 0, 0
        mas_deg_pol = None
        for i in range(2, self.L // 2):
            mas = self.create_matrix(0, i)
            det = self.determinant(mas)
            if det != 0:
                degree_pol = i
                mas_deg_pol = mas
            elif br > 2:
                break
            else:
                br += 1

        print("===========================================")
        print("\t\tГанкелева матрица")
        for line in mas_deg_pol:
            print(line)
        print("===========================================")
        print("\tСтепень минимального многочлена: ", degree_pol)
        print("===========================================\n")
