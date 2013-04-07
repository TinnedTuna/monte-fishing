import arbiter

if __name__=='__main__':
    jobs = []
    for i in range(1):
        a = arbiter.Arbiter(5000)
        a.start() # Non-blocking
        jobs.append(a)
    for j in jobs:
        j.join()
        for outcome in j.outcome_log:
            print(outcome)
        

