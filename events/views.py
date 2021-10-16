from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.
def home(request, year, month):
    name = 'Natalie'
    month = month.title()

    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create a calendar

    cal = HTMLCalendar().formatmonth(year, month_number)

    return render(request, 
    # the curly brackets below is the context dictionary, which allows us to pass data from the backend to the front end of your website
    'home.html', {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
    })