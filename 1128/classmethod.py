'''
class Converter :
    conversion_rate = 1.60934

    @classmethod
    def miles_to_kilometer(cls, mile) :
        return mile * cls.conversion_rate
    
print(Converter.miles_to_kilometer(7))
'''
'''
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year) :
        age = 2024 - birth_year
        return cls(name, age)

p1 = Person.from_birth_year("정태영", 1992)
print(p1.name, p1.age)
'''
'''
class Counter :
    count = 0

    @classmethod
    def increment(cls) :
        cls.count +=1

    @classmethod
    def get_count(cls) :
        return cls.count
    
Counter.increment()
print(Counter.get_count())
'''
'''
class Animal :
    species = "동물"

    @classmethod
    def get_species(cls) :
        return cls.species
    
class Dog(Animal) :
    species = "진돗개"

print(Animal.get_species())
print(Dog.get_species())
'''
class MathUtils :
    @staticmethod
    def add(a,b) :
        return a+b
    
    @staticmethod
    def minus(a, b) :
        return a-b

print(MathUtils.add(2,3))
print(MathUtils.minus(3,2))