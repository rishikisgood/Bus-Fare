class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        """Calculates the base fare for the vehicle."""
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        """
        Overrides the fare method to include a 10% maintenance charge for Bus.
        """
        base_fare = super().fare()  # Call the parent class's fare method
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare

# Example usage:
school_bus = Bus("School Volvo", 12, 50)
print(f"Total Bus fare for {school_bus.name} with capacity {school_bus.capacity} is: {school_bus.fare()}")

regular_vehicle = Vehicle("Sedan", 25, 4)
print(f"Total fare for {regular_vehicle.name} with capacity {regular_vehicle.capacity} is: {regular_vehicle.fare()}")
