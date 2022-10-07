class StockAccount():
    def __init__(self,name,no_of_share,price_of_share):
        self.name=name
        self.no_of_share=no_of_share
        self.price_of_share=price_of_share

    def buy(self,amount):
        pass

    def sell(self):
        pass

    def save(self):
        pass
    
    def print_report(self):
        pass

if __name__=="__main__":
    print
    obj_account=StockAccount("Mahindra", 100, 10000)
    obj_account.print_report()