from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
import calendar

@login_required
def calendar_view(request, year=None, month=None):
    today = date.today()

    try:
        year = int(year) if year else today.year
        month = int(month) if month else today.month
    except (TypeError, ValueError):
        year, month = today.year, today.month

    if month == 1:
        prev_month, prev_year = 12, year - 1
    else:
        prev_month, prev_year = month - 1, year

    if month == 12:
        next_month, next_year = 1, year + 1
    else:
        next_month, next_year = month + 1, year

    cal = calendar.Calendar(firstweekday=0)
    month_days = list(cal.itermonthdays(year, month))

    eng_months = [
        '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
        'October', 'November', 'December'
    ]
    month_name = eng_months[month]

    day_today = today.day
    month_today = eng_months[today.month]
    year_today = today.year

    context = {
        'day_today': day_today,
        'month_today': month_today,
        'year_today': year_today,
        'year': year,
        'month': month,
        'month_name': month_name,
        'month_days': month_days,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    }


    return render(request, 'main_app/calendar.html', context)