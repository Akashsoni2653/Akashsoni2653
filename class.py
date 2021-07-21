class student:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"let's have a convertation \'{self.name}\'")


akash = student(input("what is your name: "))
akash.talk()
shresth = student(input("what is your name: "))
shresth.talk()