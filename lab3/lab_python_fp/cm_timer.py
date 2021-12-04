from contextlib import contextmanager
import time

class cm_timer_1:

    def __init__(self):
        pass

    def __enter__(self):
        self.time = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(time.time() - self.time)

@contextmanager
def cm_timer_2():
    time_ = time.time()
    yield 7
    print(time.time() - time_)


# with cm_timer_1():
#     time.sleep(1.2)
#
# with cm_timer_2():
#     time.sleep(2.5)
