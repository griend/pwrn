import unittest

from pwrn.base import Latitude
from pwrn.error import LatitudeError


class TestLatitude(unittest.TestCase):
    def test_init_0(self):
        lat = Latitude(0.0)

        self.assertEqual(lat.get_degrees(), 0.0)
        self.assertEqual(str(lat), "00 00.0 N")

    def test_init_52N(self):
        lat = Latitude(52.0)

        self.assertEqual(lat.get_degrees(), 52.0)
        self.assertEqual(str(lat), "52 00.0 N")

    def test_init_52S(self):
        lat = Latitude(-52.0)

        self.assertEqual(lat.get_degrees(), -52.0)
        self.assertEqual(str(lat), "52 00.0 S")

    def test_init_52_15N(self):
        lat = Latitude(52.25)

        self.assertEqual(lat.get_degrees(), 52.25)
        self.assertEqual(str(lat), "52 15.0 N")

    def test_init_52_15S(self):
        lat = Latitude(-52.25)

        self.assertEqual(lat.get_degrees(), -52.25)
        self.assertEqual(str(lat), "52 15.0 S")

    def test_init_90N(self):
        lat = Latitude(90.0)

        self.assertEqual(lat.get_degrees(), 90.0)
        self.assertEqual(str(lat), "90 00.0 N")

    def test_init_91N(self):
        with self.assertRaises(LatitudeError):
            lat = Latitude(91.0)

    def test_init_90S(self):
        lat = Latitude(-90.0)

        self.assertEqual(lat.get_degrees(), -90.0)
        self.assertEqual(str(lat), "90 00.0 S")

    def test_init_91S(self):
        with self.assertRaises(LatitudeError):
            lat = Latitude(-91.0)


if __name__ == "__main__":
    unittest.main()
