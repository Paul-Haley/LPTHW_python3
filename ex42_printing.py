## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    # a __str__ method is called when the string representation of the object 
    # is called for. Doing `print("Hello, %s", rover)` would print the return 
    # from this method.
    def __str__(self):
        return "I am a animal!"

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    def __str__(self):
        return "%s is-a Dog which is a type of Animal." % self.name

## Cat is-a Aniaml
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name
    
    def __str__(self):
        return "%s is-a Cat which is a type of Animal." % self.name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def __str__(self):
        if self.pet is None:
            return "%s is-a Person and does not have a pet" % self.name
        else:
            return ("%s is-a Person and has-a pet:\n\t%s" 
                % (self.name, self.pet))

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has a name like a Person. `super` means to look at the 
        #super class (in this case, the super class is Person) and we are using
        #the __init__ method to assign the name.
        super(Employee, self).__init__(name)

        ## Employee has-a salary
        self.salary = salary
    
    def __str__(self):
        return ("%s is-a Employee with a salary of $%d. An Employee is-a " \
                "Person." % (self.name, self.salary))

## Fish is-a object
class Fish(object):
    
    def __str__(self):
        return "Fish is-a object."

## Salmon is-a Fish
class Salmon(Fish):
    
    def __str__(self):
        return "Salmon is-a Fish."

## Halibut is-a Fish
class Halibut(Fish):
    
    def __str__(self):
        return "Halibut is-a Fish."


## rover is-a Dog
rover = Dog("Rover")
print(rover)

## satan is-a Cat
satan = Cat("Satan")
print(satan)

## mary is-a Person
mary = Person("Mary")
print(mary)

## mary has-a pet (satan)
mary.pet = satan
print(mary)

## frank is-a Employee and frank has-a salary of 120000
frank = Employee("Frank", 120000)
print(frank)

## frank has-a pet (rover). Frank is Employee, therefore, Frank is Person.
frank.pet = rover

## flipper is-a Fish
flipper = Fish()
print("Flipper says '%s'" % flipper)

## crouse is-a Salmon
crouse = Salmon()
print("Crouse says '%s'" % crouse)

## harry is-a Halibut
harry = Halibut()
print("Harry say '%s'" % harry)
