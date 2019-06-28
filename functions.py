def beef():  # any line after colon will be executed
    print("This is a function.")


def bitcoin_to_usd(btc):  # take a bitcoin value and turn it to United States Dollar
    amount = btc * 527
    print("The USD amount is", amount, ".")


beef()  # calling the function
bitcoin_to_usd(3.85)
bitcoin_to_usd(1)
bitcoin_to_usd(11)
