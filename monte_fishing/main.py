import arbiter

if __name__=='__main__':
    jobs = []
    for i in range(4):
        a = arbiter.Arbiter(500)
        a.start() # Non-blocking
        jobs.append(a)
    for j in jobs:
        j.join()
        

