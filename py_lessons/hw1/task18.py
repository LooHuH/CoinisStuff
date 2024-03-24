from askvar import askvar

ps5_price = askvar('PS5 price')
ps5_price_up = ps5_price * 1.1
ps5_price_down = ps5_price_up * 0.9

print(f'''\
Price after +10% - {ps5_price_up}
+10% Price after -10% - {ps5_price_down}
''')
