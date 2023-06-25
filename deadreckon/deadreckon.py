"""
Deadreckon is a cool name for a module, so this module deadreckons.

Deadreckon could take geographic coordinate in string form or as kwargs but it doesn't.
It could track a csv file on the local file system and update another file system with
the calculated coordinates, but it doesnt do that either. Everythong is hard-coded, and 
if you create an instance it will make and track random moves from the fixed position and display
the path traveled.

Accounts for curviture of the earth.
Does NOT account for drift due to sea current or wind, or magnetic/true north offset.
Only works when in Northern AND Western hemispheres. 
"""


import numpy as np
import random
from cooredhandler import CoordHandler

from matplotlib import pyplot as plt

class Rose:
    def __init__(self, heading: int):
        self._heading = heading % 360
        self._set_slope()

    def set_heading(self, heading):
        if heading < 0:
            heading = 360 - (heading % 360)
        self._heading = heading % 360
        self._set_slope()

    def turn_left(self, abs=None):
        self._heading = self._heading - 15
        if self._heading < 0:
            self._heading = 360 + self._heading
        self._set_slope()

    def turn_right(self):
        self._heading = (self._heading + 15) % 360
        self._set_slope()

    def _set_slope(self):
        if self._heading == 0:
            self.slope = 1, 0
            return
        radians = (360 - self._heading + 90) % 360 * np.pi / 180 # Flip and rotate compass then get radians.
        self.slope = np.sin(radians), np.cos(radians) # Opposite, and Adjacent. Respectively.



class Travel:
    def __init__(self, datum, heading=45):
        self.datum = datum
        self.rose = Rose(heading)
        self.speed: int = 0
        self.coord = CoordHandler(coord_str=self.datum)
    
    def set_speed(self, speed: int):
        self.speed = speed

    def get_dist(self, time):
        lat_dist = self.rose.slope[0] * self.speed * time
        lon_dist = self.rose.slope[1] * self.speed * time
        return self.speed * time, lat_dist, lon_dist
    
    def update_pos(self, time):
        _, lat_dist, lon_dist = self.get_dist(time)
        self.coord.update(lat_dist, lon_dist)

class DeadReckon:

    datum = "41°43'57\" N 49°56'49\" W"
    travel = Travel(datum, heading=0)

    lats = []
    lons = []
    lats.append(travel.coord.lat)
    lons.append(travel.coord.lon)

    plt.ion()
    clock = 0
    for _ in range(200):
        travel.set_speed(random.randint(3, 7))
        time = random.randint(120, 600)
        travel.update_pos(time)
        lats.append(travel.coord.lat)
        lons.append(travel.coord.lon)
        turn = random.choice([travel.rose.turn_right, travel.rose.turn_left])
        turn()

        clock += time
        plt.plot(lons, lats)
        plt.text(0,
            0.9,
            f"""
            { travel.coord.coord_str }
            lat: { np.round(travel.coord.lat, 2) } lon: { np.round(travel.coord.lon, 2 ) }
            speed: { travel.speed } m/s time.:{ clock // 3600 } h.
            """,
            transform=plt.gca().transAxes)
        plt.pause(0.1)
        plt.cla()
    plt.show(block=True)

DeadReckon()
