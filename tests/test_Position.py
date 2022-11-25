import unittest

from pwrn.core import Position


class TestPosition(unittest.TestCase):
    def test_hvh(self):
        hvh = Position(latitude=51.983333333333334, longitude=4.133333333333334)

        self.assertEqual(str(hvh), "51 59.0 N 004 08.0 E")

    def test_tinte(self):
        tinte = Position(longitude=4.136111111111112, latitude=51.886944444444445)
        self.assertEqual(str(tinte), "51 53.2 N 004 08.2 E")
