c =float( input("please enter number:") );
EPSILON = 1e-15;
t = c;

while abs(t-c/t) > (EPSILON * t):
    t= (c/t+t) / 2.0
    
print(t);