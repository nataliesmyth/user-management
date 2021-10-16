from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.
def home(request, year, month):
    # the curly brackets below is the context dictionary, which allows us to pass data from the backend to the front end of your website
    name = 'Natalie'
    month = month.title()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    return render(request, 
    'home.html', {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
    })