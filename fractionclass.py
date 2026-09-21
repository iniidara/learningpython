class SimpleFraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    def plus(self, oth):
        top = self.num*oth.denom + self.denom*oth.num
        bottom = self.denom*oth.denom
        return top/bottom 
    def times(self, oth):
        top = self.num*oth.num
        bottom = self.denom*oth.denom
        return top/bottom
    def get_inverse(self):
        return self.denom/self.num
    def invert(self):
        newnum = self.denom
        newdenom = self.num
        self.num = newnum
        self.denom = newdenom

f1 = SimpleFraction(3, 4)
f2 = SimpleFraction(1, 4)

print(f1.num)
print(f1.denom)
print(f1.plus(f2))
print(f1.times(f2))
print(f1.get_inverse())
f1.invert()
print(f1.num, f1.denom) 