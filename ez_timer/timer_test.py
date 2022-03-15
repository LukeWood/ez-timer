import time
import unittest

from ez_timer import ez_timer


class TestTimer(unittest.TestCase):
    def test_timer(self):
        with ez_timer() as timer:
            time.sleep(1.5)
        assert timer.result > 1
