print("enter number of terms in list")
ll=int(input())

l1=[]

for i in range(ll):
    print("enter the ",i,"th element:")
    l1.append(input())

print(l1)
l1.sort()    
#l1=[2,1,4,21,23,44,5]
#for x in range(len(l1)):
 #   for j in range(x):
  ##         temp =l1[x]
    #        l1[x]=l1[j]
     #       l1[j]=temp
    #print(l1[x])
print(l1)        
#this is redundant, use l1.sort next time
