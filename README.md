# 📊 Mô phỏng các Thuật toán Sắp xếp bằng Đồ họa

---

## 1. 📝 Mô tả hệ thống

**“Mô phỏng các thuật toán sắp xếp bằng đồ họa”** là một chương trình trực quan giúp người dùng **nhập vào một dãy số gồm tối đa 20 phần tử**, sau đó **lựa chọn một trong sáu thuật toán sắp xếp phổ biến** để quan sát quá trình sắp xếp.

Sau khi người dùng lựa chọn thuật toán, chương trình sẽ **mô phỏng trực quan từng bước sắp xếp**: các phần tử được di chuyển, so sánh và thay đổi vị trí thông qua các hiệu ứng hình ảnh. Kết quả cuối cùng là một dãy số đã được sắp xếp theo thứ tự tăng dần.

Chương trình hướng đến mục tiêu:
- Hỗ trợ người học hiểu rõ nguyên lý hoạt động của các thuật toán sắp xếp.
- Tạo ra một trải nghiệm học thuật sinh động, trực quan và dễ tiếp cận.

---

## 2. ⚙️ Các yêu cầu & tính năng cơ bản

Chương trình hỗ trợ mô phỏng **6 thuật toán sắp xếp** thông dụng, mỗi thuật toán đều có:
- Mô phỏng bằng đồ họa động
- Tùy chọn số lượng và giá trị phần tử đầu vào (tối đa 20 phần tử)
- Kết quả sắp xếp được hiển thị trực quan sau khi hoàn tất

### ✅ Danh sách thuật toán hỗ trợ:

| STT | Thuật toán                 | Tên tiếng Anh         |
|-----|----------------------------|------------------------|
| 1   | Sắp xếp chọn               | Selection Sort         |
| 2   | Sắp xếp chèn               | Insertion Sort         |
| 3   | Sắp xếp nổi bọt            | Bubble Sort            |
| 4   | Sắp xếp trộn               | Merge Sort             |
| 5   | Sắp xếp nhanh              | Quick Sort             |
| 6   | Sắp xếp vun đống (heap)    | Heap Sort              |

---

## 3. 📦 Các thư viện hỗ trợ

Chương trình được xây dựng bằng ngôn ngữ **Python** và sử dụng các thư viện sau để hỗ trợ việc xây dựng giao diện và trực quan hóa:

| Thư viện       | Chức năng chính                                                                 | Cài đặt |
|----------------|----------------------------------------------------------------------------------|--------|
| `tkinter`      | Tạo giao diện người dùng (GUI)                                                   |        |
| `matplotlib`   | Hiển thị biểu đồ và hoạt ảnh trực quan cho quá trình sắp xếp                    |pip install matplotlib|
| `networkx`     | (Tùy chọn) Dùng để mô tả cấu trúc dữ liệu dạng đồ thị, hỗ trợ trực quan nâng cao |pip install networkx|

---
> 📚 Dự án cuối kỳ môn lập trình Python mang tính học thuật, tham khảo đối với sinh viên.
