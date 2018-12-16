import csv
import requests

#---------------------------------------------------------------------------------------
# CSV_file class object
# This object is used to store CSV info. This allows us to request and parse just once
# to allow for quicker queries
#---------------------------------------------------------------------------------------

class csv_file():
    _valid_csv_fields = ['employee_id', 'company', 'tenure_years', 'time_in_role_years',
                    'age_years', 'compensation_base', 'compensation_bonus', 'performance',
                    'compensation_equity', 'attrition_risk']

    _company_fields = ['company', 'industry', 'geography']

    def __init__(self):
        self._reader = None
        self._companies = None
        self._companyInfo = None

    def _get_csv_companies(self):
        url = "https://s3.amazonaws.com/twine-labs-engineering-public/dec-2018/companies.csv"
        res = requests.get(url)
        decoded = res.content.decode('utf-8')
        reader = csv.reader(decoded.splitlines(), delimiter=',')
        return list(reader)

    def _get_csv_employees(self):
        url = "https://s3.amazonaws.com/twine-labs-engineering-public/dec-2018/employees.csv"
        res = requests.get(url)
        decoded = res.content.decode('utf-8')
        reader = csv.reader(decoded.splitlines(), delimiter=',')
        return list(reader)

    def _get_all_companies(self):
        buf = set()
        for row in self.reader:
            buf.add(row[csv_file._valid_csv_fields.index('company')])
        return sorted(list(buf))

    @property
    def companyInfo(self):
        if self._companyInfo == None:
            self._companyInfo = self._get_csv_companies()
        return self._companyInfo

    @property
    def reader(self):
        if self._reader == None:
            self._reader = self._get_csv_employees()
        return self._reader

    @property
    def companies(self):
        if self._companies == None:
            self._companies = self._get_all_companies()
        return self._companies

