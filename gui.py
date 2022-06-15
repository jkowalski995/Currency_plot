"""This application draw a plot of currency values change in provided time range. Polish National Bank (NBP) API
provides information about values on two tables A and B. In order to keep it as simple as possible I only work with
table A so not every currency is available. List of currency is below:

THB USD AUD HKD CAD NZD SGD EUR HUF CHF GBP UAH JPY CZK DKK ISK NOK SEK HRK RON BGN TRY ILS CLP
PHP MXN ZAR BRL MYR IDR INR KRW CNY XDR

"""
import json

import PySimpleGUI as Sg
import datetime

import requests

import connect
import plot

layout = [
    [Sg.Text("Provide the unified name of the currency", size=(40, 1)), Sg.InputText(key="-code-")],
    [Sg.Text("Provide the start date of the plot", size=(40, 1)), Sg.InputText('YYYY-MM-DD', key="-start-")],
    [Sg.Text("Provide the end date of the plot", size=(40, 1)), Sg.InputText('YYYY-MM-DD', key="-stop-")],
    [Sg.Button("Plot")],
    [Sg.Exit()]
]


def check_date_format(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        Sg.popup(f"Wrong data format in {date}, should be YYYY-MM-DD", title="Result!", line_width=300)


if __name__ == '__main__':

    window = Sg.Window(title="Currency plot", layout=layout, margins=(100, 50))

    while True:
        event, values = window.read()
        print(event, values)

        # Exit the program
        if event == Sg.WINDOW_CLOSED or event == 'Exit':
            break

        currency_code = values["-code-"]
        start_date = values["-start-"]
        end_date = values["-stop-"]

        # Check if code is in table A
        codes_lst = ['THB', 'USD', 'AUD', 'HKD', 'CAD', 'NZD', 'SGD', 'EUR', 'HUF', 'CHF', 'GBP', 'UAH', 'JPY', 'CZK',
                     'DKK', 'ISK', 'NOK', 'SEK', 'HRK', 'RON', 'BGN', 'TRY', 'ILS', 'CLP', 'PHP', 'MXN', 'ZAR', 'BRL',
                     'MYR', 'IDR', 'INR', 'KRW', 'CNY', 'XDR']
        if currency_code not in codes_lst:
            Sg.popup(f"Provided {currency_code} is not in code list! \nTry another value. Available values:\n"
                     f"{codes_lst[:10]}\n{codes_lst[11:21]}\n{codes_lst[22:32]}\n{codes_lst[33:]}", title="Code!",
                     line_width=500)
            continue

        # Check the values if any is empty
        if currency_code == '' or start_date == '' or end_date == '':
            Sg.popup("Every field must be filled with proper value", title="Result!", line_width=300)
            continue

        # Check data format
        check_date_format(start_date)
        check_date_format(end_date)

        # Get data from API
        try:
            data = connect.ask_about_currency(currency_code, start_date, end_date)
        except (json.decoder.JSONDecodeError, requests.exceptions.JSONDecodeError) as e:
            Sg.popup("Provided range is to big to be handled as json! \nCorrect Your range and try again!",
                     title="Range!", line_width=300)
            continue

        # Draw a plot
        if event == 'Plot':
            plot.plot_currency(data[0], data[1], currency_code)

    window.close()
