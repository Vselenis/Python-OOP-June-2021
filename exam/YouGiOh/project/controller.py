from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository
from project.battle_field import BattleField

class Controller:
    def __init__(self):
        self.p_repository = PlayerRepository()
        self.c_repository = CardRepository()

    def add_player(self, type, username):
        if type == "Advanced":
            new_player = Advanced(username)
        else:
            new_player = Beginner(username)
        self.p_repository.add(new_player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        if type == "Trap":
            new_card = TrapCard(name)
        else:
            new_card = MagicCard(name)
        self.c_repository.add(new_card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = self.p_repository.find(username)
        card = self.c_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card} to user: {player}"

    def fight(self, attack_name, enemy_name):
        attacker = self.p_repository.find(attack_name)
        enemy = self.p_repository.find(enemy_name)
        BattleField().fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = 0
        for p in self.p_repository.players:
            result += f'Username: {p.username} - Health: {p.health} - Cards {self.p_repository.count}\n'
            for c in p.card_repository.cards:
                result += f'### Card: {c.name} - Damage: {c.damage_points}\n'
        return result