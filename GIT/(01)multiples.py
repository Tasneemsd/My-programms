#write a programme which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200.
for i in range(2000,3201):
    if i%7==0:
        pass
    elif i%5!=0:
          print(i,end=" ")

#output 2001.....3198
