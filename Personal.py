import pandas as pd
import os
import datetime as dt
import json

class Personal():
    def __init__(self, csv_obj):
        self.csv_obj = csv_obj

    def try_parsing_date(self,text):
        for fmt in ('%m-%d-%Y', '%m/%d/%Y'):
            try:
                return dt.datetime.strptime(text, fmt)
            except ValueError:
                pass
        raise ValueError('Invalid date format found')

    def calculateage(self,deadline):
        if isinstance(deadline, str):
            currentDate = dt.datetime.now()
            deadlineDate = self.try_parsing_date(deadline)
            daysLeft = deadlineDate - currentDate
            years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
            yearsInt = int(years)
            months = (years - yearsInt) * 12
            monthsInt = int(months)
            return '{0} years {1} months'.format(abs(yearsInt), abs(monthsInt))


    def grade(self, totmark):
        percent = (totmark / 1000) * 100
        if percent >= 90:
            return 'A+'
        elif percent >= 80 and percent <= 89:
            return 'A'
        elif percent >= 70 and percent <= 79:
            return 'B+'
        elif percent >= 60 and percent <= 69:
            return 'B'
        elif percent >= 50 and percent <= 59:
            return 'C'
        elif percent <= 50:
            return 'D'

    def prs_personal(self):
        self.csv_obj['fullName'] = self.csv_obj['firstname'] + ' ' + self.csv_obj['lastname']
        self.csv_obj['age'] = self.csv_obj['dob'].apply(lambda x: self.calculateage(x))
        self.csv_obj['fgender'] = self.csv_obj['gender'].apply(lambda x: 'Male' if (x == 'm') else ('Female' if (x == 'f') else ''))
        self.csv_obj['contact_number'] = self.csv_obj['contact_number'].astype(str)
        self.csv_obj['city'] = self.csv_obj['city'].apply(lambda x: x.capitalize())




