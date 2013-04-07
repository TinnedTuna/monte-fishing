import sys

class SynchronisedPrinter(object):
    def __init__(self, print_lock):
        self.print_lock = print_lock

    def print_synchronised(self, string):
        self.print_lock.acquire()
        print(string)
        sys.stdout.flush()
        self.print_lock.release()

    def print_batch(self, strings):
        self.print_lock.acquire()
        for s in strings:
            print(s)
        sys.stdout.flush()
        self.print_lock.release()
