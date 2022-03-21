"""Working with polynomials."""


class Polynomial:
    """
    CLass that stores parameters about the polymonial and
    has methods to work with math problems.
    """
    def __init__(self, coeff_list: list):
        """
        Stores the following parameter:
        :param coeff_list: list
        Excludes the fact of tuple instead of list.
        Makes the zeroes before the degree disappear.
        """
        self.coeff_list = coeff_list
        if len(self.coeff_list) == 0:
            self.coeff_list = [0]
        for i in range(len(self.coeff_list)):
            if self.coeff_list[i] != 0:
                self.coeff_list = self.coeff_list[i:]
                break
        if type(self.coeff_list) == tuple:
            self.coeff_list = list(self.coeff_list)

    def __repr__(self) -> str:
        """
        Represents the info about the class object.
        :return: str
        """
        return "Polynomial(coeffs=" + str(self.coeff_list) + ")"

    def degree(self) -> int:
        """
        Returns the degree of the polynomial
        :return: int
        """
        return len(self.coeff_list) - 1

    def coeff(self, num: int) -> float:
        """
        Returns the coefficient with the exact number.
        :param num: int
        :return: float
        """
        return self.coeff_list[len(self.coeff_list)-num-1]

    def evalAt(self, value: float) -> float:
        """
        Gets the evaluation at an exact point.
        :param value: float
        :return: float
        """
        ans = 0
        for i in range(len(self.coeff_list)):
            ans += value**i * self.coeff_list[::-1][i]
        return ans

    def __eq__(self, other) -> bool:
        """
        Compares the two class objects and tests their equality.
        :param other: Polynomial object
        :return: bool (True if equal)
        """
        if type(self) == type(other):
            if self.coeff_list == other.coeff_list:
                return True
        elif type(other) == int and len(self.coeff_list) == 1:
            if self.coeff_list[0] == other:
                return True
        return False

    def __hash__(self):
        """
        Allows to add objects into sets with the hash function.
        :return:
        """
        for i in self.coeff_list:
            return hash(i)

    def scaled(self, num: float):
        """
        Scales all the coefficients on the exact number.
        :param num: float
        :return: Polynomial object
        """
        ans = []
        for i in self.coeff_list:
            ans.append(i * num)
        return Polynomial(ans)

    def derivative(self):
        """
        Gets the derivative for the polynomial
        :return: Polynomial object
        """
        ans = []
        for i in range(len(self.coeff_list)-1, -1, -1):
            ans.append(i*self.coeff_list[::-1][i])
        return Polynomial(ans[:-1])

    def addPolynomial(self, other):
        """
        Adds two Polynomial objects.
        :param other: Polynomial object
        :return: Polynomial object
        """
        ans = []
        for i in range(len(self.coeff_list) + len(other.coeff_list)):
            try:
                ans.append(self.coeff_list[i] + other.coeff_list[i])
            except IndexError:
                break
        return Polynomial(ans)

    def multiplyPolynomial(self, other):
        """
        Multiplies two Polynomial objects.
        :param other: Polynomial object
        :return: Polynomial object
        """
        pass


p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
p3 = p1.derivative() # 4x - 3
p4 = p1.addPolynomial(p3) # (2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
print(p4)
