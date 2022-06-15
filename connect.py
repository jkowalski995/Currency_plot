import requests


def ask_about_currency(code, start, stop, lst_value=None, lst_date=None):
    """
    This function ask NBP API about currency values in provided range of time

    :param code: unified code of the currency
    :param start: start date for plot
    :param stop: end date for plot
    :param lst_value: list of currency values from API
    :param lst_date: corresponding with values list of dates from API
    :return: both lists
    """

    code = str(code).lower()
    url = "http://api.nbp.pl/api/exchangerates/rates/a/"+code+"/"+start+"/"+stop+"/"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers).json()

    for idx, value in enumerate(response['rates']):
        if lst_value is None:
            lst_value = []
        lst_value.append(response['rates'][idx]['mid'])
        if lst_date is None:
            lst_date = []
        lst_date.append(response['rates'][idx]['effectiveDate'])

    return lst_value, lst_date
