
class Bike(object):
    
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price
        print "Top speed:", self.max_speed
        print "Ridden", self.miles, "miles"
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self

Specialized = Bike("$2,500", "40mph")
Trek = Bike("$1,000", "30mph")
Huffy = Bike("$300", "15mph")

Specialized.ride().ride().ride().reverse().displayInfo()
Trek.ride().ride().reverse().reverse().displayInfo()
Huffy.reverse().reverse().reverse().displayInfo()