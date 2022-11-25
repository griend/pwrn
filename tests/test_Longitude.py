import unittest

from pwrn.core import Longitude, LongitudeException


class TestLongitude(unittest.TestCase):
    def test_init_0(self):
        long = Longitude(0.0)

        self.assertEqual(long.degrees, 0.0)
        self.assertEqual(str(long), "000 00.0 E")

    def test_init_52E(self):
        long = Longitude(52.0)

        self.assertEqual(long.degrees, 52.0)
        self.assertEqual(str(long), "052 00.0 E")

    def test_init_52W(self):
        long = Longitude(-52.0)

        self.assertEqual(long.degrees, -52.0)
        self.assertEqual(str(long), "052 00.0 W")

    def test_init_52_15E(self):
        long = Longitude(52.25)

        self.assertEqual(long.degrees, 52.25)
        self.assertEqual(str(long), "052 15.0 E")

    def test_init_52_15W(self):
        long = Longitude(-52.25)

        self.assertEqual(long.degrees, -52.25)
        self.assertEqual(str(long), "052 15.0 W")

    def test_init_180E(self):
        long = Longitude(180.0)

        self.assertEqual(long.degrees, 180.0)
        self.assertEqual(str(long), "180 00.0 E")

    def test_init_181E(self):
        with self.assertRaises(LongitudeException):
            long = Longitude(181.0)

    def test_init_180W(self):
        long = Longitude(-180.0)

        self.assertEqual(long.degrees, -180.0)
        self.assertEqual(str(long), "180 00.0 W")

    def test_init_181W(self):
        with self.assertRaises(LongitudeException):
            long = Longitude(-181.0)

    def test_sub00(self):
        long0 = Longitude(0.0)
        long1 = Longitude(4.25)
        delta = long1 - long0

        self.assertEqual(delta.degrees, 4.25)

    def test_sub01(self):
        long0 = Longitude(180.0)
        long1 = Longitude(-180.0)
        delta = long1 - long0

        self.assertEqual(delta.degrees, -360.0)

    def test_sub02(self):
        long0 = Longitude(-180.0)
        long1 = Longitude(180.0)
        delta = long1 - long0

        self.assertEqual(delta.degrees, 360.0)

    def test_sub03(self):
        long0 = Longitude(4.0)
        long1 = Longitude(4.50)
        delta = long1 - long0

        self.assertEqual(delta.degrees, 0.5)


if __name__ == "__main__":
    unittest.main()
