class Polynomial:
    """
    CLass that stores parameters about the polymonial and
    has methods to work with math problems.
    """
    def __init__(self, coeff_list):
        self.coeff_list = coeff_list

    def __repr__(self):
        return "Polynomial(coeffs=" + str(self.coeff_list) + ")"

    def degree(self):
        return len(self.coeff_list) - 1

    def coeff(self, num):
        return self.coeff_list[len(self.coeff_list)-num-1]

    def evalAt(self, value):
        ans = 0
        for i in range(len(self.coeff_list)):
            ans += value**i * self.coeff_list[::-1][i]
        return ans

    def __eq__(self, other):
        if type(self) == type(other):
            if self.coeff_list == other.coeff_list:
                return True
        elif type(other) == int and len(self.coeff_list) == 1:
            if self.coeff_list[0] == other:
                return True
        return False

    def scaled(self, num):
        pass

    def derivative(self):
        pass

    def addPolynomial(self, other):
        pass

    def multiplyPolynomial(self, other):
        pass
