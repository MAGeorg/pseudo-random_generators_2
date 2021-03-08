import random


class LinearRecurrentSequence:
    def __init__(self, x, s, L):
        self.x = self.__num_to_bin_list(x)
        self.s = self.__list_to_num(self.__num_to_bin_list(s))
        self.L = L
        # print(self.x, "\n", self.s)

    @staticmethod
    def __num_to_bin_list(num: int):
        return [int(i) for i in bin(num)[2:]][::-1]

    @staticmethod
    def __list_to_num(lnum: list):
        res = 0
        for i in range(0, len(lnum) - 1):
            res = (res + lnum[i]) * 2
        return res + lnum[-1]

    def generate(self):
        res = list()
        len_x = len(self.x)
        lfsr = self.s
        for i in range(0, L):
            bit = 0
            for j in range(1, len_x):
                if self.x[j] != 0:
                    bit ^= (lfsr >> (len_x - 1 - j)) % 2 ** (len_x - 1)
            res.append(lfsr % 2)
            lfsr = ((lfsr >> 1) | (bit << len_x - 2)) % 2 ** (len_x - 1)
        self.__writing_to_file(res)
        # return res

    @staticmethod
    def __writing_to_file(self, res):
        with open("result.txt", "w") as file:
            cnt = 1
            for num in res:
                file.write("%s " % num)
                if cnt == 80:
                    file.write("\n")
                    cnt = 1
                else:
                    cnt += 1






if __name__ == "__main__":
    print("===========================================")
    print("Выберите действие:\n\t1 - генерация ЛРП\n\t2 - оценить параметры ЛРП")
    print("===========================================")
    choose = int(input("<< "))
    if choose == 1:
        # x = 76859
        # s = 50115
        # L = 65536
        x = 13
        s = 10
        L = 10
        LRS = LinearRecurrentSequence(x, s, L)
        LRS.generate()
    elif choose == 2:
        pass
    else:
        print("\n --- Wrong choice ---")
