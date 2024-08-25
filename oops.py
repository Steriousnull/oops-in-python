#car properties

no_of_wheels = 4
mileage = 20.9
no_of_airbags = 5

#car behaviour
def moveForward():
    print("car is moving")
 
def moveBackward():
    print("car is moving backward")


class Car:
    #variables
    no_of_wheels = 4
    mileage = 5.0
    no_of_airbags = 0

    #function
    def moveForward(self):
        print("Car is moving")

    def moveBackward(self):
        print("Car is moving backward")

car1 = Car()  #instance of a class / object is created / copy of class properties 
print(car1.no_of_wheels)       
print("mileage of car1 : ",car1.mileage)



car2=Car()
print("mileage of car2 : ",car2.mileage)
#print(car2.no_of_wheels)
car2.mileage = 34.0
#print(car2.no_of_airbags)
print("mileage of car1 : ",car1.mileage)
print("mileage of car2 : ",car2.mileage)
car3 = Car()
car3.moveForward()
car2.moveBackward()