#!/usr/bin/python3

class Dog:
    def __init__(self, name, age):
        self.n = name # string - name of the dog
        self.a = age # int - age of the dog

    def __str__(self):
        return self.n

    def namechange(self, newname):
        self.n = newname

class Jackrussell(Dog):
     def __init__(self, name, age, isWirehair, isHunter):
         Dog.__init__(self, name, age)
         self.wh = isWirehair
         self.h = isHunter

def main():
    mutt1 = Dog("Spot", 3)
    print(mutt1)
    print("Your dog just got adopted and his name is now...")
    dogname = input("What is the new name of the dog? ")
    mutt1.namechange(dogname)

    print("The age of my dog is", mutt1.a)
    print("The name of my dog is", mutt1.n)
    print("Type:\n", type(mutt1))
    print("Dir:\n", dir(mutt1))


    mutt2 = Jackrussell("Eddie", 4, True, False)
    print(mutt2)
    mutt2.namechange("Frank")
    print(mutt2)
    print("Is dog trained to hunt? ", mutt2.h)
    

if __name__ == "__main__":
   main()
