import datetime as dt
import numpy as np
import random
from faker import Faker
class CPRGenerator:
    def __init__(self, start: dt.datetime.date = None, end: dt.datetime.date = None, bootstrap: bool = False):
        self.control = np.array([int(n) for n in str(432765432)])
        fake = Faker()
        self.birthdate = fake.date_time_between(start_date=start, end_date=end).date()
        if bootstrap:
            self.start = start
            self.end = end
            self.cpr = self.create_new_CPR()
        else:
            self.cpr = None
    def validate_CPR(self, cpr: str) -> bool:
        cpr = cpr.replace('-', '')
        if len(cpr) != 10:
            return False
        cpr_control = np.array([int(n) for n in str(cpr[:-1])]) * self.control
        remainder = cpr_control.sum() % 11
        control_digit = 11 - remainder
        return control_digit == int(cpr[-1])

    def _get_CPR_control_number(self, cpr: str) -> bool:
        cpr = cpr.replace('-', '')
        cpr_control = np.array([int(n) for n in str(cpr)]) * self.control
        remainder = cpr_control.sum() % 11
        control_digit = 11 - remainder
        return control_digit
    def create_new_CPR(self) -> str:

        first_six_digits = self.birthdate.strftime('%d%m%y')
        year = self.birthdate.year
        seventh_digit_options = []
        if year < 2000 and year >= 1900:
            seventh_digit_options.extend([0, 1, 2, 3])
            if year > 1937:
                seventh_digit_options.extend([4, 9])
        elif year <= 2000:
            seventh_digit_options.extend([4, 5, 6, 7, 8, 9])
        else:
            seventh_digit_options.extend([5, 6, 7, 8])

        seventh_digit = random.choice(seventh_digit_options)
        eight_nine_digits = str(random.randint(0, 99)).zfill(2)
        out = first_six_digits + str(seventh_digit) + eight_nine_digits
        control_digit = self._get_CPR_control_number(out)
        out += str(control_digit)

        return out

if __name__ == '__main__':
    start = dt.datetime.strptime('01-01-1900', '%d-%m-%Y').date()
    end = dt.datetime.strptime('01-01-2000', '%d-%m-%Y').date()
    cpr = CPRGenerator(start, end, bootstrap=True)
    print(cpr.cpr)
    print(cpr.validate_CPR(cpr.cpr))
    x = 2