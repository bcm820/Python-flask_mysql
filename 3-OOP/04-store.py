
class Product(object):
    
    def __init__(self, item, price, weight, brand, cost):
        self.item = item
        self.price = price
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
    def Sell(self):
        self.status = "sold"
        return self.status
    
    def addTax(self, tax):
        self.price *= tax
        return self.price

    def returnItem(self, reason):
        if reason.find('defect' or 'broke' or 'malfunction' or 'not work') > -1:
            self.status = "defective"
            self.price = 0
        if reason.find('new' or 'unopen' or 'with box' or 'not open') > -1:
            self.status = "for sale"
        if reason.find('opened' or 'used') > -1:
            self.status = "used"
            self.price *= 0.20
        return self.status, self.price

    def displayInfo(self):
        print "Item Name:", self.item
        print "Price: ${}".format(self.price)
        print "Weight:", self.weight, "lbs."
        print "Brand:", self.brand
        print "Cost: ${}".format(self.cost)
        print "Status:", self.status
        return self


class Store(object):

    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self, product):
        product_info = [
            product.item,
            product.price,
            product.weight,
            product.brand,
            product.cost,
            product.status
            ]
        self.products.append(product_info)
        print product.item, "added to inventory."
        print "---"

    def remove_product(self, product):
        self.products.remove([
            product.item,
            product.price,
            product.weight,
            product.brand,
            product.cost,
            product.status
        ])
        print product.item, "removed from inventory."
        print "---"

    def inventory(self):
        for product in self.products:
            print "Item Name:", product[0]
            print "Price: ${}".format(product[1])
            print "Weight:", product[2], "lbs."
            print "Brand:", product[3]
            print "Cost: ${}".format(product[4])
            print "Status:", product[5]
            print "---"

# Initializing objects
product1 = Product("Baseball", 5, 3, "Wilson", 1)
product2 = Product("Bat", 25, 6, "MLB", 10)
store1 = Store("Fairfax","Bill")

# Adding products
store1.add_product(product1)
store1.add_product(product2)

# Check inventory
store1.inventory()

# Removing product
store1.remove_product(product1)

# Check inventory
store1.inventory()