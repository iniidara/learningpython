class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def __str__(self):
        return "animal: " + str(self.name) + ":" + str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.years = newage
    def set_name(self, newname=""):
        self.name = newname

class Cat(Animal):
    def speak(self):
        print("Meow!!")
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends.copy()
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I'm still zooming")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)


class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(5)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return(0, self, other)

r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
r4 = r1+r2
print(r1)
print(r2)
print(r4)