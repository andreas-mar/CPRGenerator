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
        self.birthdate = self._get_birthdate_from_cpr()
        # Map first name
        self.cpr_no_dash = self.cpr.replace('-', '')
        self.is_male = 'Mand' if int(self.cpr) % 2 == 0 else 'Kvinde'
        self.mod_11_check = self.validate_CPR(self.cpr)


    def _get_birthdate_from_cpr(self) -> dt.date:
        current_year = dt.datetime.now().year
        day = int(self.cpr[0:2])
        month = int(self.cpr[2:4])
        year = int(self.cpr[4:6])
        final_year = 1900 + year if year < current_year else 2000 + year
        return str(dt.date(final_year, month, day).strftime('%d-%m-%Y'))



    def to_dict(self):
        return {'first_name' : 'test',
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
