class cart:
    def __init__(self,name,price,qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total_price(self):
        return self.price * self.qty

    def display(self):
        print(f"Name-{self.name}")
        print(f"Price-{self.price}")
        print(f"Quantity-{self.qty}")
        print(f"Total Price-{self.total_price()}")
    
cart_det = cart("hitesh",1000,5.5)
cart_det.display();
