import calendar
calendar.setfirstweekday(calendar.SUNDAY)
def print_month_calendar(year,month):
    cal=calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatmonth(year,month))
for month in  range(1,13):
    print_month_calendar(2024,month)