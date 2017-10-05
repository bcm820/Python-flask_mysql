
class Product(object):
    
    def __init__(self, price, item, weight, brand, cost):
        self.price = price
        self.item = item
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
        print "Price: ${}".format(self.price)
        print "Item Name:", self.item
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self
