from app.BusinessLogic.CPRGenerator import CPRGenerator
import datetime as dt
from app.DataAccess.Models import FirstNames


class FictionalPerson(CPRGenerator):
    def __init__(self, lastname: str, start: dt.date = None, end: dt.date = None):
        # init CPRGenerator
        start = start
        end = end
        super().__init__(start, end, bootstrap=True)

        self.last_name = lastname
        self.cpr_no_dash = self.cpr.replace('-', '')
        self.is_male = 'Mand' if int(self.cpr) % 2 == 0 else 'Kvinde'
        self.mod_11_check = self.validate_CPR(self.cpr)
        self.firstname = 'none'

    def to_dict(self):
        return {'first_name' : self.firstname,
                'last_name': self.last_name,
                'cpr': self.cpr,
                'birthdate': self.birthdate,
                'gender': self.is_male,
                'cpr_no_dash': self.cpr_no_dash,
                'mod_11_compliant': str(self.mod_11_check)}


if __name__ == '__main__':
    p = FictionalPerson('f', 'test', 'Male')
    print(p.to_dict())
    x = 2
