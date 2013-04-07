import arbiter
import argparse

from multiprocessing import Lock

parser = argparse.ArgumentParser(description="Run various Go Fish! strategies against one another in a monte-carlo fashion.")
parser.add_argument('--trials', type=int, help="How many trials to run.", default=10)
parser.add_argument('--processes', type=int, help="How many processes to use.", default=1)
args = parser.parse_args()

if __name__=='__main__':
    jobs = []
    outcomes = {}
    print("Processes: "+str(args.processes))
    print("Trials: "+str(args.trials))
    print_lock = Lock()
    for i in range(args.processes):
        a = arbiter.Arbiter(args.trials, print_lock)
        a.start() # Non-blocking
        jobs.append(a)
    for j in jobs:
        j.join()

