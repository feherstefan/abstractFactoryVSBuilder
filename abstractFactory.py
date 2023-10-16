class HouseFactory:
    def createWalls(self):
        pass

    def createWindows(self):
        pass

    def createDoors(self):
        pass

    def createRoof(self):
        pass

    def createFeatures(self):
        pass

class ModernHouseFactory(HouseFactory):
    def createWalls(self):
        return "Glass Walls"

    def createWindows(self):
        return "Large Windows"

    def createDoors(self):
        return "Sliding Doors"

    def createRoof(self):
        return "Flat Roof"

    def createFeatures(self):
        return "Swimming Pool"

class TraditionalHouseFactory(HouseFactory):
    def createWalls(self):
        return "Brick Walls"

    def createWindows(self):
        return "Wooden Windows"

    def createDoors(self):
        return "Wooden Doors"

    def createRoof(self):
        return "Tiled Roof"

    def createFeatures(self):
        return "Garden"

class House:
    def __init__(self, walls, windows, doors, roof, features):
        self.walls = walls
        self.windows = windows
        self.doors = doors
        self.roof = roof
        self.features = features

    def __str__(self):
        return f"House: Walls - {self.walls}, Windows - {self.windows}, Doors - {self.doors}, Roof - {self.roof}, Features - {self.features}"

class HouseDirector:
    def constructHouse(self, factory):
        walls = factory.createWalls()
        windows = factory.createWindows()
        doors = factory.createDoors()
        roof = factory.createRoof()
        features = factory.createFeatures()
        return House(walls, windows, doors, roof, features)

while True:
    user_choice = input("Enter 'modern' for a Modern House or 'traditional' for a Traditional House: ").strip().lower()

    if user_choice == "modern":
        factory = ModernHouseFactory()
        break
    elif user_choice == "traditional":
        factory = TraditionalHouseFactory()
        break
    else:
        print("Invalid choice. Please enter 'modern' or 'traditional'.")

director = HouseDirector()
house = director.constructHouse(factory)

print(f"{user_choice.capitalize()} House:")
print(house)
