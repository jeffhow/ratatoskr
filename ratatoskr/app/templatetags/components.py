from functools import reduce
from django.template.defaulttags import register

def ctx(c):
    return reduce(lambda a, b: a | b, c, {})

@register.inclusion_tag("app/components/test.html")
def test_component(echo):
    return {
        "echo": echo
    }

@register.inclusion_tag("app/components/login_button.html")
def login_button():
    return {}

@register.inclusion_tag("app/components/logout_button.html")
def logout_button():
    return {}

@register.inclusion_tag("app/components/schedule_card.html")
def schedule_card(schedule):
    return {
        "schedule": schedule 
    }   

@register.inclusion_tag("app/components/timeslot_card.html")
def timeslot_card(date, timeslots):
    return {
        "date": date,
        "timeslots": timeslots
    }   

@register.inclusion_tag("app/components/timeslot_date.html", takes_context=True)
def timeslot_date(context, date, schedule, from_time, to_time):
    return ctx(context) | {
        "date": date,
        "schedule": schedule,
        "from_time": from_time,
        "to_time": to_time
    }   

@register.inclusion_tag("app/components/timeslot_time.html")
def timeslot_time(timeslot):
    return {
        "timeslot": timeslot,
    }   
