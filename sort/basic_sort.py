# for Test IDLE
# ref: https://medium.com/@fiv3star/%EC%A0%95%EB%A0%AC%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-sorting-algorithm-%EC%A0%95%EB%A6%AC-8ca307269dc7
from random import randint
import time

def start():
    while True:
        size = 10
        array_ = [randint(1,1000000) for x in range(size) ]
        if len(set(array_)) == size:
            print(f"정렬 전 : {array_}")
            bubbleSort(array_)
            selectionSort(array_)
            insertionSort(array_)
            print(f"Merge Sort : {mergeSort(array_)}")
            break
        else:
            print("중복체크")
            start()
            break

def timeChecker(func):
    """
    데코레이터 함수 별 소요시간 체크
    """
    def wrapper(_):
        start = time.time()
        func(_)
        during = time.time() - start
        print(f"소요시간 : {during}")
    return wrapper

@timeChecker
def bubbleSort(alist):
    """
    # 버블정렬(Bubble Sort)
     - 시간복잡도 O(n^2)
     - 공간복잡도 O(n) : 하나의 배열만 사용하기 때문
    """
    for loof_count in range(len(alist)-1, 0, -1):
        for idx in range(loof_count):
            if alist[idx] > alist[idx +1]:
                tmp = alist[idx+1]
                alist[idx+1] = alist[idx]
                alist[idx] = tmp
    print(f"Bubble Sort: {alist} ")

@timeChecker
def selectionSort(alist):
    """
    # 선택정렬(Selection Sort)
     - 한번 순회를 하면서 가장 작은 수를 찾아서 배열의 마지막 위치와 교환(제일작은걸 가장 앞으로)
     - 시간복잡도 O(n^2)
    """
    for offset in range(0, len(alist)-1):
        offset_min = offset
        for num in range(offset+1, len(alist)):
            # 최소값(offset_min)보다 새로 탐색하는 값(num)이 작으면 최소값 가리키는 포인터 갱신
            if alist[offset_min] > alist[num]:
                offset_min = num
        tmp = alist[offset_min]
        alist[offset_min] = alist[offset]
        alist[offset] = tmp
    print(f"Selection Sort: {alist}")


@timeChecker
def insertionSort(alist):
    """
    # 삽입정렬(Insertion Sort)
     - 1부터 n까지 Index를 설정하여 현재위치의 값을 아래쪽으로 순회하며 알맞은 위치에 넣어주는 정렬 알고리즘
     - 시간복잡도 
     - O(n) : 이미 정렬이 되어있는경우
     - O(n^2) : Big-O
    """
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentValue:
            alist[position] = alist[position-1]
            position = position - 1
    
    alist[position] = currentValue
    print(f"Insertion Sort: {alist}")

def mergeSort(alist):
    """
    # 병합정렬(Merge Sort)
     - 리스트를 반으로 쪼개나가며 좌측과 우측 리스트를 계속하여 분할
     - 각 리스트내에서 정렬 후 병합 -> 정렬 후 병합을 계속함
     - 시간복잡도 : O(nlogn)
    """
    if len(alist) <= 1:
        return alist
    
    mid = len(alist) // 2

    leftlist = alist[:mid]
    rightlist = alist[mid:]

    L = mergeSort(leftlist)
    R = mergeSort(rightlist)

    i = j = 0
    result = []

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    
    result += L[i:]
    result += R[j:]
    
    print(f"Merge Sort 중간 과정: {result}")
    return result


def fastmerge(array1, array2):
    # https://www.seokdev.site/208
    # for Tim Sort
    merged_array = []
    while array1 or array2:
        print(merged_array)
        if not array1:
            merged_array.append(array2.pop())
        elif (not array2) or array1[-1] > array2[-1]:
            merged_array.append(array1.pop())
        else:
            merged_array.append(array2.pop())
    merged_array.reverse()
    return merged_array



def quickSort(x):
    """
    # 퀵정렬(Quick Sort)
     - real-world Data에서 빠르다고 알려져 있음
     - pivot을 선정하여 pivot을 기준으로 좌측과 우측으로 pivot보다 작은값은 왼쪽 / pivot보다 큰값은 오른쪽으로 재배치
     - 시간복잡도 : Worst- O(n^2) / Avg- O(nlogn)
    """
    if len(x) <= 1:
        return x
    pivot = x[len(x)//2]
    less = []
    more = []
    for a in x:
            if a < pivot:
                less.append(a)
            elif a > pivot:
                more.append(a)
            else:
                equal = [a]
    return quickSort(less) + equal + quickSort(more)

