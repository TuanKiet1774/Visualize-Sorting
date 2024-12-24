from tkinter import *
from Visualize import *
from Sort import *

def interaction():
    try:
        # Lấy số lượng phần tử và các giá trị từ giao diện
        n = int(entry_n.get())
        elements = entry_elements.get().split()
        array = list(map(int, elements))
        
        # Kiểm tra số lượng phần tử
        if len(array) != n:
            result_label.config(text="Số lượng phần tử không khớp! Vui lòng thử lại (cách nhau bởi khoảng trắng).", fg="red")
            return
        elif n < 5 or n > 20:
            result_label.config(text="Số lượng phần tử trong khoảng 0 - 20", fg="red")
            return
        else:
            result_label.config(text="")

        # Lấy thuật toán được chọn
        algorithm = algorithm_var.get()

        # Thực hiện sắp xếp và trực quan hóa
        if algorithm == "Selection Sort":
            selection_sort_visualize(array)
        elif algorithm == "Insertion Sort":
            insertion_sort_visualize(array)
        elif algorithm == "Bubble Sort":
            bubble_sort_visualize(array)
        elif algorithm == "Merge Sort":
            merge_sort_visualize(array)
        elif algorithm == "Heap Sort":
            heap_sort_visualize(array)
        elif algorithm == "Quick Sort":
            quick_sort_visualize(array)
        else:
            result_label.config(text="Vui lòng chọn một thuật toán hợp lệ!", fg="red")
    except ValueError:
        result_label.config(text="Dữ liệu không hợp lệ! Vui lòng nhập lại.", fg="red")

# Tạo cửa sổ chính
root = Tk()
root.title("Mô phỏng thuật toán sắp xếp")
root.geometry("600x300")

# Khung nhập số lượng phần tử
frame = Frame(root)
frame.pack(pady=10)
label_n = Label(frame, text="Nhập số lượng phần tử:", font=("Arial", 10))
label_n.grid(row=0, column=0, padx=10, pady=10)
entry_n = Entry(frame, width=10)
entry_n.grid(row=0, column=1, padx=5, pady=5)

# Khung nhập các phần tử
label_elements = Label(frame, text="Nhập các phần tử:", font=("Arial", 10))
label_elements.grid(row=1, column=0, padx=5, pady=5)
entry_elements = Entry(frame, width=50)
entry_elements.grid(row=1, column=1, padx=15, pady=15)

# Khung chọn thuật toán
label_algorithm = Label(frame, text="Chọn thuật toán sắp xếp:", font=("Arial", 10))
label_algorithm.grid(row=2, column=0, padx=5, pady=5)
algorithm_var = StringVar(value="Thuật toán sắp xếp")
algorithm_menu = OptionMenu(frame, algorithm_var, "Selection Sort", "Insertion Sort", "Bubble Sort", "Merge Sort", "Heap Sort", "Quick Sort")
algorithm_menu.grid(row=2, column=1, padx=5, pady=5)

# Nút bắt đầu sắp xếp
sort_button = Button(root, text="Trực quan hóa", command=interaction)
sort_button.pack(pady=10)

# Nhãn hiển thị kết quả
result_label = Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)

# Chạy ứng dụng
root.mainloop()
