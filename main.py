import math
import random
import timeit


class Star:
    def __init__(self, mass, position, init_speed):
        self.m = mass
        self.r = position
        self.v = init_speed
        self.a = (0, 0, 0)

    def __str__(self):
        return f'Masa: {self.m}, position: {self.r}, init speed: {self.v}, acceleration: {self.a}'

    def distance(self, point):
        return math.sqrt((point[0] - self.r[0]) ** 2 + (point[1] - self.r[1]) ** 2 + (point[2] - self.r[2]) ** 2)

    def calculate_acceleration(self, stars):
        for star in stars:
            if star != self:
                ax = (star.m / math.fabs(self.distance(star.r)) ** 3) * (star.r[0] - self.r[0])
                ay = (star.m / math.fabs(self.distance(star.r)) ** 3) * (star.r[1] - self.r[1])
                az = (star.m / math.fabs(self.distance(star.r)) ** 3) * (star.r[2] - self.r[2])
                self.a = (ax, ay, az)


class Process:
    def __init__(self, n):
        self.n = n
        self.buffer = []
        self.init_buffer()
        self.accumulator = []
        self.collect(self.buffer)

    def init_buffer(self):
        for i in range(self.n):
            m = random.random() * 100
            r = (random.random() * 100, random.random() * 100, random.random() * 100)
            v = (random.random() * 100, random.random() * 100, random.random() * 100)
            new_star = Star(m, r, v)
            self.buffer.append(new_star)

    def collect(self, stars):
        self.buffer = stars
        for star in self.buffer:
            self.accumulator.append(star)

    def do_interactions(self):
        for star in self.accumulator:
            star.calculate_acceleration(self.accumulator)


if __name__ == '__main__':
    # init system
    n_stars = 8
    n_processes = 4
    processes = []
    for i in range(n_processes):
        process = Process(n_stars // n_processes)
        processes.append(process)

    start = timeit.default_timer()
    # communications
    for iteration in range(n_processes - 1):
        for i in range(n_processes):
            if i == 0:
                processes[n_processes - 1].collect(processes[i].buffer)
            else:
                processes[i - 1].collect(processes[i].buffer)

    # calculate accelerations
    for process in processes:
        process.do_interactions()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

    # print result
    for process in processes:
        for star in process.buffer:
            print(star)
