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


class Buyer:
    def __init__(self):
        self.cart={} # this dictionary will contain the name of item and the money spent on it
        self.quantity={} # item name and quantity
        self.total_amount=0

    def search(self,seller,item_name):
        if seller.products_quantity.get(item_name):
            print("Quantity "+ str(seller.products_quantity.get(item_name)))
            print("Price per product " + str(seller.products_price.get(item_name)))
            choice=input(print("Do you want add into the cart? y/n"))
            if choice=="y":
                quantity=int(input("Enter quantity:"))
                if quantity>seller.products_quantity.get(item_name):
                    print("Quantity does not exist ")
                    self.search(seller,item_name) #calling the function again
                else:
                    self.cart[item_name]=seller.products_price.get(item_name)*quantity
                    self.quantity[item_name]=quantity
                    self.total_amount+=seller.products_price.get(item_name)*quantity
            
            else:
                pass
        else:
            print("The product doesnt exist") 

    def show(self):
        print("Showing items......")
        for i,j in self.cart.items():
            print(i,j)

    def buy(self,seller):
        print("These are the items in your cart")
        self.show()
        print("Total payable amount is: "+str(self.total_amount))
        for item,quantity in self.quantity.items():
            seller.buy(item,quantity)

out_option=True
seller=Seller()
buyer=Buyer()
while(out_option):
    choice=input("Are you buyer or seller? b/s-")
    if choice=="s":
        option=True
        while(option):
            print("1. Update items")
            print("2. Show items")
            print("3. Exit")
            choice=input("Enter choice-")

            if choice=="1":
                seller.update()
            elif choice=="2":
                seller.show()
            elif choice=="3":
                option= False  
            else:
                print("Invalid choice")
    
    elif choice=="b":
        option=True
        while(option):
            print("1. Search items")
            print("2. Buy items")
            print("3. Exit")
            choice=input("Enter choice-")

            if choice=="1":
                item_name=input("Enter name of product ")
                buyer.search(seller,item_name)
            elif choice=="2":
                buyer.buy(seller)
            elif choice=="3":
                option= False  
            else:
                print("Invalid choice")
    else:
        out_option=False
        print("Exiting system.... Thank you for staying")

