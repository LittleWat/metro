import json
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import pprint

class OneMonthPay:

    def __init__(self, start_date: date, end_date: date, payment: int):
        self.start_date = start_date
        self.end_date = end_date
        self.payment = payment

    def __str__(self):
        return "%s - %s: %d"%(self.start_date.strftime("%Y-%m-%d"), self.end_date.strftime("%Y-%m-%d"), self.payment)


f = open("./input.json", "r")
input_json = json.load(f)
pprint.pprint(input_json)

checkin_date = datetime.strptime(input_json["checkin_date"], '%Y-%m-%d')
checkout_date = datetime.strptime(input_json["checkout_date"], '%Y-%m-%d')
monthly_payment = input_json["monthly_payment"]
oneday_payment = int(monthly_payment / 30)

now_nonth_date = checkin_date
next_month_date = now_nonth_date + relativedelta(months=1) - timedelta(days=1)

results = []
while (next_month_date <= checkout_date):
    results.append(
        OneMonthPay(now_nonth_date, next_month_date, monthly_payment)
    )

    now_nonth_date += relativedelta(months=1)
    next_month_date += relativedelta(months=1)

last_month_payment = ((checkout_date - now_nonth_date).days + 1) * oneday_payment
results.append(
    OneMonthPay(now_nonth_date, checkout_date, last_month_payment)
)

for result in results:
    print(result)