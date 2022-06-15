import matplotlib.pyplot as plt
import matplotlib.ticker as tck


def plot_currency(lst_value, lst_date, code):
    """
    This function draw a plot of currency values change in time

    :param lst_value: list of currency values from API
    :param lst_date: corresponding with values list of dates from API
    :param code: unified code of the currency
    :return: None
    """

    fig, axes = plt.subplots(figsize=(12, 15))
    plt.title(f"Plot currency value for {code.upper()}")
    plt.plot(lst_date, lst_value, linestyle='--', marker='o', color='b')
    plt.xticks(rotation=90)
    axes.yaxis.set_minor_locator(tck.AutoMinorLocator())
    plt.grid(True)
    plt.xlim([lst_date[0], lst_date[-1]])
    plt.show()
