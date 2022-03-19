class Polynomial:
    """
    CLass that stores parameters about the polymonial and
    has methods to work with math problems.
    """
    def __init__(self, coeff_list):
        self.coeff_list = coeff_list
        if len(self.coeff_list) == 0:
            self.coeff_list = [0]
        for i in range(len(self.coeff_list)):
            if self.coeff_list[i] != 0:
                self.coeff_list = self.coeff_list[i:]
                break
        if type(self.coeff_list) == tuple:
            self.coeff_list = list(self.coeff_list)

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

    def __hash__(self):
        for i in self.coeff_list:
            return hash(i)

    def scaled(self, num):
        ans = []
        for i in self.coeff_list:
            ans.append(i * num)
        return Polynomial(ans)

    def derivative(self):
        ans = []
        for i in range(len(self.coeff_list)-1, -1, -1):
            ans.append(i*self.coeff_list[::-1][i])
        return Polynomial(ans[:-1])

    def addPolynomial(self, other):
        ans = []
        for i in range(max(len(self.coeff_list), len(other.coeff_list))):
            if min(len(other.coeff_list), len(self.coeff_list)) - 1 <= i:
                ans.append(self.coeff_list[i] + other.coeff_list[i])
            else:
                break
        return Polynomial(ans)

    def multiplyPolynomial(self, other):
        pass


p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
p3 = p1.derivative() # 4x - 3
p4 = p1.addPolynomial(p3) # (2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
print(p4)
