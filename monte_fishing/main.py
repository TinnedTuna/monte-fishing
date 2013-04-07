import arbiter

if __name__=='__main__':
    jobs = []
    for i in range(1):
        a = arbiter.Arbiter(5)
        a.start() # Non-blocking
        jobs.append(a)
    for j in jobs:
        j.join()
        

