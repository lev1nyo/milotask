from _datetime import datetime
from django import template

register = template.Library()


@register.simple_tag
def allowed(birthday, age):
    today = datetime.now()
    if today.year - birthday.year >= age:
        return "allowed"
    else:
        return "blocked"


@register.simple_tag
def bizz_fuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "BizzFuzz"
    elif number % 3 == 0:
        return "Bizz"
    elif number % 5 == 0:
        return "Fuzz"
    return number
