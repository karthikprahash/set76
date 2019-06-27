# set76
i=int(input())
count=0
for x in range(1,i+1):
    if(i%x==0):
        count+=1
if (count==2):
    print('yes')
else:
    print('no')
