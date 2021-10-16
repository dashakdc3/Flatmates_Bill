class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill + number of flatmates
    """

    def __init__(self, amount, period, flatmates):
        self.amount = amount
        self.period = period
        self.flatmates = flatmates


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, flatmate1=None, dih1=0, flatmate2=None, dih2=0, flatmate3=None, dih3=0, flatmate4=None, dih4=0, flatmate5=None, dih5=0):
        self.name = flatmate1
        self.f2 = flatmate2
        self.f3 = flatmate3
        self.f4 = flatmate4
        self.f5 = flatmate5
        self.dih1 = dih1
        self.dih2 = dih2
        self.dih3 = dih3
        self.dih4 = dih4
        self.dih5 = dih5

    def pays(self, bill,):
        weight = self.dih1 / \
            (self.dih1 + self.dih2 + self.dih3 + self.dih4 + self.dih5)
        to_pay = bill.amount * weight
        return round(to_pay)


# a = Flatmate(flatmate1="Dasha", dih1=10, flatmate2="Sasha",
#              dih2=15, flatmate3="Nika", dih3=20)
# b = Bill(amount=120, period="March", flatmates=3)
# print(a.pays(bill=b))
