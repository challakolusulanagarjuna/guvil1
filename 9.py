a=input()
n1=0
n2=0
get=[]
o_list=[int(x) for x in input().split()]
s=len(o_list)
while(n1==0):
    l=o_list[n1]
    o_list.remove(o_list[0])
    if((l in o_list)and(l not in get)):
        print(l,end=" ")
        get.insert(n2,l)
        n2+=1
    elif((o_list==get) and (l not in get) and (s==len(get))):
        print('unique')
    if(o_list==[]):
        break
