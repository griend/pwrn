class LatitudeException(Exception):
    def __init__(self, deg: float):
        super().__init__(deg)


class LongitudeException(Exception):
    def __init__(self, deg: float):
        super().__init__(deg)


class Angle:
    def __init__(self, deg: float = 0.0):
        self.degrees = deg

    @property
    def degrees(self):
        """The latiude in degrees."""
        return self.__degrees

    @degrees.setter
    def degrees(self, deg: float):
        self._set_degrees(deg)

    def _set_degrees(self, deg: float = 0):
        self.__degrees = deg


class Latitude(Angle):
    def _set_degrees(self, deg: float = 0):
        if deg < -90.0 or deg > 90.0:
            raise LatitudeException(deg)

        super()._set_degrees(deg)

    def __str__(self):
        deg = self.degrees
        s = "N" if deg >= 0.0 else "S"
        a = abs(deg)
        d = int(round(a))
        m = a * 60.0 - d * 60.0
        min = f"{m:0.3}"
        min = f"0{min}" if len(min) <= 3 else min
        str = f"{d:02} {min} {s}"
        return str


class Longitude(Angle):
    def _set_degrees(self, deg: float):
        if deg < -180.0 or deg > 180.0:
            raise LongitudeException(deg)

        super()._set_degrees(deg)

    def __str__(self):
        deg = self.degrees
        s = "E" if deg >= 0.0 else "W"
        a = abs(deg)
        d = int(round(a))
        m = a * 60.0 - d * 60.0
        min = f"{m:0.3}"
        min = f"0{min}" if len(min) <= 3 else min
        str = f"{d:03} {min} {s}"
        return str


if __name__ == "__main__":
    a = Angle(45.0)

    print(f"degrees: {a.degrees}")

    lat0 = Latitude()

    print(f"degrees: {lat0.degrees}")

    long1 = Longitude(15.0)

    print(f"degrees: {long1.degrees}")
