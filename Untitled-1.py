n=100;
number1=0;number2=0;
for i in range(1,n+1):
    number1=number1+(1/i);
    number2=number2+(1/(i*i));

print(number1);
print(number2);