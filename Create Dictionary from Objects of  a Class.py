class Mydictionary:

    def __init__(self):
        self.fruit="mango"
        self.vegetable="bean"
        self.flower="blackrose"
        self.animal="lion"
        self.bird="eagle"
        self.city="london"
        self.sea="pacific ocean"

    def Printit(self):
        print("the dictionary made from object is:")

dictionary=Mydictionary()

dictionary.Printit()

print(dictionary.__dict__)
