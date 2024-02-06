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
    N = len(arr)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]


def count_sort(arr: list) -> None:
    """Алгоритм сортировки подсчетом."""
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    for i in range(len(arr)):
        count_arr[arr[i] - min_value] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_value] - 1] = arr[i]
        count_arr[arr[i] - min_value] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]


def quick_sort(arr):
    """Алгоритм бьстрой сортировкиэ"""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


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
    if len(arr) > 1:
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
