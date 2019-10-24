import getdata


if __name__ == "__main__":
    instruments = getdata.get_constituent_list()
    constituents = getdata.get_id(instruments)
    close_price = getdata.get_constituents_prev_close_price(constituents)
    print(close_price)