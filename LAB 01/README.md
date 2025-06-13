# LAB 01: Thuật Toán Tìm Kiếm Mù - Breadth-First Search & Depth-First Search

## 1. Tổng Quan

Lab này tập trung vào hai thuật toán tìm kiếm mù cơ bản trong trí tuệ nhân tạo: Thuật toán tìm kiếm theo chiều rộng (BFS) và thuật toán tìm kiếm theo chiều sâu (DFS). Các thuật toán này được áp dụng trên các đồ thị không trọng số và có trọng số để tìm đường đi từ một nút nguồn đến nút đích.

## 2. Cơ Sở Lý Thuyết

### 2.2 Tìm Kiếm theo Chiều Rộng (BFS)

- **Nguyên lý**: BFS khám phá tất cả các nút ở mức hiện tại trước khi chuyển sang mức tiếp theo.
- **Cấu trúc dữ liệu**: Hàng đợi (Queue) - FIFO (First In First Out).
- **Đặc điểm**:
  - Đảm bảo tìm ra đường đi ngắn nhất theo số cạnh trên đồ thị không trọng số.
  - Không đảm bảo đường đi có tổng trọng số nhỏ nhất trên đồ thị có trọng số.

### 2.3 Tìm Kiếm theo Chiều Sâu (DFS)

- **Nguyên lý**: DFS khám phá một nhánh đến tận cùng trước khi quay lại thử nhánh khác.
- **Cấu trúc dữ liệu**: Ngăn xếp (Stack) - LIFO (Last In First Out) hoặc đệ quy.
- **Đặc điểm**:
  - Không đảm bảo đường đi ngắn nhất trong cả đồ thị không trọng số và có trọng số.
  - Kết quả phụ thuộc vào thứ tự duyệt các nút kề.


## 3. Bài Tập Lập Trình

### So Sánh Hiệu Suất BFS và DFS
> [!NOTE]
> Đơn vị đo tính bằng miliseconds (ms) và đc làm tròn 3 chữ số vì giây quá nhỏ nên hơi khó hình dung 

Khi chạy trên đồ thị mẫu 6 (có trọng số):
- BFS: Thời gian chạy trung bình (5 lần) rơi vào `0.205 ms`
- DFS: Thời gian chạy trung bình (5 lần) rơi vào `0.149 ms`

Khi chạy trên đồ thị mẫu 7 (không trọng số):
- BFS: Thời gian chạy trung bình (5 lần) rơi vào : `0.144 ms`
- DFS: Thời gian chạy trung bình (5 lần) rơi vào : `0.119 ms`

Nhận xét: BFS và DFS có thời gian thực thi tương đương nhau trên các đồ thị nhỏ. Sự khác biệt về thời gian có thể trở nên đáng kể trên các đồ thị lớn hoặc không gian trạng thái rộng.

### Kết Quả trên Đồ Thị Phức Tạp (12 nút, 17 cạnh)

Khi chạy trên đồ thị phức tạp từ S đến N:
- BFS: Đường đi S → C → F → G → N với tổng trọng số 32
- DFS: Đường đi S → A → D → E → L → M → N với tổng trọng số 28


> [!Lưu ý chung] 
> - Tuy nói rằng việc tìm BFS và DFS điều có ưu điểm riêng, nhưng khi chạy thì phải đảm bảo để không bị rơi vào vòng lặp.
> - Nếu không kiểm tra kĩ thì rất dễ xảy ra tình trạng lặp đi lặp lại xét 2 đỉnh
> - Để giải quyết tình trạng này, ta sẽ chỉnh sửa input đồ thị vào, hoặc tạo ràng buộc `is_visited` kiểm tra các đỉnh đã thăm và không xét lại các đỉnh đó nữa 
> - Đó là lí do tại sao, khi mà ta mô hình hoá thủ công bằng tay thì ra được đường ngắn. Nhưng chạy chương trình thì lại ra đường dài hơn đáng kể.





