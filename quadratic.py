from polinomial import Polynomial
from math import sqrt, isclose


class Quadratic(Polynomial):
    def __init__(self, coeff_list):
        super().__init__(coeff_list)
        if len(coeff_list) != 3:
            raise ValueError

    def __repr__(self):
        return f"Quadratic(a={self.coeff_list[0]}, b={self.coeff_list[1]}, c={self.coeff_list[2]})"

    def discriminant(self):
        return self.coeff_list[1]**2 - 4 * self.coeff_list[0] * self.coeff_list[2]

    def numberOfRealRoots(self):
        if self.discriminant() > 0:
            return 2
        elif self.discriminant() == 0:
            return 1
        return 0

    def getRealRoots(self):
        ans = []
        if self.discriminant() < 0:
            ans = []
        elif self.discriminant() == 0:
            ans.append((- self.coeff_list[1]) / 2 * self.coeff_list[0])
        else:
            ans.append((-sqrt(self.discriminant()) - self.coeff_list[1]) / (2 * self.coeff_list[0]))
            ans.append((sqrt(self.discriminant()) - self.coeff_list[1]) / (2 * self.coeff_list[0]))
            ans.sort(key=lambda x: x)
        return ans
