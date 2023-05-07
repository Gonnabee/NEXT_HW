from datetime import date
import datetime
from django import template

register = template.Library()

def due_date(deadline):
    current_date = datetime.date.today()
    delta = deadline - current_date

    return delta.days

register.filter('due_date', due_date)