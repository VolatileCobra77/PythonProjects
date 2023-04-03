import threading
ObjectsToBuy = []
objectsOwned = []
money = 200
global itteration
itteration = 0

def clear():
    print()


def mainLoop():
    global itteration
    itteration += 1
    print("\033c", end='')
    print("Item Shop")
    print(f"itteration {itteration}")
    print("you Own")
    if objectsOwned == []:
        print("    You Own Nothing")
    else:
        for object in objectsOwned:
            print(f"    {object.ammountOwned} {object.name}(s)")
    print("--------------")
    print("You Can Buy")
    for object in ObjectsToBuy:
        if object.special:
            print(f"    {object.name} for ${object.cost} at position {object.index} (SPECIAL!)")
        else:
            print(f"    {object.name} for ${object.cost} at position {object.index}")
    
            
            
def ask():
    time.cancel()
    time.start()
    print("what do you want to do?")
    whatToDo = input("")
    time.cancel()
    if whatToDo.upper() == "BUY":
        time.cancel()
        print("\033c", end='')
        print("What would you like to buy(please provide item index)?")
        time.start()
        buyIndex = input()
        time.cancel()
        for i in ObjectsToBuy:
            if i.index == buyIndex:
                money = i.buy(objectsOwned, money)
                print("Success!")
                mainLoop()

time = threading.Timer(1, mainLoop)
class objectToBuy():
    def __init__(self, cost, name, list, special = False):
        self.cost = cost
        self.name = name
        list.append(self)
        self.index = list.index(self)
        self.special = special
        self.ammountOwned = 0
    def buy(self, boughtList, money):
        if money >= self.cost:
            if self.special:
                ObjectsToBuy.remove(self.name)
            boughtList.append(self.name)
            self.index = boughtList.index(self.name)
            return money - self.cost
        else:
            return money
        

gun = objectToBuy(100, "gun", ObjectsToBuy)
ammo = objectToBuy(50, "ammo", ObjectsToBuy)
running = True



while running:
    mainLoop()
    ask()
    