''' PROGRAM TO CHECK NUMBER IS APMSTRONG NUMBER OR NOT '''
a=int(input())
sum=0
temp=a
while (temp>0):
   digit=temp%10
   sum+=digit**3
   temp//=10
if (a==sum):
   print("yes")
else:
   print("no")
