class Seller:
    def __init__(self):
        self.products_quantity={} # dictionary storing product name and quantity as key and value pair
        self.products_price={} # same as above name and price
        self.profit=0

    def update(self):
        item_name=input("Enter name of item-")
        item_quantity=int(input("Enter quantity-"))
        item_price=int(input("Enter selling price"))
        self.products_quantity[item_name]=item_quantity #setting the key value pairs for the dictionary
        self.products_price[item_name]=item_price

    def show(self):
        for i,j in self.products_quantity.items():
            print(i,j)

    def buy(self,item_name,quantity):
        if quantity>self.products_quantity.get(item_name):
            print("We dont have sufficient quantity")
        else:
            self.products_quantity[item_name]=self.products_quantity.get(item_name)-quantity
            self.profit += self.products_price.get(item_name)*quantity
