import time
# print(time.time())

def wiele_liczb(max):
    t1 = time.time()
    for x in range (0, max):
        print (x)

    t2 = time.time()
    print('it takes %s seconds' % (t2-t1))  

wiele_liczb (1000)
