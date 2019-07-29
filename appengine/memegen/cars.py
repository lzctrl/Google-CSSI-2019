from google.appengine.ext import ndb

class Car(ndb.Model):
    make = ndb.StringProperty(required=True)
    model = ndb.StringProperty(required=True)

    def printCarInfo(self):
        print(self.make + " " + self.model)

car1 = Car(make="Lexus", model="Lx 470")
car2 = Car(make="BMW", model="M5")

car1.printCarInfo()
car2.printCarInfo()
