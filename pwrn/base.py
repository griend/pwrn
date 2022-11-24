from pwrn.error import LatitudeError, LongitudeError


class Angle:
    def __init__(self):
        self._deg = 0.0

    def set_degrees(self, deg: float):
        self.deg = deg

    def get_degrees(self):
        return self.deg


class Latitude(Angle):
    def __init__(self, deg: float):
        self.set_degrees(deg)

    def set_degrees(self, deg: float):
        if deg < -90.0 or deg > 90.0:
            raise LatitudeError()

        super().set_degrees(deg)

    def __str__(self):
        deg = self.get_degrees()
        s = "N" if deg >= 0.0 else "S"
        a = abs(deg)
        d = int(round(a))
        m = a * 60.0 - d * 60.0
        min = f"{m:0.3}"
        min = f"0{min}" if len(min) <= 3 else min
        str = f"{d:02} {min} {s}"
        return str


class Longitude(Angle):
    def __init__(self, deg: float):
        self.set_degrees(deg)

    def set_degrees(self, deg: float):
        if deg < -180.0 or deg > 180.0:
            raise LongitudeError()

        super().set_degrees(deg)

    def __str__(self):
        deg = self.get_degrees()
        s = "E" if deg >= 0.0 else "W"
        a = abs(deg)
        d = int(round(a))
        m = a * 60.0 - d * 60.0
        min = f"{m:0.3}"
        min = f"0{min}" if len(min) <= 3 else min
        str = f"{d:03} {min} {s}"
        return str
