class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0

    def __str__(self) -> str:
        return f"{self.minutes:02}:{self.seconds:02}"


class Clock(Stopwatch):
    def __init__(self, h: int, m: int, s: int):
        super().__init__()
        self.hours = h
        self.minutes = m
        self.seconds = s

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 00

    def set(self, h: int, m: int):
        self.hours = h
        self.minutes = m
        self.seconds = 0

    def __str__(self) -> str:
        return f"{self.hours:02}:{super().__str__()}"


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
