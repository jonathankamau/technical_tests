def check_non_prime(n):
    for num in xrange(n,20000):
        for integer in xrange(2,num):
            if num % integer == 0 and num>n:
                yield num-1

def manipulate_generator(g,n):
    for num in check_non_prime(n):
        g.send(num)
        break
            
        
        

def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)

