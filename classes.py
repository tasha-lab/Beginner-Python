# classes- capitalize the class 

class Vehicle:
    #properties
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along ...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle("Tesla","Model 3") #my_car =  object
# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_Car = Vehicle('Cadillac','Escalade')
your_Car.get_make_model()
your_Car.moves()

##################################
########### Inheritance ##########
class Airplane(Vehicle):
    def __init__(self,make,model,faa_id):
        super().__init__(make,model) ##inherit them from the parent function
        self.faa_id =faa_id


    def moves(self):
        print("Flies along ...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along ....")

class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessna','SkyHawk','N-12345')
mack = Truck('Mack','Pinacle')
golfwagon = GolfCart('Yamaha','GC100')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

######polymorphism - same method different output
print('\n')
for v in (my_car,your_Car,cessna,mack,golfwagon):
    v.get_make_model()
    v.moves()