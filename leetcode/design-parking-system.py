# design-parking-system.py

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_max = big
        self.medium_max = medium
        self.small_max = small
        self.big_rest = 0
        self.medium_rest = 0
        self.small_rest = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_max > self.big_rest:
                self.big_rest += 1
                return True
        elif carType == 2:
            if self.medium_max > self.medium_rest:
                self.medium_rest += 1
                return True
        elif carType == 3:
            if self.small_max > self.small_rest:
                self.small_rest += 1
                return True
        return False


        # Your ParkingSystem object will be instantiated and called as such:
N = int(input())
big, medium, small = map(int, input().split())
obj = ParkingSystem(big, medium, small)
for i in range(N):
    carType = int(input())
    print(obj.addCar(carType))
