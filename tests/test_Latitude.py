import unittest

from pwrn.core import Latitude, LatitudeException


class TestLatitude(unittest.TestCase):
    def test_init_0(self):
        lat = Latitude(0.0)

        self.assertEqual(lat.degrees, 0.0)
        self.assertEqual(str(lat), "00 00.0 N")

    def test_init_52N(self):
        lat = Latitude(52.0)

        self.assertEqual(lat.degrees, 52.0)
        self.assertEqual(str(lat), "52 00.0 N")

    def test_init_52S(self):
        lat = Latitude(-52.0)

        self.assertEqual(lat.degrees, -52.0)
        self.assertEqual(str(lat), "52 00.0 S")

    def test_init_52_15N(self):
        lat = Latitude(52.25)

        self.assertEqual(lat.degrees, 52.25)
        self.assertEqual(str(lat), "52 15.0 N")

    def test_init_52_15S(self):
        lat = Latitude(-52.25)

        self.assertEqual(lat.degrees, -52.25)
        self.assertEqual(str(lat), "52 15.0 S")

    def test_init_90N(self):
        lat = Latitude(90.0)

        self.assertEqual(lat.degrees, 90.0)
        self.assertEqual(str(lat), "90 00.0 N")

    def test_init_91N(self):
        with self.assertRaises(LatitudeException):
            lat = Latitude(91.0)

    def test_init_90S(self):
        lat = Latitude(-90.0)

        self.assertEqual(lat.degrees, -90.0)
        self.assertEqual(str(lat), "90 00.0 S")

    def test_init_91S(self):
        with self.assertRaises(LatitudeException):
            lat = Latitude(-91.0)

    def test_sub00(self):
        lat0 = Latitude(0.0)
        lat1 = Latitude(52.0)
        delta = lat1 - lat0

        self.assertEqual(delta.degrees, 52.0)

    def test_sub01(self):
        lat0 = Latitude(90.0)
        lat1 = Latitude(-90.0)
        delta = lat1 - lat0

        self.assertEqual(delta.degrees, -180.0)

    def test_sub02(self):
        lat0 = Latitude(-90.0)
        lat1 = Latitude(90.0)
        delta = lat1 - lat0

        self.assertEqual(delta.degrees, 180.0)

    def test_sub03(self):
        lat0 = Latitude(52.0)
        lat1 = Latitude(52.50)
        delta = lat1 - lat0

        self.assertEqual(delta.degrees, 0.5)


if __name__ == "__main__":
    unittest.main()
