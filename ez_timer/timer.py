import time

class Timer(float):
    def __init__(self, performance=True):
        self.start_time = None
        self.end_time = None
        self._elasped = 0.0
        self._performance = performance

    def __enter__(self):
        if self._performance:
            self.start_time = time.perf_counter()
        else:
            self.start_time = time.time()

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._performance:
            self.end_time = time.perf_counter()
        else:
            self.end_time = time.time()
        self._elasped = self.end_time - self.start_time

    @property
    def result(self):
        if self.start_time is None or self.end_time is None:
            raise RuntimeError(
                "Attempting to use timer before timing context is exited."
            )
        return self._elasped

    def __float__(self):
        return float(self._elasped)

    def __str__(self):
        return str(float(self))

    def __repr__(self):
        return str(float(self))
