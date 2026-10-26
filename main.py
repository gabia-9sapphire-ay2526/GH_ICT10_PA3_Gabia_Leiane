# countries capitals
from pyscript import display, document

def countries_capital(e):
    document.getElementById('output').innerHTML = ' '
    user_input = document.getElementById('input1').value.capitalize().strip()

    countries = {
    'Philippines':'Manila',
    'France':'Paris',
    'Germany':'Berlin',
    'Spain':'Madrid',
    'Japan':'Tokyo',
    'China':'Beijing',
    'South Korea':'Seoul'
    }

    countries_checker = user_input in countries

    display_message = (f'Sorry, there is no {user_input} in the list', f'{user_input} is in the list')

    display(display_message[countries_checker], target='result')
