import matplotlib.pyplot as plt
from Visualize import *

def selection_sort_visualize(array, order="ascending"):
    fig, ax = plt.subplots(figsize=(10, 4))
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=list(range(len(array))), y_positions=[0] * len(array))
            plt.pause(0.5)
            if (order == "ascending" and array[j] < array[min_idx]) or (order == "descending" and array[j] > array[min_idx]):
                min_idx = j
        if min_idx != i:
            swap_animation_selection(array, i, min_idx, ax)
        draw_array_as_squares(array, highlight=[], ax=ax, positions=list(range(len(array))), y_positions=[0] * len(array))
    plt.show()
    
def insertion_sort_visualize(array, order="ascending"):
    fig, ax = plt.subplots(figsize=(10, 4))
    positions = list(range(len(array)))  # Vị trí ban đầu trên trục X
    y_positions = [0] * len(array)  # Vị trí trên trục Y (mặc định là 0)

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        if order == "ascending":
            while j >= 0 and array[j] > key:
                swap_animation_insertion(array, j + 1, j, ax)
                j -= 1
        elif order == "descending":
            while j >= 0 and array[j] < key:
                swap_animation_insertion(array, j + 1, j, ax)
                j -= 1
        array[j + 1] = key
    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.show()
    
def bubble_sort_visualize(array, order="ascending"):
    fig, ax = plt.subplots(figsize=(10, 4))
    positions = list(range(len(array)))  # Vị trí ban đầu trên trục X
    y_positions = [0] * len(array)  # Vị trí trên trục Y (mặc định là 0)

    # Thuật toán Bubble Sort
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if (order == "ascending" and array[j] > array[j + 1]) or \
               (order == "descending" and array[j] < array[j + 1]):
                swap_animation_bubble(array, j, j + 1, ax)

    # Vẽ lại toàn bộ mảng sau khi sắp xếp xong
    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.show()
   
def merge_sort_visualize(array, order="ascending"):
    fig, ax = plt.subplots(figsize=(12, 8))
    positions = list(range(len(array)))  # Vị trí x của các phần tử
    y_positions = [0] * len(array)  # Vị trí y ban đầu

    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.pause(0.5)

    merge_sort_recursive(array, 0, len(array) - 1, ax, positions, y_positions, order)

    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.show()
    
# Hàm heap sort với hiển thị trực quan
def heap_sort_visualize(array, order="ascending"):
    fig, (ax_tree, ax_array) = plt.subplots(2, 1, figsize=(12, 8)) 
    n = len(array)
    fig.set_size_inches(14, 10)  
    # Xây dựng heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i, ax_tree, ax_array, order)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        draw_binary_tree(array, ax_tree, i, highlight_root=0)  
        draw_array(array, i, ax_array)  
        plt.pause(1) 

        plt.pause(1) 
        draw_array(array, n, ax_array) 
        heapify(array, i, 0, ax_tree, ax_array, order)

    draw_binary_tree([], ax_tree, 0) 
    draw_array(array, 0, ax_array)
    plt.show()

# Hàm phân hoạch cho thuật toán QuickSort
def quick_sort_partition(array, low, high, ax, positions, y_positions, order="ascending"):
    pivot_index = (low + high) // 2
    pivot = array[pivot_index]
    left = low
    right = high

    while left <= right:
        draw_array_quick(array, highlight=None, pivot=pivot_index, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)
        # So sánh dựa trên thứ tự
        while (array[left] < pivot if order == "ascending" else array[left] > pivot):
            left += 1
        while (array[right] > pivot if order == "ascending" else array[right] < pivot):
            right -= 1
        if left <= right:
            swap_animation_quick(array, left, right, ax, pivot=pivot_index)
            left += 1
            right -= 1
    return left

# Hàm sắp xếp QuickSort trực quan
def quick_sort(array, low, high, ax, positions, y_positions, order="ascending"):
    if low < high:
        pivot_index = quick_sort_partition(array, low, high, ax, positions, y_positions, order)
        quick_sort(array, low, pivot_index - 1, ax, positions, y_positions, order)
        quick_sort(array, pivot_index, high, ax, positions, y_positions, order)
    
    draw_array_quick(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.pause(0.05)

# Hàm gọi thuật toán QuickSort và hiển thị kết quả
def quick_sort_visualize(array, order="ascending"):
    fig, ax = plt.subplots(figsize=(10, 4))
    positions = list(range(len(array)))  # Vị trí ban đầu trên trục X
    y_positions = [0] * len(array)  # Vị trí trên trục Y (mặc định là 0)

    quick_sort(array, 0, len(array) - 1, ax, positions, y_positions, order)
    plt.show()

