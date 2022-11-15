

class Employee:

    def __init__(self, first, last, tele, pay):
        self.first = first
        self.last = last
        self.tele = tele
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
