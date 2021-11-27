class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


    def get_monthly_consumptions(self):
        monthly_cost_for_room = sum([r.room_cost for r in self.rooms])
        expenses_for_month = sum([r.expenses for r in self.rooms])
        return f"Monthly consumption: {monthly_cost_for_room + expenses_for_month}$."

    def pay(self):
        pass

    def status(self):
        pass