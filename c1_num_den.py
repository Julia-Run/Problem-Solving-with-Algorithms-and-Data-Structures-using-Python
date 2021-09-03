def gcd(s, m):
    while m % s != 0:
        m, s = s, m % s
    return s


class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    # def show(self):
    #     print(str(self.num) + '/' + str(self.den))

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        num_new = self.num * other.den + self.den * other.num
        den_new = self.den * other.den
        common = gcd(num_new, den_new)
        if den_new / common < 0:
            return Fraction(-num_new // common, -den_new // common)
        else:
            return Fraction(num_new // common, den_new // common)

    def __sub__(self, other):
        num_new = self.num * other.den - self.den * other.num
        den_new = self.den * other.den
        common = gcd(num_new, den_new)
        if den_new / common < 0:
            return Fraction(-num_new // common, -den_new // common)
        else:
            return Fraction(num_new // common, den_new // common)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num


a = Fraction(-3, 50)
b = Fraction(-1, 2)
c = a + b
d = b - a
print(a, b, c, d, a == b, sep='    ')
