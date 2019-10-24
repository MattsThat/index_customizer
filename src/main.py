import getdata


if __name__ == "__main__":
    constituents = ['6758:JP']
    close_price = getdata.get_constituents_price(constituents)
    print(close_price)