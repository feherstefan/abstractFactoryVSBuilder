class House:
    def __init__(self):
        self.walls = ""
        self.windows = ""
        self.doors = ""
        self.roof = ""
        self.features = ""

    def __str__(self):
        return f"House: Walls - {self.walls}, Windows - {self.windows}, Doors - {self.doors}, Roof - {self.roof}, Features - {self.features}"

class Builder:
    def addWalls(self):
        pass
    def addWindows(self):
        pass
    def addDoors(self):
        pass
    def addRoof(self):
        pass
    def addFeatures(self):
        pass

class HouseBuilder(Builder):
    def __init__(self):
        self.house = House()

    def addWalls(self):
        self.house.walls = "Bricks"

    def addWindows(self):
        self.house.windows = "Glass"

    def addDoors(self):
        self.house.doors = "Wooden"

    def addRoof(self):
        self.house.roof = "Tiles"

    def addFeatures(self):
        self.house.features = "Swimming Pool"


class Director:
    def __init__(self, builder):
        self.builder = builder

    def setBuilder(self, builder):
        self.builder = builder

    def getHouse(self):
        self.builder.addWalls()
        self.builder.addWindows()
        self.builder.addDoors()
        self.builder.addRoof()
        self.builder.addFeatures()
        return self.builder.house


builder = HouseBuilder()
director = Director(builder)
house = director.getHouse()
print(house)

