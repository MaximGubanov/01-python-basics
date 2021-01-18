from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self._color = {'RAD': 7, 'YELLOW': 2, 'GREEN': 2}

    def running(self, count):
        count_time = 0
        for i in cycle(dict.keys(self._color)):
            if count_time == count:
                break
            else:
                print(i)
                sleep(dict.get(self._color, i))
                count_time += 1

traffic_light = TrafficLight()
traffic_light.running(count=6)

