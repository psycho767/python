class cart:
    def __init__(self,product_name,price,quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print(f"Product Name - {self.product_name}")
        print(f"Price - {self.price}")
        print(f"Quantity - {self.quantity}")
        print(f"amount - {self.total_price()}")
        print(f"10 % discount applied over 5000 - {self.discount()}")
        print(f"Final price - {self.total_price() - self.discount()}")

    def total_price(self):
        return  self.price * self.quantity
    

    def discount(self):
        if self.total_price() >= 5000:
            return ((self.total_price()*10)/100)
        else:
            return 0

    
s= cart("Laptop",1000,6)
s.display()


