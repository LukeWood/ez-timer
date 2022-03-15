import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end_time = time.perf_counter()

    @property
    def result(self):
        if self.start_time is None or self.end_time is None:
            raise RuntimeError(
                "Attempting to use timer before timing context is exited."
            )
        return self.end_time - self.start_time
