
class Employee:

    def __init__(self, first, last, tele, pay):
        self.first = first
        self.last = last
        self.tele = tele
        self.pay = pay
        self.pay_raise = 1.05

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@iths.se'.format(self.first, self.last)

    @property
    def telenr(self):
        return 'tele: {}'.format(self.tele)

    @property
    def salary(self):
        return 'pay: {}'.format(self.pay)

    @property
    def salary_raise(self):
        return 'new salary: {}'.format(int(self.pay * self.pay_raise))
