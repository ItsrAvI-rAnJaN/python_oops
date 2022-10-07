class Stocks:
    def __init__(self, name, no_of_share, price_of_share):
        self.name = name
        self.no_of_share = no_of_share
        self.price_of_share = price_of_share

    def display_stock(self):
        print(name)
        print(no_of_share)
        print(price_of_share)


class TotalValueOfStocks(Stocks):
    def __init__(self, value_of_stocks):
        self.value_of_stocks = value_of_stocks

    def totalvalue(self):
        value_of_stocks = no_of_share*price_of_share
        print("total Value of Share :", value_of_stocks)


if __name__ == "__main__":
    obj_share = Stocks("Airtel", 20, 100)
    obj_share.display_stock()
    obj_value = TotalValueOfStocks()
    obj_share.totalvalue()
