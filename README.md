# Currency_plot

This is the simple currency plot made by using the PySimpleGUI.

I made this as my own one-day coding challenge. 

## This repository consits of 3 files:
- `gui.py` witch is the main app witch generate the GUI and ask user for providing the data
- `plot.py` this is a file containing the function drawing a plot in provided range
- `connect.py` here this file connects with Polish National Bank (NBP) API and `GET` the required data

Polish National Bank (NBP) API
provides information about values on two tables A and B. In order to keep it as simple as possible I only work with
table A so not every currency is available. List of currency is below:

THB
USD
AUD
HKD
CAD
NZD
SGD
EUR
HUF
CHF
GBP
UAH
JPY
CZK
DKK
ISK
NOK
SEK
HRK
RON
BGN
TRY
ILS
CLP
PHP
MXN
ZAR
BRL
MYR
IDR
INR
KRW
CNY
XDR