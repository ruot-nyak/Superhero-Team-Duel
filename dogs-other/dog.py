
#creating dog class
class Dog:
    def __init__ (self,name,breed):
        self.name = name
        self.breed = breed
        print ('Dog initialized!')
    #definging an action for the dogs to do
    def bark(self):
        print("Woof!")
    def sit(self):
        print('<> sits')
    def rollover(self):
        print('<> rolls over')

