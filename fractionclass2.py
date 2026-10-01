class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        return str(self.num) + "/" + str(self.denom)
    def __mul__(self, oth):
        top = self.num*oth.num
        bottom = self.denom*oth.denom
        return Fraction(top, bottom)
    def __add__(self, oth):
        top = self.num*oth.denom + self.denom*oth.num
        bottom = self.denom * oth.denom
        return Fraction(top, bottom)
    def __float__(self):
        return self.num/self.denom
    def reduce(self):
        def gcd(n, d):
            while d != 0:
                (d, n) = (n%d, d)
            return n
        if self.denom == 0:
            return None
        elif self.denom == 1:
            return self.num
        else:
            greatest_common_divisor = gcd(self.num, self.denom)
            top = int(self.num/greatest_common_divisor)
            bottom = int(self.denom/greatest_common_divisor)
            return Fraction(top, bottom)

f1 = Fraction(3, 4)
f2 = Fraction(1, 4)
f3 = Fraction(5, 1)
f4 = f1*f2*f3
f5 = f1+f2+f3+f4
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)
print(float(f5))
print(f5.reduce())
