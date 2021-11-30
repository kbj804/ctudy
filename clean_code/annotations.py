"""
데이터의 유효성을 검사하고 사전 값을 반환
함수인자로 어떤 값이 와야하는지 힌트를 주고자 함
> Annotations
"""


class Point:  # pylint: disable=R0903
    """Example to be used as return type of locate"""
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


def locate(latitude: float, longitude: float) -> Point:
    """Find an object in the map by its coordinates"""
    return Point(latitude, longitude)


class NewPoint:  # pylint: disable=R0903
    """Example to display its __annotations__ attribute."""
    lat: float
    long: float
