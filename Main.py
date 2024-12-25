from tkinter import *
from Visualize import *
from Sort import *

def interaction():
    try:
        # Lấy số lượng phần tử và các giá trị từ giao diện
        n = int(entry_n.get())
        elements = entry_elements.get().split()
        array = list(map(float, elements))
        
        # Kiểm tra số lượng phần tử
        if len(array) != n:
            result_label.config(text="Số lượng phần tử không khớp! Vui lòng thử lại (cách nhau bởi khoảng trắng).", fg="red")
            return
        elif n < 5 or n > 20:
            result_label.config(text="Số lượng phần tử trong khoảng 5 - 20", fg="red")
            return
        else:
            result_label.config(text="")

        # Lấy thuật toán được chọn
        algorithm = algorithm_var.get()
        
        # Lấy lựa chọn sắp xếp
        order = order_var.get()

        # Thực hiện sắp xếp và trực quan hóa
        if algorithm == "Selection Sort":
            selection_sort_visualize(array, order=order)
        elif algorithm == "Insertion Sort":
            insertion_sort_visualize(array, order=order)
        elif algorithm == "Bubble Sort":
            bubble_sort_visualize(array, order=order)
        elif algorithm == "Merge Sort":
            merge_sort_visualize(array, order=order)
        elif algorithm == "Heap Sort":
            heap_sort_visualize(array, order=order)
        elif algorithm == "Quick Sort":
            quick_sort_visualize(array, order=order)
        else:
            result_label.config(text="Vui lòng chọn một thuật toán hợp lệ!", fg="red")
    except ValueError:
        result_label.config(text="Dữ liệu không hợp lệ! Vui lòng nhập lại.", fg="red")

# Tạo cửa sổ chính
root = Tk()
root.title("Mô phỏng thuật toán sắp xếp")
root.geometry("600x400")

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

# Khung chọn thứ tự sắp xếp
label_order = Label(frame, text="Chọn thứ tự sắp xếp:", font=("Arial", 10))
label_order.grid(row=3, column=0, padx=5, pady=5)
order_var = StringVar(value="ascending")
order_frame = Frame(frame)
order_frame.grid(row=3, column=1, padx=5, pady=5)
ascending_button = Radiobutton(order_frame, text="Tăng dần", variable=order_var, value="ascending", font=("Arial", 10))
ascending_button.pack(side=LEFT, padx=5)
descending_button = Radiobutton(order_frame, text="Giảm dần", variable=order_var, value="descending", font=("Arial", 10))
descending_button.pack(side=LEFT, padx=5)

# Nút bắt đầu sắp xếp
sort_button = Button(root, text="Trực quan hóa", command=interaction)
sort_button.pack(pady=10)

# Nhãn hiển thị kết quả
result_label = Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)

# Hàm này sẽ gọi hàm interaction khi nhấn phím Enter
root.bind("<Return>", lambda event: interaction())

# Chạy ứng dụng
root.mainloop()
