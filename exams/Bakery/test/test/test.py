from unittest import TestCase, main
from project.pet_shop import PetShop



class TestPetShop(TestCase):
    def setUp(self):
        self.pf = PetShop("Test")

    def test_init(self):
        self.assertEqual("Test", self.pf.name)
        self.assertEqual({}, self.pf.food)
        self.assertEqual([], self.pf.pets)


    def test_add_food_invalid_quantity(self):
        name = "Bone"
        quantity = -1
        with self.assertRaises(ValueError) as ex:
            self.pf.add_food(name, quantity)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))


    def test_add_food_not_in_dict(self):
        name = "Bone"
        quantity = 1
        self.assertEqual(0, len(self.pf.food))
        self.pf.add_food(name, quantity)
        self.assertEqual(1, len(self.pf.food))

    def test_add_food_key_value_in_dict(self):
        name = "Bone"
        quantity = 1
        self.assertEqual(0, len(self.pf.food))
        self.pf.add_food(name, quantity)
        self.assertEqual(1, len(self.pf.food))
        self.pf.add_food(name, quantity)
        self.assertEqual(1, len(self.pf.food))
        self.assertEqual(2, self.pf.food["Bone"])


    def test_add_food_key_value_in_dic_return(self):
        name = "Bone"
        quantity = 1
        self.assertEqual(0, len(self.pf.food))
        self.pf.add_food(name, quantity)
        self.assertEqual(1, len(self.pf.food))
        self.assertEqual("Successfully added 1.00 grams of Bone.", self.pf.add_food(name, quantity))

    def test_add_pet_new(self):
        name = "Dogy"
        self.assertEqual(0, len(self.pf.pets))
        self.pf.add_pet(name)
        self.assertEqual(1, len(self.pf.pets))

    def test_add_pet_with_same_name(self):
        name = "Dogy"
        self.assertEqual(0, len(self.pf.pets))
        self.pf.add_pet(name)
        self.assertEqual(1, len(self.pf.pets))
        with self.assertRaises(Exception) as ex:
            self.pf.add_pet(name)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_no_pets_in_list(self):
        food_name = "Corn"
        pet_name = "Dogys"
        with self.assertRaises(Exception) as ex:
            self.pf.feed_pet(food_name, pet_name)
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_no_food_in_dict(self):
        self.pf.food = {"Corn": 5}
        self.pf.pets = ["Dogy"]
        pet_name = "Dogy"
        new_food = "Meat"
        self.assertEqual(f'You do not have {new_food}', self.pf.feed_pet(new_food, pet_name))

    def test_feed_pet_food_below_100(self):
        self.pf.food = {"Corn": 5}
        self.pf.pets = ["Dogy"]
        pet_name = "Dogy"
        food_name = "Corn"
        self.assertEqual("Adding food...", self.pf.feed_pet(food_name, pet_name))

    def test_feed_pet_food_above_100(self):
        self.pf.food = {"Corn": 1005}
        self.pf.pets = ["Dogy"]
        pet_name = "Dogy"
        food_name = "Corn"
        self.assertEqual(f"{pet_name} was successfully fed", self.pf.feed_pet(food_name, pet_name))
        self.assertEqual({"Corn": 905}, self.pf.food)

    def test_feed_pet_food_above_10_sd(self):
        self.pf.food = {"Corn": 1005}
        self.pf.pets = ["Dogy"]
        pet_name = "Dogy"
        food_name = "Corn"
        self.assertEqual(f"{pet_name} was successfully fed", self.pf.feed_pet(food_name, pet_name))
        self.assertEqual({"Corn": 905}, self.pf.food)
        self.assertEqual(len()



    def test_repr_(self):
        food_name = "Corn"
        pet_name = "Dogy"
        self.pf.food[food_name] = 1
        self.pf.pets.append(pet_name)
        self.assertEqual(f'Shop Test:\n' \
               f'Pets: Dogy', repr(self.pf))


if __name__ == "__main__":
    main()
