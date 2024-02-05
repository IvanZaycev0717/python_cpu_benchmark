def insert_sort(arr: int) -> None:
    """Алгоритм сортировки вставками."""
    N = len(arr)
    for top in range(1, N):
        k = top
        while k > 0 and arr[k - 1] > arr[k]:
            arr[k], arr[k - 1] = arr[k-1], arr[k]
            k -= 1


def selection_sort(arr: list) -> None:
    """Алгоритм сортировки выбором."""
    N = len(arr)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if arr[k] < arr[pos]:
                arr[k], arr[pos] = arr[pos], arr[k]


def bubble_sort(arr: list) -> None:
    """Алгоритм сортировки пузырьком."""
    print("Сортировка запущена")
    N = len(arr)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]


def count_sort(arr: list) -> None:
    """Алгоритм сортировки подсчетом."""
    N = len(arr)
    output = [0] * N
    count = [0] * 10

    for i in range(0, N):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = N - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, N):
        arr[i] = output[i]


def quick_sort(arr: list) -> None:
    """Алгоритм быстрой сортировки."""
    if len(arr) <= 1:
        return
    barrier = arr[0]
    L = []
    M = []
    R = []
    for x in arr:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in L + M + R:
        arr[k] = x
        k += 1


def merge(A: list[int], B: list[int]) -> list[int]:
    """Вспомогальный метод для сортировки слиянием."""
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(arr: list[int]) -> None:
    """Алгоритм сортировки слиянием."""
    if len(arr) <= 1:
        return
    middle = len(arr) // 2
    L = [arr[i] for i in range(middle)]
    R = [arr[i] for i in range(middle, len(arr))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(arr)):
        arr[i] = C[i]
