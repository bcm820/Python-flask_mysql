
class Animal(object):

    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        print "walk"
        return self

    def run(self):
        self.health -= 5
        print "run"
        return self

    def displayHealth(self):
        print self.name, self.health

animal = Animal("Animal:")
animal.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        print "pet"
        return self

dog = Dog("Dog:")
dog.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):

    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 500

    def fly(self):
        self.health -= 10
        print "fly"
        return self

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon named", self.name

drogon = Dragon("Drogon")
drogon.walk().run().fly().displayHealth()

# animal2 = Animal("animal2")
# animal2.pet().fly() - prints AttributeError: 'Animal' object has no attribute 'pet'
# dog.fly() - prints AttributeError: 'Dog' object has no attribute 'fly'
# drogon.pet() - prints AttributeError: 'Dragon' object has no attribute 'pet'