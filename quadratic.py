"""Working with quadratic equations"""
from polinomial import Polynomial
from math import sqrt


class Quadratic(Polynomial):
    """
    Child class to Polynomial.
    Allows to store parameters for quadratic polynomials.
    Has methods to work with quadratic equations.
    """
    def __init__(self, coeff_list):
        super().__init__(coeff_list)
        if len(coeff_list) != 3:
            raise ValueError

    def __repr__(self) -> str:
        """
        Represents the info about the class object.
        :return: str
        """
        return f"Quadratic(a={self.coeff_list[0]}, b={self.coeff_list[1]}, c={self.coeff_list[2]})"

    def discriminant(self) -> float:
        """
        Returns the discriminant for the quadratic equation.
        :return: float
        """
        return self.coeff_list[1]**2 - 4 * self.coeff_list[0] * self.coeff_list[2]

    def numberOfRealRoots(self) -> int:
        """
        Returns the number of real roots depending on the discriminant.
        :return: int
        """
        if self.discriminant() > 0:
            return 2
        elif self.discriminant() == 0:
            return 1
        return 0

    def getRealRoots(self) -> list:
        """
        Finds the roots of the equation and returns a list of them.
        :return: list
        """
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
