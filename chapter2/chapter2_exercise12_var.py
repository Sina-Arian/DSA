'''12.Write a class to represent a plynomial. The class should store ...s'''

class Variable:
    def __init__(self, coeff:int, degree = 0):
        self.coeff = coeff
        self.deg = degree
    
    def __str__(self):
        return '{self.coeff}x**{self.deg}'.format(**locals())
    
    def __add__(self, other):
        if self.deg != other.deg:
            return 'They have diffrent degrees'
        else:
            return Variable(self.coeff + other.coeff, self.deg)

    def __iadd__(self, other):
        if self.deg != other.deg:
            return 'They have diffrent degrees'
        else:
            self.coeff = self.coeff + other.coeff
            return Variable(self.coeff , self.deg)

    def __sub__(self, other):
        if self.deg != other.deg:
            return 'They have diffrent degrees'
        else:
            return Variable(self.coeff - other.coeff, self.deg)
    
    def __mul__(self, other):
        return Variable(self.coeff*other.coeff, self.deg + other.deg)
    
    def coefficient(self):
        return self.coeff
    
    def degree(self):
        return self.deg

    def attri(self):
        if self.coeff > 0:
            return '+'
        elif self.coeff < 0:
            return '-'

class Polynomial:
    def __init__(self, coefficient:list): #coefficient is a list of Variable class objects
        for i in coefficient:
            i_ind = coefficient.index(i) + 1
            for t in coefficient[i_ind:]:
                if i.degree() == t.degree():
                    temp = coefficient.pop(coefficient.index(t))
                    i += temp
        self.coeff = coefficient
        self.deg = 0
        for i in self.coeff:
            if i.degree() > self.deg:
                self.deg = i.degree()

    def __add__(self, other):
        res_lst = []
        for i in self.coeff:
            for t in other.coeff:
                if i.degree() == t.degree():
                    c = i + t
                    res_lst.append(c)
        return Polynomial(res_lst)

    def __sub__(self, other):
        res_lst = []
        for i in self.coeff:
            for t in other.coeff:
                if i.degree() == t.degree():
                    c = i - t
                    res_lst.append(c)
        return Polynomial(res_lst)

    def __str__(self):
        res = []
        for i in self.coeff:
            res.append(str(i))
        res = ' '.join(res)
        return res

    def __mul__(self, other):
        res = []
        for i in self.coeff:
            for t in other.coeff:
                a = i * t
                res.append(a)
        return Polynomial(res)
