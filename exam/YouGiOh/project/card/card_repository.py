class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        try:
            search_card = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f"Card {search_card.name} already exists!")
        except IndexError:
            self.cards.append(card)
            self.count += 1

    def remove(self, card):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        else:
            search_card = [c for c in self.cards if c.name == card][0]
            self.cards.remove(search_card)
            self.count -= 1

    def find(self, name):
        search_card = [c for c in self.cards if c.name == name][0]
        return search_card

