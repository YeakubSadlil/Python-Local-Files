
class Dog:
    def __init__(self,name):
        self.n = name
        print("Dog is created")
        print("Name is: ",self.n)
        
    def bark(self,x=1):
        print("Hello World")
        print(x)
    
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
        
d = Dog("Tommy")           # creating an object of class Dog, creating a new isinstance of class Dog and type Dog
d.bark()
print(type(Dog))
print(d.n)
d.set_age(10)
print(d.get_age())
print(d.age)

