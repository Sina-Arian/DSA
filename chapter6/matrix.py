from copy import deepcopy

class Matrix():
    def __init__(self, row, col):
        self.matrice = []
        column = []
        for i in range(col):
            column.append(1)
        for j in range(row):
            self.matrice.append(deepcopy(column))


    def __pow__(self, n):
        if n == 1:
            return self
        elif n % 2 == 0: # n is even
            return self.__pow__(n//2) * self.__pow__(n//2)
        elif n % 2 != 0: # n is odd
            n -= 1
            return self.__pow__(n //2) * self.__pow__(n//2) * self


    def __mul__(self, other):
        newMatrice = Matrix(len(self.matrice), len(other.matrice[0]))

        for r in self.matrice:                      # r == satr
            r_index = self.matrice.index(r)

            for c in range(len(other.matrice[0])):  # c == sotoon

                a = 0
                for i in r:                         # i == har kodom az deraye haye satr
                    i_index = r.index(i)
                    a += ( self.matrice[r_index][i_index] * other.matrice[i_index][c] )

                newMatrice.matrice[r_index][c] = a

        return newMatrice


    def __add__(self, other):
        newMatrice = Matrix(len(self.matrice), len(self.matrice[0]))
        for r in self.matrice:                      # r == satr
            r_index = self.matrice.index(r)
            for i in r:                             # i == har kodom az deraye haye satr
                    i_index = r.index(i)
                    a = self.matrice[r_index][i_index] + other.matrice[r_index][i_index]
                    newMatrice.matrice[r_index][i_index] = a
        return newMatrice


    def __sub__(self, other):
        newMatrice = Matrix(len(self.matrice), len(self.matrice[0]))
        for r in self.matrice:                      # r == satr
            r_index = self.matrice.index(r)
            for i in r:                             # i == har kodom az deraye haye satr
                    i_index = r.index(i)
                    a = self.matrice[r_index][i_index] - other.matrice[r_index][i_index]
                    newMatrice.matrice[r_index][i_index] = a
        return newMatrice


    def __str__(self):
        out = ''
        for i in self.matrice:
            out += str(i)
            out += '\n'
        return out

