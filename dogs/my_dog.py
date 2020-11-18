#importing code from dog.py file
import dog

my_dog = dog.Dog("Rex", "SuperDog")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()

Buddy = dog.Dog("Buddy", "TinyDog")
print(Buddy.name)
print(Buddy.breed)
Buddy.rollover()

Annie = dog.Dog("Annie", "SadDog")
print(Annie.name)
print(Annie.breed)
Annie.sit()