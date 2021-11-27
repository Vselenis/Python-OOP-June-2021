from unittest import TestCase
from project1.hero import Hero

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Sylenis", 100, 200, 300)
        self.enemy = Hero("Gosho", 100, 200, 300)
        self.strong_hero = Hero("Strong Harry", 1000, 200000, 3000)
    def test_init(self):
        hero = Hero("Sylenis", 80, 100, 150)
        self.assertEqual("Sylenis", hero.username)
        self.assertEqual(80, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(150, hero.damage)

    def test_cannot_fight_yourself(self):
        with self.assertRaises(Exception) as s:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(s.exception))

    def test_battle_with_no_health(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_with_enemy_with_no_health(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(e.exception))

    def test_battle_draw(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "Draw")

    def test_win_battle(self):
        result = self.strong_hero.battle(self.enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(170005, self.strong_hero.health)
        self.assertEqual(3005, self.strong_hero.damage)
        self.assertEqual(1001, self.strong_hero.level)
        self.assertEqual(-2999800, self.enemy.health)
        self.assertEqual(300, self.enemy.damage)
        self.assertEqual(100, self.enemy.level)

    def test_lose_battle(self):
        result = self.enemy.battle(self.strong_hero)
        self.assertEqual(result, "You lose")
        self.assertEqual(170005, self.strong_hero.health)
        self.assertEqual(3005, self.strong_hero.damage)
        self.assertEqual(1001, self.strong_hero.level)
        self.assertEqual(-2999800, self.enemy.health)
        self.assertEqual(300, self.enemy.damage)
        self.assertEqual(100, self.enemy.level)

    def test_str(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\n"
               f"Health: {self.hero.health}\n"
               f"Damage: {self.hero.damage}\n", str(self.hero))
