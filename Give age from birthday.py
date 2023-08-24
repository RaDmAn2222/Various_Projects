import datetime
from dateutil import relativedelta

birthday = input('Enter your birthday(yyyy/mm/dd): ')
birthday1 = birthday.split('/')
birthday1.reverse()
birthday2 = '-'.join(birthday1)

start_date = datetime.datetime.strptime(birthday2, "%d-%m-%Y")
end_date = datetime.date.today()
delta = relativedelta.relativedelta(end_date, start_date)

print('Your age is %s years and %s months and %s days'%(delta.years, delta.months, delta.days))