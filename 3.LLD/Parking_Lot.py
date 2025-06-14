from abc import ABCMeta, abstractmethod
from enum import Enum


class VehicleSize(Enum):
    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2


class Vehicle(metaclass=ABCMeta):
    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size
        self.spots_taken = []

    def clear_spots(self):
        for spot in self.spots_taken:
            spot.remove_vehicle()
        self.spots_taken = []

    def take_spot(self, spot):
        self.spots_taken.append(spot)

    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass


class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.MOTORCYCLE, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return True


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.COMPACT, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return spot.spot_size in (VehicleSize.LARGE, VehicleSize.COMPACT)


class Bus(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.LARGE, license_plate, spot_size=5)

    def can_fit_in_spot(self, spot):
        return spot.spot_size == VehicleSize.LARGE


# Main class
class ParkingLot:
    def __init__(self, num_levels):
        self.levels = [Level(i, 30) for i in range(num_levels)]

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False


class Level:
    SPOTS_PER_ROW = 10

    def __init__(self, floor, total_spots):
        self.floor = floor
        self.spots = [
            ParkingSpot(
                self,
                row=i // Level.SPOTS_PER_ROW,
                spot_number=i,
                spot_size=self.get_spot_size(i),
            )
            for i in range(total_spots)
        ]
        self.available_spots = total_spots

    def get_spot_size(self, index):
        if index % 10 < 2:
            return VehicleSize.MOTORCYCLE
        elif index % 10 < 5:
            return VehicleSize.COMPACT
        else:
            return VehicleSize.LARGE

    def spot_freed(self):
        self.available_spots += 1

    def park_vehicle(self, vehicle):
        start_index = self._find_available_spot(vehicle)
        if start_index is None:
            return False
        for i in range(start_index, start_index + vehicle.spot_size):
            self.spots[i].park_vehicle(vehicle)
        return True

    def _find_available_spot(self, vehicle):
        consecutive = 0
        for i in range(len(self.spots)):
            if self.spots[i].can_fit_vehicle(vehicle):
                consecutive += 1
                if consecutive == vehicle.spot_size:
                    return i - vehicle.spot_size + 1
            else:
                consecutive = 0
        return None


class ParkingSpot:
    def __init__(self, level, row, spot_number, spot_size):
        self.level = level
        self.row = row
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        vehicle.take_spot(self)
        self.level.available_spots -= 1

    def remove_vehicle(self):
        if self.vehicle:
            self.vehicle = None
            self.level.spot_freed()


# Step 1: Create a parking lot with 2 levels
parking_lot = ParkingLot(num_levels=2)

# Step 2: Create some vehicles
bike1 = Motorcycle("BIKE-111")
car1 = Car("CAR-123")
bus1 = Bus("BUS-777")

# Step 3: Try parking each vehicle
print("Parking Motorcycle:", parking_lot.park_vehicle(bike1))  # Should be True
print("Parking Car:", parking_lot.park_vehicle(car1))  # Should be True
print(
    "Parking Bus:", parking_lot.park_vehicle(bus1)
)  # Should be True if 5 large spots are available in a row

# # Step 4 (optional): Show where each vehicle was parked
# print(
#     "Motorcycle spots:",
#     [
#         f"Level {spot.level.floor}, Spot {spot.spot_number}"
#         for spot in bike1.spots_taken
#     ],
# )
# print(
#     "Car spots:",
#     [f"Level {spot.level.floor}, Spot {spot.spot_number}" for spot in car1.spots_taken],
# )
# print(
#     "Bus spots:",
#     [f"Level {spot.level.floor}, Spot {spot.spot_number}" for spot in bus1.spots_taken],
# )


# Unpark car1
car1.clear_spots()
print("Unparked Car:", car1.license_plate)
