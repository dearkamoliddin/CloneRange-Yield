class CloneRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.stop = start
            self.start = -step
            self.step = step
        else:
            self.start = start - step
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.start < self.stop:
            self.start += self.step
            if self.start >= self.stop:
                raise StopIteration
            return self.start

        if self.step > 0 and self.start > self.stop:
            raise StopIteration

        if self.step < 0 and self.start < self.stop:
            self.start += self.step
            if self.start >= self.stop:
                raise StopIteration
            return self.start

        if self.step < 0 and self.start > self.stop:
            self.start += self.step
            if self.start <= self.stop:
                raise StopIteration
            return self.start


for i in CloneRange(20, 2, -2):
    print(i)
