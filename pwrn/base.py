from pwrn.error import LatitudeError

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
        s = 'N' if self.degrees >= 0.0 else 'S'
        a = abs(self.degrees)
        d = int(round(a))
        m = a * 60.0 - d * 60.0
        str = f'{d:02} {m:02.3} {s}'
        return str 


if __name__ == "__main__":
    print(Latitude(52.25))
    print(Latitude(52.33))
    print(Latitude(52.50))

    print(Latitude(91.0))
