
class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if software.capacity_consumption <= self.available_consumption and software.memory_consumption <= self.available_memory:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")


    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_consumption(self):
        cap = self.capacity - sum([sc.capacity_consumption for sc in self.software_components])
        return cap

    @property
    def available_memory(self):
        mem = self.memory - sum([mc.memory_consumption for mc in self.software_components])
        return mem

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def used_memory(self):
        return sum([m.memory_consumption for m in self.software_components])
