import unittest

from pwrn.base import Latitude

class TestLatitude(unittest.TestCase):

    def test_create(self):
        lat = Latitude(0.0)

        self.assertEqual(lat.get_degrees(), 0.0)


if __name__ == '__main__':
    unittest.main()
