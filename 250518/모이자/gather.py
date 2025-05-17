n = int(input())
A = list(map(int, input().split()))

def cal(arr):
    sum = 0
    for i in range(len(arr)-1):
        sum += abs(arr[i]-arr[i+1])
    return sum

max_sum = -999999
for i in range(n):
    new_list = A
    new_list[i] *= 2
    diff_sum = cal(new_list)
    
    max_sum = max(max_sum, diff_sum)
    new_list[i] //= 2

print(max_sum)