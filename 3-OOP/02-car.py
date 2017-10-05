
class Car(object):
    
    def __init__(self, model, year, top_speed, hp, mileage, price):
        self.make = "Subaru"
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self.hp = hp
        self.mileage = mileage
        self.price = price
        if price > 10000:
            self.tax = 15
        else:
            self.tax = 12
        self.display_all()

    def display_all(self):
        print "Make:", self.make
        print "Model:", self.model
        print "Year", self.year 
        print "Top Speed: {}mph".format(self.top_speed)
        print "Horsepower: {}hp".format(self.hp)
        print "Mileage:", self.mileage + "mpg"
        print "MSRP: From ${:,}".format(self.price)
        print "Tax: {}%".format(self.tax)
        print "-----"

Impreza = Car("Impreza", 2017, 122, 148, "25/34", 19215)
Legacy = Car("Legacy", 2017, 130, 175, "26/36", 21995)
Forester = Car("Forester", 2016, 122, 250, "23/28", 22595)
BRZ = Car("BRZ", 2017, 134, 205, "21/29", 25495)
WRX = Car("WRX", 2017, 144, 268, "21/28", 27695)
STI = Car("WRX STI", 2017, 159, 305, "17/22", 36955)
