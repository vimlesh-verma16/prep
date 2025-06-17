from enum import Enum


class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3


class SpotType(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


class Vehicle:
    def __init__(self, license_plate: str):
        self.license_plate = license_plate

    def get_type(self) -> VehicleType:
        raise NotImplementedError()


class Motorcycle(Vehicle):
    def get_type(self):
        return VehicleType.MOTORCYCLE


class Car(Vehicle):
    def get_type(self):
        return VehicleType.CAR


class Truck(Vehicle):
    def get_type(self):
        return VehicleType.TRUCK


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.occupied = False
        self.vehicle = None

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        vt = vehicle.get_type()
        if vt == VehicleType.MOTORCYCLE:
            return True
        elif vt == VehicleType.CAR:
            return self.spot_type in {SpotType.COMPACT, SpotType.LARGE}
        elif vt == VehicleType.TRUCK:
            return self.spot_type == SpotType.LARGE
        return False

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if not self.occupied and self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            self.occupied = True
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None
        self.occupied = False


class Level:
    def __init__(self, level_num: int, spots: list[ParkingSpot]):
        self.level_num = level_num
        self.spots = spots

    def park_vehicle(self, vehicle: Vehicle) -> ParkingSpot:
        for spot in self.spots:
            if spot.park_vehicle(vehicle):
                return spot
        return None

    def free_spot(self, spot_id: str):
        for spot in self.spots:
            if spot.spot_id == spot_id:
                spot.remove_vehicle()
                break

    def get_available_spots(self):
        return [spot for spot in self.spots if not spot.occupied]


import uuid
from datetime import datetime


class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()


class ParkingLot:
    def __init__(self, levels: list[Level]):
        self.levels = levels
        self.active_tickets = {}

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        for level in self.levels:  # levels is a list of object of levels
            spot = level.park_vehicle(
                vehicle
            )  # this will be calling level park_vechicle press F!2 to check
            if spot:
                ticket = Ticket(vehicle, spot)  # Created a ticket here with id
                self.active_tickets[ticket.ticket_id] = (ticket, level)
                print(f"Vehicle parked at Level {level.level_num}, Spot {spot.spot_id}")
                return ticket
        print("No available spot for this vehicle.")
        return None

    def leave(self, ticket_id: str):
        if ticket_id not in self.active_tickets:
            print("Invalid Ticket")
            return
        ticket, level = self.active_tickets.pop(ticket_id)
        level.free_spot(ticket.spot.spot_id)
        print(
            f"Vehicle with plate {ticket.vehicle.license_plate} left spot {ticket.spot.spot_id}."
        )

    def get_availability(self):
        for level in self.levels:
            print(
                f"Level {level.level_num} has {len(level.get_available_spots())} free spots."
            )


# ---------------------------------------------------------------------------------------------------


# Create a parking lot with 2 levels, each with 5 spots
def create_sample_parking_lot():
    levels = []
    for level_num in range(2):
        spots = []
        for i in range(2):
            spots.append(
                ParkingSpot(f"L{level_num}-M{i}", SpotType.MOTORCYCLE)
            )  # Spot_id with spot_type created
        for i in range(2):
            spots.append(ParkingSpot(f"L{level_num}-C{i}", SpotType.COMPACT))
        for i in range(1):
            spots.append(ParkingSpot(f"L{level_num}-L{i}", SpotType.LARGE))
        level = Level(
            level_num, spots
        )  # All Level have been initialized  with level and spots  2 level wit 5 spots each
        levels.append(level)  # Created a level and added to levels
    return ParkingLot(levels)  # Create parking lot with leve;s


# Test Code
lot = create_sample_parking_lot()  # Created a parking lot with 2 levels 5 spots each
v1 = Car("DL-123")
v2 = Motorcycle("MH-456")
v3 = Truck("UP-789")

t1 = lot.park_vehicle(v1)
t2 = lot.park_vehicle(v2)
t3 = lot.park_vehicle(v3)

lot.get_availability()

lot.leave(t2.ticket_id)
lot.get_availability()
