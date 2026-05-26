# ABSTRACTION : 

# what is meant by abstraction in OOP ?
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.

# ADVANTAGES OF ABSTRACTION:
# hides complexity. 
# low risk. 
# clean architecture.  
# follows open and closed principle. 

#SIMPLE CODE:
class car:
    def start_engine(self):
        print("engine_started")
    def accelerate(self):
        print("car accelerated")
    def brake(self):
        print("car stopped")

car = car()
car.start_engine()
car.accelerate()
car.brake()

# the simple code which makes us understand tht how car has been started and how the car has been accelerated and how car stopped.
# it hides the inner working of car how it starts , accelerates and brakes.
# it shows only necessary working of a car for user. it is known as abstraction  in OOP.

