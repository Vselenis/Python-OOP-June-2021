from unittest import TestCase
from project1.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.v = Vehicle(80, 161)

    def test_init(self):
        fuel = 80
        hp = 161
        default_pc = 1.25

        vehicle = Vehicle(fuel, hp)


        self.assertEqual(vehicle.fuel, fuel)
        self.assertEqual(vehicle.capacity, fuel)
        self.assertEqual(vehicle.horse_power, hp)
        self.assertEqual(vehicle.fuel_consumption, default_pc)

    def test_drive(self):
        km = 20
        remaining_fuel = 55
        self.v.drive(km)
        self.assertEqual(self.v.fuel, remaining_fuel)

    def test_drive_exception_raise(self):
        km = 100
        with self.assertRaises(Exception) as e:
            self.v.drive(km)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel(self):
        self.v.fuel -= 20
        self.v.refuel(10)
        self.assertEqual(self.v.fuel, 70)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as e:
            self.v.refuel(5)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_str(self):
        hp = 161
        fuel = 80
        fc = 1.25
        self.assertEqual(f"The vehicle has {hp} horse power with {fuel} fuel left and {fc} fuel consumption", str(self.v))
