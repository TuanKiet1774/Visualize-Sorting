import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx

# Hàm vẽ mảng số dưới dạng ô vuông
def draw_array_as_squares(array, highlight=None, ax=None, positions=None, y_positions=None):
    ax.clear()
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-2, 4)
    ax.axis('off')  # Ẩn trục
    for i, value in enumerate(array):
        # Vẽ hình chữ nhật
        color = 'red' if highlight and i in highlight else 'blue'
        rect = patches.Rectangle((positions[i], y_positions[i]), 1, 1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        # Vẽ giá trị bên trong ô
        ax.text(positions[i] + 0.5, y_positions[i] + 0.5, str(value), ha='center', va='center', fontsize=14, color='white')

# Hàm tạo hiệu ứng hoán đổi cho sắp xếp chọn
def swap_animation_selection(array, i, j, ax):
    n_frames = 30  # Số khung hình cho hoạt ảnh
    positions = list(range(len(array)))
    y_positions = [0] * len(array)

    # Bước 1: Di chuyển lên/xuống (trục y) để tránh đè lên nhau
    for frame in range(n_frames // 2):
        y_positions[i] = frame / 10  # Di chuyển lên
        y_positions[j] = -frame / 10  # Di chuyển xuống
        
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)
    
    # Bước 2: Di chuyển ngang (trục x) để đổi chỗ
    while positions[i] < positions[j]:
        distance = positions[j] - positions[i]  # Tính khoảng cách giữa hai ô
        dis = 0.1 # Di chuyển mỗi lần 0.05 đơn vị
        # Di chuyển dần dần cho tới khi di chuyển đủ khoảng cách
        while distance > 0:
            if distance < dis:
                dis = distance  # Nếu khoảng cách nhỏ hơn 0.05, chỉ di chuyển đủ khoảng cách còn lại
            positions[i] += dis  # Di chuyển ô i qua phải
            positions[j] -= dis  # Di chuyển ô j qua trái
            distance -= dis  # Cập nhật khoảng cách còn lại
            draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
            plt.pause(0.05)
            
    # Bước 3: Trở về trục X (y = 0)
    for frame in range(n_frames):
        # Di chuyển ô i xuống (trở về trục x nếu ô i ở trên)
        if y_positions[i] > 0:
            y_positions[i] -= 0.1  # Di chuyển xuống từng bước nhỏ đến 0
            if y_positions[i] < 0:  # Đảm bảo không đi quá trục x
                y_positions[i] = 0
        
        # Di chuyển ô j lên (trở về trục x nếu ô j ở dưới)
        if y_positions[j] < 0:
            y_positions[j] += 0.1  # Di chuyển lên từng bước nhỏ đến 0
            if y_positions[j] > 0:  # Đảm bảo không đi quá trục x
                y_positions[j] = 0
        
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Hoán đổi vị trí các ô theo đúng vị trí của nhau
    target_pos_i, target_pos_j = positions[j], positions[i]
    positions[i] = target_pos_j
    positions[j] = target_pos_i

    # Bước 4: Cập nhật giá trị hoán đổi trong mảng
    array[i], array[j] = array[j], array[i]
    y_positions[i], y_positions[j] = 0, 0  # Trả lại vị trí y

# Hàm tạo hiệu ứng hoán đổi cho sắp xếp chèn
def swap_animation_insertion(array, i, j, ax):
    n_frames = 30  # Số khung hình cho hoạt ảnh
    positions = list(range(len(array)))
    y_positions = [0] * len(array)

    # Bước 1: Di chuyển lên/xuống (trục y) để tránh đè lên nhau
    for frame in range(n_frames // 2):
        y_positions[i] = frame / 10  # Di chuyển ô i lên
        y_positions[j] = -frame / 10  # Di chuyển ô j xuống
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 2: Di chuyển ngang (trục x) để đổi chỗ
    x_distance = positions[j] - positions[i]  # Khoảng cách trên trục x
    step = x_distance / (n_frames // 2)  # Khoảng cách di chuyển mỗi khung hình
    for frame in range(n_frames // 2):
        positions[i] += step
        positions[j] -= step
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 3: Trở về trục X (y = 0)
    for frame in range(n_frames // 2):
        y_positions[i] = max(0, y_positions[i] - 1 / 15)  # Di chuyển dần xuống
        y_positions[j] = min(0, y_positions[j] + 1 / 15)  # Di chuyển dần lên
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 4: Cập nhật giá trị hoán đổi trong mảng
    array[i], array[j] = array[j], array[i]

# Hàm tạo hiệu ứng hoán đổi trong Bubble Sort
def swap_animation_bubble(array, i, j, ax):
    n_frames = 30  # Số khung hình cho hoạt ảnh
    positions = list(range(len(array)))
    y_positions = [0] * len(array)

    # Bước 1: Di chuyển lên/xuống (trục y) để tránh đè lên nhau
    for frame in range(n_frames // 2):
        y_positions[i] = frame / 15  # Di chuyển ô i lên
        y_positions[j] = -frame / 15  # Di chuyển ô j xuống
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 2: Di chuyển ngang (trục x) để đổi chỗ
    x_distance = positions[j] - positions[i]  # Khoảng cách trên trục x
    step = x_distance / (n_frames // 2)  # Khoảng cách di chuyển mỗi khung hình
    for frame in range(n_frames // 2):
        positions[i] += step
        positions[j] -= step
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 3: Trở về trục X (y = 0)
    for frame in range(n_frames // 2):
        y_positions[i] = max(0, y_positions[i] - 1 / 15)  # Di chuyển dần xuống
        y_positions[j] = min(0, y_positions[j] + 1 / 15)  # Di chuyển dần lên
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 4: Cập nhật giá trị hoán đổi trong mảng
    array[i], array[j] = array[j], array[i]

#-------------------------------------------------------------
# Hàm hợp nhất hai mảng con
def merge(array, start, mid, end, ax, positions, y_positions):
    left = array[start:mid + 1]
    right = array[mid + 1:end + 1]
    l_idx = 0
    r_idx = 0
    sorted_idx = start

    # Tăng vị trí y của mảng con để hiển thị rõ các bước hợp nhất
    for i in range(start, end + 1):
        y_positions[i] -= 1

    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.pause(0.5)

    # Hợp nhất hai mảng con
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            array[sorted_idx] = left[l_idx]
            highlight = [sorted_idx]  # Highlight phần tử đang được đưa vào vị trí mới
            l_idx += 1
        else:
            array[sorted_idx] = right[r_idx]
            highlight = [sorted_idx]  # Highlight phần tử đang được đưa vào vị trí mới
            r_idx += 1

        # Cập nhật y_positions cho cả hai phần tử đang so sánh
        y_positions[sorted_idx] += 1
        draw_array_as_squares(array, ax=ax, highlight=highlight, positions=positions, y_positions=y_positions)
        plt.pause(0.5)
        sorted_idx += 1

    # Copy phần còn lại của mảng con bên trái
    while l_idx < len(left):
        array[sorted_idx] = left[l_idx]
        y_positions[sorted_idx] += 1  # Đưa giá trị hợp nhất lên hàng trên
        highlight = [sorted_idx]
        draw_array_as_squares(array, ax=ax, highlight=highlight, positions=positions, y_positions=y_positions)
        plt.pause(0.5)
        l_idx += 1
        sorted_idx += 1

    # Copy phần còn lại của mảng con bên phải
    while r_idx < len(right):
        array[sorted_idx] = right[r_idx]
        y_positions[sorted_idx] += 1  # Đưa giá trị lên hàng trên
        highlight = [sorted_idx]
        draw_array_as_squares(array, ax=ax, highlight=highlight, positions=positions, y_positions=y_positions)
        plt.pause(0.5)
        r_idx += 1
        sorted_idx += 1

# Hàm đệ quy cho Merge Sort
def merge_sort_recursive(array, start, end, ax, positions, y_positions):
    if start < end:
        mid = (int)((start + end) / 2)
        # Tách mảng con bên trái
        merge_sort_recursive(array, start, mid, ax, positions, y_positions)
        # Tách mảng con bên phải
        merge_sort_recursive(array, mid + 1, end, ax, positions, y_positions)
        # Hợp nhất hai mảng con
        merge(array, start, mid, end, ax, positions, y_positions)

#-------------------------------------------------------------
# Hàm vẽ mảng số dưới dạng ô vuông và hiển thị tọa độ
def draw_array_quick(array, highlight=None, pivot=None, ax=None, positions=None, y_positions=None):
    ax.clear()
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-2, 4)
    ax.axis('off')  # Ẩn trục
    for i, value in enumerate(array):
        # Vẽ hình chữ nhật
        if pivot is not None and i == pivot:
            color = 'yellow'  # Pivot có màu vàng
        elif highlight and i in highlight:
            color = 'red'  # Đổi chỗ có màu đỏ
        else:
            color = 'blue'  # Bình thường có màu xanh
        rect = patches.Rectangle((positions[i], y_positions[i]), 1, 1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        # Vẽ giá trị bên trong ô
        ax.text(positions[i] + 0.5, y_positions[i] + 0.5, str(value), ha='center', va='center', fontsize=14, color='white')

# Hàm tạo hiệu ứng hoán đổi
def swap_animation_quick(array, i, j, ax, pivot):
    n_frames = 30  # Số khung hình cho hoạt ảnh
    positions = list(range(len(array)))
    y_positions = [0] * len(array)

    # Bước 1: Di chuyển lên/xuống (trục y) để tránh đè lên nhau
    for frame in range(n_frames // 2):
        y_positions[i] = frame / 10  # Di chuyển ô i lên
        y_positions[j] = -frame / 10  # Di chuyển ô j xuống
        draw_array_quick(array, highlight=[i, j], pivot=pivot, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 2: Di chuyển ngang (trục x) để đổi chỗ
    x_distance = positions[j] - positions[i]  # Khoảng cách trên trục x
    step = x_distance / (n_frames // 2)  # Khoảng cách di chuyển mỗi khung hình
    for frame in range(n_frames // 2):
        positions[i] += step
        positions[j] -= step
        draw_array_quick(array, highlight=[i, j], pivot=pivot, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 3: Trở về trục X (y = 0)
    for frame in range(n_frames // 2):
        y_positions[i] = max(0, y_positions[i] - 1 / 10)  # Di chuyển dần xuống
        y_positions[j] = min(0, y_positions[j] + 1 / 10)  # Di chuyển dần lên
        draw_array_quick(array, highlight=[i, j], pivot=pivot, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 4: Cập nhật giá trị hoán đổi trong mảng
    array[i], array[j] = array[j], array[i]

#-------------------------------------------------------------
# Hàm vẽ cây nhị phân
def draw_binary_tree(array, ax, n, highlight_root=None, highlight_swap=None):
    ax.clear()  # Xóa nội dung trước khi vẽ lại
    G = nx.DiGraph()
    positions = {}
    edges = []

    def add_edges_and_positions(index, x, y, level_gap):
        if index >= n:  # Chỉ vẽ các phần tử trong phạm vi heap
            return
        G.add_node(index, value=array[index])
        positions[index] = (x, y)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < n:
            G.add_edge(index, left_child)
            edges.append((index, left_child))
            add_edges_and_positions(left_child, x - level_gap, y - 1, level_gap / 2)
        if right_child < n:
            G.add_edge(index, right_child)
            edges.append((index, right_child))
            add_edges_and_positions(right_child, x + level_gap, y - 1, level_gap / 2)

    add_edges_and_positions(0, 0, 0, 0.7)

    # Đảm bảo nút gốc luôn có màu đỏ và làm nổi bật các nút đổi chỗ
    node_colors = []
    for node in G.nodes():
        if highlight_root is not None and node == highlight_root:
            node_colors.append('red')  # Nút gốc màu đỏ
        elif highlight_swap is not None and (node == highlight_swap[0] or node == highlight_swap[1]):
            node_colors.append('yellow')  # Nút đang đổi chỗ màu vàng
        else:
            node_colors.append('skyblue')

    # Vẽ cây mà không thay đổi các đường nối
    nx.draw(G, pos=positions, ax=ax, with_labels=False, node_size=1000, node_color=node_colors, edgelist=edges)
    labels = {node: G.nodes[node]['value'] for node in G.nodes()}
    nx.draw_networkx_labels(G, pos=positions, labels=labels, ax=ax, font_size=8, font_color='black')

# Hàm di chuyển các nút
def move_node(array, i, j, ax_tree, ax_array, n):
    positions = {}
    G = nx.DiGraph()
    edges = []

    # Xây dựng cây nhị phân
    def add_edges_and_positions(index, x, y, level_gap):
        if index >= n:
            return
        G.add_node(index, value=array[index])
        positions[index] = (x, y)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < n:
            G.add_edge(index, left_child)
            edges.append((index, left_child))
            add_edges_and_positions(left_child, x - level_gap, y - 1, level_gap / 2)
        if right_child < n:
            G.add_edge(index, right_child)
            edges.append((index, right_child))
            add_edges_and_positions(right_child, x + level_gap, y - 1, level_gap / 2)
    add_edges_and_positions(0, 0, 0, 0.7)

    # Tạo hiệu ứng di chuyển giữa các nút
    steps = 20
    x1, y1 = positions[i]
    x2, y2 = positions[j]

    for step in range(steps + 1):
        alpha = step / steps
        x = (1 - alpha) * x1 + alpha * x2
        y = (1 - alpha) * y1 + alpha * y2

        positions[i] = (x, y)
        positions[j] = (x2 - alpha * (x2 - x1), y2 - alpha * (y2 - y1))

        node_colors = ['red' if node == i or node == j else 'skyblue' for node in G.nodes()]
        ax_tree.clear()  # Xóa cây trước khi vẽ lại
        nx.draw(G, pos=positions, ax=ax_tree, with_labels=False, node_size=1000, node_color=node_colors, edgelist=edges)
        labels = {node: G.nodes[node]['value'] for node in G.nodes()}
        nx.draw_networkx_labels(G, pos=positions, labels=labels, ax=ax_tree, font_size=8, font_color='black')

        draw_array(array, n, ax_array)
        plt.pause(0.05)  # Thời gian tạm dừng giữa mỗi bước di chuyển

# Hàm vẽ dãy số
def draw_array(array, n, ax):
    ax.clear()  # Xóa nội dung trước khi vẽ lại
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-1, 2)
    ax.axis('off')

    for i in range(len(array)):
        color = 'red' if i >= n else 'blue'  # Đánh dấu phần tử đã sắp xếp
        rect = patches.Rectangle((i, 0), 1, 1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(i + 0.5, 0.5, str(array[i]), ha='center', va='center', fontsize=10, color='white')

# Hàm heapify với hiệu ứng di chuyển
def heapify(array, n, i, ax_tree, ax_array):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        move_node(array, i, largest, ax_tree, ax_array, n)
        array[i], array[largest] = array[largest], array[i]
        draw_binary_tree(array, ax_tree, n, highlight_root=i, highlight_swap=(i, largest))
        draw_array(array, n, ax_array)
        plt.pause(1) 
        heapify(array, n, largest, ax_tree, ax_array)
