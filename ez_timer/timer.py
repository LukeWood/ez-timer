import time

_TIME_DECIMAL = 6


class TimeMixin:
    @staticmethod
    def _ms(t):
        return round(t * 1000, _TIME_DECIMAL)

    @staticmethod
    def _h(t):
        return round(t / 3600, _TIME_DECIMAL)

    @staticmethod
    def _m(t):
        return round(t / 60, _TIME_DECIMAL)

    @staticmethod
    def _hms(t):
        return time.strftime("%H:%M:%S", time.gmtime(t))


class Timer(float, TimeMixin):
    def __init__(self, performance=True, verbose=False):
        self.start_time = None
        self.end_time = None
        self._elasped = 0.0
        self._performance = performance
        self.verbose = verbose

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

        if self.verbose:
            print("Time elasped: %fs" % self._elasped)

    def _check_runtime_error(self):
        if self.start_time is None or self.end_time is None:
            raise RuntimeError(
                "Attempting to use timer before timing context is exited."
            )

    @property
    def elasped(self):
        self._check_runtime_error()
        return self

    @property
    def hours(self):
        self._check_runtime_error()
        return self._h(self._elasped)

    @property
    def milliseconds(self):
        self._check_runtime_error()
        return self._ms(self._elasped)

    @property
    def hms(self):
        self._check_runtime_error()
        return self._hms(self._elasped)

    @property
    def minutes(self):
        self._check_runtime_error()
        return self._m(self._elasped)

    def __float__(self):
        self._check_runtime_error()
        return float(self._elasped)

    def __str__(self):
        return str(float(self))

    def __repr__(self):
        return str(float(self))
