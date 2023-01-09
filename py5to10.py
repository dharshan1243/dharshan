fresh=int(input("enter the number of fresh loves purchased"))
old=int(input("enter the number of old day loaves purshaced"))
print("regular price:rs.185.00")
fresh-amount=185.00*float(fresh)
old-amount=(185*0.4)*float(old)
total=fresh-amount+old-amount
print("amunt of new loaves:rs" ,fresh-amount)
print("amount of day old loaves:rs" ,old-amount)
print("total amount:rs" ,total)



class solution:
    def maxarea(self,a):
        maxarea=0
        l=0
        r= len(a)-1
        while l < r:
            base = r-l
            height=min(a[l],a[r])
            area = base * height
            maxarea=max(area,maxarea)
            if a[l] , a[r]:
                l += 1
            else:
                r -=1
        return maxarea
ob=solution()
print(ob.maxarea([1,5,4,3]))
print(ob.maxarea([3,1,2,4,5]))





def countstring(n, start):
    if n== 0:
        return 1
    count = 0
    for i in range(start,5):
        count +=countstring(n-1,i)
    return count
def countvowlesstring(n):
    return countstring(n,0)
n=1
print(countvowlesting(n))




def isnumeric(s):
    s =s.strip()
    try:
        s=float(s)
        return true
    except:
        return flase
    print(isnumeric("0.2"))
    print(isnumeric("xyz"))
    print(isnumeric("hello"))
    print(isnumeric("-2.5"))
    print(isnumeric("10"))



    time=int(input())
    entry=list(map(int,input().split()))
    exit=list(map(int,input().split()))
    present=0
    total_guests=0
    for i in range(time):
        present+= entry[i]-exit[i]
        if total_guest<present:
            total_guest = present
    print(total_guests= present,end=" ")





    def addfrequencytocharacter(s):
        frequency=[0]*26
        n=len(s)
        for i in range(n):
            frequency[ord(s[i])-ord('a')]+=1
        for in range(n):
            add=frquency[ord(s[i])-ord('a')]%26
            if (ord(s[i]) + add <=ord('z')):
                s[i]=chr(ord(s[i])+add)
            else:
                add=(ord(s[i])+add)-(ord('z'))
                s[i]=chr(ord('a')+add-1)
        print("".join(s))
if__name__=='__main__':
    str="ghee"
    addfrequrncytocharacter([i for i in str])

    

                        
                
