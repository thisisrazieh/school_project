#ruler    razieh
def ruler1():
    n=" ";
    for i in range(1 ,10000000):
        n = n + str(i)  +n;
        yield n
        
pr= ruler1()

for i in pr:
    print(i);