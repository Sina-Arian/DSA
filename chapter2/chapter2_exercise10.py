from math import ceil

class Rational:

    def __init__(self, num = 0, den = 1):
        a = self._gcd(num, den)
        self.num = num // a
        self.den = den // a

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def _gcd(self ,a, b):
        while True:
            c = a % b
            if c == 0:
                return b
            else:
                a = b
                b = c

    def __add__(self, other):
        makhraj = self.den * other.den
        soorat1 = self.num * other.den
        soorat2 = other.num * self.den
        return Rational(soorat1 + soorat2, makhraj)

    def __sub__(self, other):
        makhraj = self.den * other.den
        soorat1 = self.num * other.den
        soorat2 = other.num * self.den
        return Rational(soorat1 - soorat2, makhraj)

    def __truediv__(self, other):
        soorat = self.num * other.den
        makhraj = self.den * other.num
        return Rational(soorat, makhraj)

    def __lt__(self, other):
        makhraj = self.den * other.den
        soorat1 = self.num * makhraj
        soorat2 = other.num * makhraj
        if soorat1 < soorat2 :
            return True
        else:
            return False

    def __le__(self, other):
        makhraj = self.den * other.den
        soorat1 = self.num * makhraj
        soorat2 = other.num * makhraj
        if soorat1 <= soorat2 :
            return True
        else:
            return False

    def __gt__(self, other):
        makhraj = self.den * other.den
        soorat1 = self.num * makhraj
        soorat2 = other.num * makhraj
        if soorat1 > soorat2 :
            return True
        else:
            return False

    def __ge__(self, other):
        makhraj = self.den * other.den
        soorat1 = self.num * makhraj
        soorat2 = other.num * makhraj
        if soorat1 >= soorat2 :
            return True
        else:
            return False

    def __eq__(self, other):
        makhraj = self.den * other.den
        soorat1 = self.num * makhraj
        soorat2 = other.num * makhraj
        if soorat1 == soorat2 :
            return True
        else:
            return False

    def __ne__(self, other):
        makhraj = self.den * other.den
        soorat1 = self.num * makhraj
        soorat2 = other.num * makhraj
        if soorat1 != soorat2 :
            return True
        else:
            return False

    def reverse_ceil(self):
        num, den = self.den, self.num
        return ceil(num/den)

    def numinator(self):
        return self.num

    def denominator(self):
        return self.den

