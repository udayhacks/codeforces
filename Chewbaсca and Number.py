k = int(input())
j = len(str(k))
ans = 0
g = 0

while k > 0 :
    if k < 10 and k == 9 :
        ans +=((10**g)*k)
        break
    f= k%10
    k = k//10  

    l = min(f,(9-f))
    ans += ((10**g)*l)
    g+=1 
    
print(ans)
        
    














    
    