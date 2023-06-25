"""
CoordHandler calculates its new Lat/Long.

Updates itself when given meters traveled in North/South and meters traveles East/West directions.
Also, convertes between digital format and formated string. 
"""

import numpy as np


def globe_dist(lat, km=True):
    """Calculates the number of meters at equal one degree Latitudes and one degree Longitude."""
    radians = lat * np.pi / 180
    north_south = 111_132.92 \
                - 559.82 * np.cos( 2*radians ) \
                + 1.175 * np.cos( 4*radians ) \
                - 0.002_3 * np.cos( 6*radians )
    east_west = 111_412.84 * np.cos( radians ) \
                - 93.5 * np.cos( 3*radians ) \
                + 0.118 * np.cos( 5*radians)
    factor = 1
    if km is True:
        factor = 1000
    if km is False:
        factor = 1
    return north_south/factor, east_west/factor

def coord_parser(degree_minute_second_str: str):
    degrees, m_s = degree_minute_second_str.split("°")
    minutes, seconds_dirty = m_s.split("'")
    seconds = seconds_dirty[:-1]
    return int(sum([int(degrees) * 3_600, int(minutes) * 60, int(seconds)]))

def coored_encoder(_degree: int):
    degrees = int(_degree // 3_600)
    minutes = int(_degree % 3_600 // 60)
    seconds = int(_degree % 3_600 % 60)
    degree_minute_second_str = f"{ degrees }°{ minutes }'{seconds }\""
    return degree_minute_second_str


class CoordHandler:
    """Probably doesn't handle crossing prime meridian or equator."""
    def __init__(self, coord_str=None, **kwargs):
        if coord_str is not None:
            self.coord_str = coord_str
            self.from_coord_string()
        elif kwargs:
                self.is_north = kwargs["is_north"]
                self.is_west = kwargs["is_west"]

                self._lat = int(kwargs["lat"] * 3_600)
                self.lat = self._lat / 3_600

                self._lon = int(kwargs["lon"] * 3_600)
                self.lon = self._lon / 3_600

                self.coord_str = self.gen_coord_str()
        else:
            self.coord_str = None
            self.is_north = None
            self.is_west = None
            self.lat = None
            self._lat = None
            self.lon = None
            self._lon = None

    def from_coord_string(self):
        lat_d_m_s, north, lon_d_m_s, west = self.coord_str.split(" ")
        if north == "N":
            self.is_north = True
        else:
            self.is_north = False
        if west == "W":
             self.is_west = True
        else:
             self.is_west = False
        self._lat = coord_parser(lat_d_m_s)
        self.lat = self._lat / 3_600
        self._lon = coord_parser(lon_d_m_s)
        self.lon = self._lon / 3_600
    

    def gen_coord_str(self):
        if self.is_north is True:
            ns = "N"
        elif self.is_north is False:
            ns = "S"
        else:
            ns = "'missing data'"
        if self.is_west is True:
            ew = "W"
        elif self.is_west is False:
            ew = "E"
        else:
            ns = "'missing data'"
        return f"{ coored_encoder(self._lat) } { ns } { coored_encoder(self._lon)} { ew }"

    def update(self, lat_dist: int, lon_dist: int):
        north_south, east_west = globe_dist(self.lat, km=False)
        self._lat = self._lat + int((lat_dist / north_south) * 3600)
        self.lat = self._lat / 3600
        self._lon = self._lon + int((lon_dist / east_west) * 3600)
        self.lon = self._lon / 3_600
        self.coord_str = self.gen_coord_str()


    def __str__(self) -> str:
        return f"""
        { self.coord_str }
            Is North: { self.is_north }
            Is West: { self.is_west }
            Lat: { self.lat } - Fine: { self._lat }
            Lon: { self.lon } - Fine: { self._lon }
          """

