# -*- coding: utf-8 -*-
import re
# https://docs.python.org/3/library/re.html
# https://regex101.com/

my_values = [
  " 1.00 Fr",
  " 4.00 Fr",
  " 1,00 $",
  " 7,00",
  "Yen 700",
  "7.00 blabla",
  "what!what!",
  "㖐塬润㬵擑憔㩔޽⤰䙝ޡ鈞좞㴦署㤐㒁 0.99",
  "☀㆙ 0.99"
]

compiled_regex = re.compile('([^\s\d]*)\s*(\d+([.,]\d+)?)\s*([^\s\d]*)')
for value in my_values:
    m = compiled_regex.match(value)
    if m:
        currency_before = m.group(1)
        price = m.group(2)
        currency_after = m.group(4)
        currency = currency_after
        if not currency:
            currency = currency_before
        print("Found [%s] [%s]" % (price, currency))
    else:
        print("Failed to match %s" % value)

def parsing_price(my_values):
    compiled_regex = re.compile('([^\s\d]*)\s*(\d+([.,]\d+)?)\s*([^\s\d]*)')
    lst_price = []
    lst_currency = []    
    for value in my_values:
        m = compiled_regex.match(value)
        if m:
            currency_before = m.group(1)
            price = m.group(2)
            currency_after = m.group(4)
            currency = currency_after
            if not currency:
                currency = currency_before
                lst_currency.append(currency)
            lst_price.append(price)
            lst_currency.append(currency)
    return lst_price,lst_currency

print parsing_price(my_values)