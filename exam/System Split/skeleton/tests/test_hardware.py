from unittest import TestCase, main
from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(TestCase):
    def setUp(self):
        self.pf = Hardware("Test", "Heavy", 100, 200)

    def test_init(self):
        self.assertEqual("Test", self.pf.name)
        self.assertEqual("Heavy", self.pf.type)
        self.assertEqual(100, self.pf.capacity)
        self.assertEqual(200, self.pf.memory)
        self.assertEqual([], self.pf.software_components)

    def test_install_raise_exception(self):
        software = LightSoftware("Li", 105, 210)
        with self.assertRaises(Exception) as ex:
            self.pf.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_install_valid_software(self):
        software = LightSoftware("Li", 25, 350)
        self.pf.install(software)
        self.assertEqual(1, len(self.pf.software_components))

    def test_uninstall_invalid_software(self):
        software = LightSoftware("Liza", 45, 70)
        self.assertEqual(0, len(self.pf.software_components))
        self.pf.uninstall(software)
        self.assertEqual(0, len(self.pf.software_components))

    def test_uninstall_valid_software(self):
        software = LightSoftware("Liza", 45, 70)
        self.pf.install(software)
        self.assertEqual(1, len(self.pf.software_components))
        self.pf.uninstall(software)
        self.assertEqual(0, len(self.pf.software_components))





if __name__ == "__main__":
    main()