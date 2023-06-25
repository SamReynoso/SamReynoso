import unittest
import numpy as np
from cooredhandler import CoordHandler

class TestCodeConverter(unittest.TestCase):

    def test_convert_str(self):
        coord_str = "30°30'30\" N 0°0'1\" E"
        digital_data = {
            "is_north":True,
            "is_west":False,
            "lat": 30.508333333333333,
            "lon": 0.0002777777777777778
        }
        base_c = CoordHandler(**digital_data)
        c = CoordHandler(coord_str=coord_str)
        self.assertAlmostEqual(c._lat, 109830)
        self.assertAlmostEqual(c._lon, 1)
        self.assertAlmostEqual(c.is_north, True)
        self.assertAlmostEqual(c.is_west, False)
        self.assertEqual(c.coord_str, base_c.coord_str)
        self.assertEqual(c.is_north, base_c.is_north)
        self.assertEqual(c.is_west, base_c.is_west)
        self.assertEqual(c.lat, base_c.lat)
        self.assertEqual(c._lat, base_c._lat)
        self.assertEqual(c.lon, base_c.lon)
        self.assertEqual(c._lon, base_c._lon)

    def test_convert_data(self):
        coord_str ="34°1'22\" N 110°39'41\" W"
        digital_data = {
            "is_north":True,
            "is_west":True,
            "lat": 34.02305555555555,
            "lon": 110.6613888888889
        }
        base_c = CoordHandler(coord_str=coord_str)
        c = CoordHandler(**digital_data)
        self.assertEqual(c.coord_str, base_c.coord_str)
        self.assertEqual(c.is_north, base_c.is_north)
        self.assertEqual(c.is_west, base_c.is_west)
        self.assertEqual(c.lat, base_c.lat)
        self.assertEqual(c._lat, base_c._lat)
        self.assertEqual(c.lon, base_c.lon)
        self.assertEqual(c._lon, base_c._lon)

    def test_update(self):
        coord_str ="34°1'22\" N 110°39'41\" W"
        c = CoordHandler(coord_str=coord_str)
        print(c.lat, c.lon)

        c.update(110_000, 34_500)
        print(c.lat, c.lon)


if __name__ == "__main__":
    unittest.main()