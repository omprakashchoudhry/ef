N=int(input()) 
sum=0
num=N
while num<100000:
    dig=num%10
    sum+=dig**3
    num//=10
if(N==sum):
    print("yes")
else:
    print("no")
