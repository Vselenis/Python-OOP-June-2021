from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            check_hardware = [h for h in System._hardware if h.name == hardware_name][0]
            exs = ExpressSoftware(name, capacity_consumption, memory_consumption)
            check_hardware.install(exs)
            System._software.append(exs)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)


    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            check_hardware = [h for h in System._hardware if h.name == hardware_name][0]
            lgs = LightSoftware(name, capacity_consumption, memory_consumption)
            check_hardware.install(lgs)
            System._software.append(lgs)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            get_hardware = [h for h in System._hardware if h.name == hardware_name][0]
            get_software = [s for s in System._software if s.name == software_name][0]
            get_hardware.uninstall(get_software)
            System._software.remove(get_software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n"\
        f"Hardware Components: {len(System._hardware)}\n"\
        f"Software Components: {len(System._software)}\n"\
        f"Total Operational Memory: {sum([h.used_memory for h in System._hardware])} / {sum([h.memory for h in System._hardware])}\n"\
        f"Total Capacity Taken: {sum([h.used_capacity for h in System._hardware])} / {sum([h.capacity for h in System._hardware])}"

    @staticmethod
    def system_split():
        result = ''
        for h in System._hardware:
            result += f"Hardware Component - {h.name}\n"
            express_software_components = [s for s in h.software_components if s.__class__.__name__ == "ExpressSoftware"]
            result += f"Express Software Components: {len(express_software_components)}\n"
            light_software_components = [s for s in h.software_components if s.__class__.__name__ == "LightSoftware"]
            result += f"Light Software Components: {len(light_software_components)}\n"
            result += f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}\n"
            result += f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}\n"
            result += f"Type: {h.type}\n"
            names = ', '.join([j.name for j in h.software_components])
            result += f"Software Components: {names if names else None}"

        return result
