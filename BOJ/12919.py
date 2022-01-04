# A/B2

# A로 시작해서 B로 끝나는 경우는 불가능하다.
s = input()
t = input()


def can(s, t):
    if s == t:
        return True
    if len(t) > 0:
        if t[-1] == 'A' and can(s, t[:-1]):  # 마지막 문자를 자른다.
            return True
        if t[0] == 'B' and can(s, t[:0:-1]):  # 뒤집고 마지막 문자를 제
            return True
    return False


print(1 if can(s, t) else 0)


def lower_bound(arr, left, right, key):
    mid = (left + right) // 2
    if arr[mid] == key:
        ans = mid
        right = mid - 1  # 하한을 찾기 위해
    elif arr[mid] > key:
        right = mid - 1
    else:
        left = mid + 1


def upper_bound(arr, left, right, key):
    mid = (left + right) // 2
    if arr[mid] == key:
        ans = mid + 1
        left = mid + 1
    elif arr[mid] > key:
        right = mid - 1
    else:
        left = mid + 1





def merge(a, start, end):
    b = [0] *(start-end+1)
    mid = (start + end) // 2
    i = start
    j = mid + 1
    k = 0
    while i <= mid and j <= end:
        if a[i] <= a[j]:
            b[k] = a[i]
            k += 1
            i += 1
        else:
            b[k] = a[j]
            k += 1
            j += 1
    while i<=mid:
        b[k] = a[i]
        k+=1
        i+=1
    while j<=end:
        b[k] = a[j]
        k+=1
        j+=1
    for i in range(start, end+1):
        a[i] = b[i-start]

def merge_sort(start, end):
    if start == end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
