class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = int(year)

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vid == other.vid
        return False

    def is_new(self, n):

        return (2026 - self.year) <= n + 1

class Car(Vehicle):
    def __init__(self, vid, model, year, fuel, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel
        self.doors = doors

    def __str__(self):

        return f"[Car]        VID: {self.vid} | {self.model:<15} ({self.year}) | Fuel: {self.fuel_type:<8} | {self.doors} Doors"

class Truck(Vehicle):
    def __init__(self, vid, model, year, load, axles):
        super().__init__(vid, model, year)
        self.max_load = load
        self.axles = axles

    def __str__(self):
        return f"[Truck]      VID: {self.vid} | {self.model:<15} ({self.year}) | Load: {self.max_load}kg  | {self.axles} Axles"

class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, cc, m_type):
        super().__init__(vid, model, year)
        self.engine_cc = cc
        self.type = m_type

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model:<15} ({self.year}) | Eng: {self.engine_cc}cc      | Type: {self.type}"

def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w') as f:
        for v in vehicles:
            if isinstance(v, Car):
                f.write(f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}\n")
            elif isinstance(v, Truck):
                f.write(f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}\n")
            elif isinstance(v, Motorcycle):
                f.write(f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.type}\n")

def load_fleet_from_file(filename):
    print(f"Loading fleet data from '{filename}'...")
    vehicles = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                p = [i.strip() for i in line.split(',')]
                if p[0] == "Car": vehicles.append(Car(p[1], p[2], p[3], p[4], p[5]))
                elif p[0] == "Truck": vehicles.append(Truck(p[1], p[2], p[3], p[4], p[5]))
                elif p[0] == "Motorcycle": vehicles.append(Motorcycle(p[1], p[2], p[3], p[4], p[5]))
    except FileNotFoundError:
        pass
    print(f"{len(vehicles)} vehicles loaded successfully.\n")
    return vehicles


fleet = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]

save_fleet_to_file(fleet, "fleet.txt")
loaded = load_fleet_from_file("fleet.txt")

print(" --- All Vehicles ---")
for v in loaded: print(v)

print("\n --- Recent Vehicles (Last 4 Years) ---")
for v in loaded:
    if v.is_new(4): print(v)

print("\n --- Electric Cars Only ---")
for v in loaded:
    if isinstance(v, Car) and v.fuel_type == "Electric": print(v)