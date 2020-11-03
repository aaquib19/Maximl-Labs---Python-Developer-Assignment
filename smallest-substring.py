def check(alpha_count, mx):
    temp = 0
    for i in alpha_count:
        if i:
            temp+=1
    return temp == mx
 
 
def find_smallest_substring(s,n):
    seen = [0 for i in range(26)]
    for i in s:
        seen[ord(i)-ord('a')]=1
    mx = 0
    ans = 1
    for key in range(0,26): mx+=seen[key]
    low, high = 1, n
    while low <= high:
        flag = 0
        mid = (low+high)//2
        alpha_count =[0 for i in range(26)]
        for i in range(0,mid): alpha_count[ord(s[i]) - ord('a')]+=1
        for j in range(1,n-mid+1):
            if check(alpha_count,mx):
                flag = 1
                break
            alpha_count[ord(s[j-1]) - ord('a')]-=1
            alpha_count[ord(s[j+mid-1]) - ord('a')]+=1
        if check(alpha_count,mx):
            flag = 1
        if flag:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
 
s = input()
print(find_smallest_substring(s,len(s)))