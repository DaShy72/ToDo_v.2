from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date,timedelta
import calendar
from django.utils.dateparse import parse_date
from .models import Task


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

    next_week = today + timedelta(days=7)
    events = Task.objects.filter(user=request.user, event_date__range=[today, next_week])

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
        'events': events,
    }

    return render(request, 'main_app/calendar.html', context)


def add_event(request):
    initial_date = request.GET.get('date')
    if initial_date:
        initial_date = parse_date(initial_date)

    events = Task.objects.filter(user=request.user, event_date=initial_date)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(user=request.user, title=title, description=description, event_date=initial_date,
                            is_done=False)
    return render(request, 'main_app/add_event.html', {'events': events})



















