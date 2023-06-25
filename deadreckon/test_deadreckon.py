import unittest
from deadreckon import Rose

class TestRose(unittest.TestCase):
    
    def test_init(self):
        heading = 45
        r = Rose(heading)
        self.assertAlmostEqual(r._heading, heading)

    def test_set_heading(self):
        heading = 45
        r = Rose(heading)
        r.set_heading(55)
        self.assertEqual(r._heading, 55)
        r.set_heading(360)
        self.assertEqual(r._heading, 0)
        r.set_heading(400)
        self.assertEqual(r._heading, 40)
        r.set_heading(0)
        self.assertEqual(r._heading, 0)
        r.set_heading(-10)
        self.assertEqual(r._heading, 10)
        r.set_heading(-360)
        self.assertEqual(r._heading, 0)
        r.set_heading(-370)
        self.assertEqual(r._heading, 10)

    def test_turn_left(self):
        heading = 45
        r = Rose(heading)
        r.turn_left()
        self.assertEqual(r._heading, 30)
        r.turn_left()
        r.turn_left()
        self.assertEqual(r._heading, 0)
        r.turn_left()
        self.assertEqual(r._heading, 345)

    def test_turn_right(self):
        heading = 330
        r = Rose(heading)
        r.turn_right()
        self.assertEqual(r._heading, 345)
        r.turn_right()
        self.assertEqual(r._heading, 0)
        r.turn_right()
        self.assertEqual(r._heading, 15)

    def test__set_slope(self):
        heading = 0
        r = Rose(heading)
        slope = r.slope
        self.assertAlmostEqual(slope[0], 1)
        self.assertAlmostEqual(slope[1], 0)

        r.set_heading(360)
        slope = r.slope
        self.assertAlmostEqual(slope[0], 1)
        self.assertAlmostEqual(slope[1], 0)

        r.set_heading(45)
        slope = r.slope
        self.assertAlmostEqual(slope[0], 0.70710678)
        self.assertAlmostEqual(slope[1], 0.70710678)
        
        r.set_heading(90)
        slope = r.slope
        self.assertAlmostEqual(slope[0], 0)
        self.assertAlmostEqual(slope[1], 1)

        r.set_heading(135)
        slope = r.slope
        self.assertAlmostEqual(slope[0], -0.70710678)
        self.assertAlmostEqual(slope[1], 0.70710678)        
        
        r.set_heading(180)
        slope = r.slope
        self.assertAlmostEqual(slope[0], -1)
        self.assertAlmostEqual(slope[1], 0)

        r.set_heading(225)
        slope = r.slope
        self.assertAlmostEqual(slope[0], -0.70710678)
        self.assertAlmostEqual(slope[1], -0.70710678)

        r.set_heading(270)
        slope = r.slope
        self.assertAlmostEqual(slope[0], 0)
        self.assertAlmostEqual(slope[1], -1)      
        
        r.set_heading(315)
        slope = r.slope
        self.assertAlmostEqual(slope[0], 0.70710678)
        self.assertAlmostEqual(slope[1], -0.70710678)



if __name__ == "__main__":
    unittest.main()