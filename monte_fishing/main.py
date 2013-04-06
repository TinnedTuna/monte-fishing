import arbiter

if __name__=='__main__':
    for i in range(4):
        a = arbiter.Arbiter(500)
        a.start() # Non-blocking
        

