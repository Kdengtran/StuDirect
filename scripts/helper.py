from datetime import date, datetime

# geboortedatum omrekenen naar leeftijd
def age(datum):

    born = datetime.strptime(datum, "%d/%m/%Y").date()
    today = date.today()

    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    return '\nYou\'re {} years old!'.format(age)