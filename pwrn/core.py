import math


class LatitudeException(Exception):
    def __init__(self, deg: float):
        super().__init__(deg)


class LongitudeException(Exception):
    def __init__(self, deg: float):
        super().__init__(deg)


class Angle:
    def __init__(self, degrees: float = 0.0):
        self.degrees = degrees

    @property
    def degrees(self):
        """The latiude in degrees."""
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: float):
        self._set_degrees(degrees)

    def _set_degrees(self, degrees: float = 0):
        self.__degrees = degrees

    def __str__(self):
        return f"{self.degrees:.1f}"


class Latitude(Angle):
    def _set_degrees(self, degrees: float = 0):
        if degrees < -90.0 or degrees > 90.0:
            raise LatitudeException(degrees)

        super()._set_degrees(degrees)

    def __sub__(self, other):
        if not isinstance(other, Latitude):
            raise LatitudeException()

        delta = self.degrees - other.degrees

        if delta > 180.0:
            delta -= 180.0
        elif delta < -180.0:
            delta += 180.0

        return Angle(delta)

    def __str__(self):
        s = "N" if self.degrees >= 0.0 else "S"
        a = abs(self.degrees)
        d = math.floor(a)
        m = (a - d) * 60.0
        return f"{d:02} {m:04.1f} {s}"


class Longitude(Angle):
    def _set_degrees(self, degrees: float):
        if degrees < -180.0 or degrees > 180.0:
            raise LongitudeException(degrees)

        super()._set_degrees(degrees)

    def __sub__(self, other):
        if not isinstance(other, Longitude):
            raise LongitudeException()

        delta = self.degrees - other.degrees

        if delta > 360.0:
            delta -= 360.0
        elif delta < -360.0:
            delta += 360.0

        return Angle(delta)

    def __str__(self):
        s = "E" if self.degrees >= 0.0 else "W"
        a = abs(self.degrees)
        d = math.floor(a)
        m = (a - d) * 60.0
        return f"{d:03} {m:04.1f} {s}"


class Position:
    def __init__(self, latitude: float = 0.0, longitude: float = 0.0):
        self.latitude = Latitude(latitude)
        self.longitude = Longitude(longitude)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: Latitude):
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: Longitude):
        self._longitude = longitude

    def __str__(self):
        return f"{self.latitude} {self.longitude}"


if __name__ == "__main__":
    hvh = Position(latitude=51.983333333333334, longitude=4.133333333333334)
    print(f"Hoek van Holland: {hvh}")

    tinte = Position(longitude=4.136111111111112, latitude=51.886944444444445)
    print(f"Tinte: {tinte}")
