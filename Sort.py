import matplotlib.pyplot as plt
from Visualize import *

def selection_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(10, 4))
    for i in range(len(array)):
        min_idx = i
        # Tìm phần tử nhỏ nhất trong mảng còn lại
        for j in range(i + 1, len(array)):
            draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=list(range(len(array))), y_positions=[0] * len(array))
            plt.pause(0.5)
            if array[j] < array[min_idx]:
                min_idx = j
        # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên
        if min_idx != i:
            swap_animation_selection(array, i, min_idx, ax)
        draw_array_as_squares(array, highlight=[], ax=ax, positions=list(range(len(array))), y_positions=[0] * len(array))
    plt.show()
    
def insertion_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(10, 4))
    positions = list(range(len(array)))  # Vị trí ban đầu trên trục X
    y_positions = [0] * len(array)  # Vị trí trên trục Y (mặc định là 0)

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            swap_animation_insertion(array, j + 1, j, ax)
            j -= 1
        array[j + 1] = key
    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.show()
    
def bubble_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(10, 4))
    positions = list(range(len(array)))  # Vị trí ban đầu trên trục X
    y_positions = [0] * len(array)  # Vị trí trên trục Y (mặc định là 0)

    # Thuật toán Bubble Sort
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swap_animation_bubble(array, j, j + 1, ax)

    # Vẽ lại toàn bộ mảng sau khi sắp xếp xong
    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.show()
    
def merge_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(12, 8))
    positions = list(range(len(array)))  # Vị trí x của các phần tử
    y_positions = [0] * len(array)  # Vị trí y ban đầu
    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.pause(0.5)
    merge_sort_recursive(array, 0, len(array) - 1, ax, positions, y_positions)
    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.show()
    
def heap_sort_visualize(array):
    fig, (ax_tree, ax_array) = plt.subplots(2, 1, figsize=(12, 8))
    n = len(array)
    fig.set_size_inches(14, 10)

    # Xây dựng heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i, ax_tree, ax_array)

    # Trích xuất từng phần tử từ heap và đặt vào cuối dãy
    for i in range(n - 1, 0, -1):
        # Hoán đổi phần tử gốc với phần tử cuối cùng
        array[0], array[i] = array[i], array[0]
        draw_binary_tree(array, ax_tree, i, highlight_root=0) 
        draw_array(array, i, ax_array)  
        plt.pause(1) 

        draw_array(array, n, ax_array) 
        heapify(array, i, 0, ax_tree, ax_array)

    draw_binary_tree([], ax_tree, 0)  # Vẽ cây trống khi hoàn thành
    draw_array(array, 0, ax_array)
    plt.show()

# Hàm phân hoạch cho thuật toán QuickSort
def quick_sort_partition(array, low, high, ax, positions, y_positions):
    pivot_index = (low + high) // 2
    pivot = array[pivot_index]
    left = low
    right = high

    while left <= right:
        draw_array_quick(array, highlight=None, pivot=pivot_index, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            swap_animation_quick(array, left, right, ax, pivot=pivot_index)
            left += 1
            right -= 1
    return left

def quick_sort(array, low, high, ax, positions, y_positions):
    if low < high:
        pivot_index = quick_sort_partition(array, low, high, ax, positions, y_positions)
        quick_sort(array, low, pivot_index - 1, ax, positions, y_positions)
        quick_sort(array, pivot_index, high, ax, positions, y_positions)
    
    draw_array_quick(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.pause(0.05)

def quick_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(10, 4))
    positions = list(range(len(array)))  # Vị trí ban đầu trên trục X
    y_positions = [0] * len(array)  # Vị trí trên trục Y (mặc định là 0)

    quick_sort(array, 0, len(array) - 1, ax, positions, y_positions)
    plt.show()

