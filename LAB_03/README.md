# GIẢI THÍCH BÀI THỰC HÀNH TUẦN 3

#### 1. Bài toán 4-Queens

##### 1.1. Tóm tắt yêu cầu

- Mục tiêu : Đặt 4 quân hậu trên bàn cờ 4x4 sao cho không quân nào tấn công quân khác.
- Các quân hậu có thể di chuyển theo đường ngang, đường dọc và đường chéo.
- Yêu cầu : Tìm và xác định số lượng các giải pháp hợp lệ cho bài toán 4-Queens.

#### 1.2 Giải pháp

Sử dụng thuật toán quay lui (Backtracking) :

- Duyệt từng hàng
- Ở mỗi hàng, thử đặt quân hậu vào từng cột
- Kiểm tra xem vị trí vừa đặt có an toàn không
- Nếu an toàn, tiếp tục đặt quân hậu ở hàng tiếp theo
- Nếu đặt thành công đến hàng cuối cùng - đã tìm được một giải pháp
- Nếu không tìm được giải pháp, quay lại và thử đặt quân hậu ở cột khác

#### 1.3 Code

file [`TH_2`](./TH_2.ipynb) có chứa ví dụ minh họa bài toán Queens, hôm nay sẽ tập trung cụ thể vào 4-Queens
sau đây là giải thích các function hoạt động như thế nào :

- `is_valid_state()` : Kiểm tra xem trạng thái hiện tại có vi phạm các luật của bài toán hay không, theo cách sau:

  - kiểm tra xem số lượng quân hậu đã được đặt trong (`state`) có bằng với tổng số quân hậu cần đặt (`num_queens`) hay không. Nếu có `(len(state) == num_queens)` thì trả về True, ngược lại trả về False

- `get_candidates()` : Tìm các vị trí có thể đặt quân mới.

  - Xác định các cột an toàn `candidates` để đặt quân hậu tiếp theo (không trùng cột và đường chéo)
  - Vòng lặp qua tất cả các quân hậu đã đặt:
    - `dist = position - row` là khoảng cách theo hàng giữa quân hậu đang xét và hàng hiện tại.
    - `candidates.discard(col)`: loại bỏ cột trùng (cùng cột).
    - `col ± dist`: loại bỏ 2 ô nằm trên 2 đường chéo giao nhau tại quân hậu đã đặt:
  - Trả về danh sách các cột an toàn

- `search()` : Đệ quy tìm lời giải hợp lệ

  - Nếu state là lời giải hợp lệ (đủ num_queens quân hậu), thêm vào danh sách solutions.
  - Với mỗi cột hợp lệ từ get_candidates():
    - Thêm quân hậu vào hàng hiện tại (state.append(candidate)).
    - Gọi đệ quy search() để tiếp tục đặt quân cho hàng tiếp theo.
    - Sau khi thử xong, quay lui bằng cách xóa quân hậu vừa đặt (state.remove(candidate)).

- `solve()` : Bắt đầu quá trình giải N-Queens

  - `solutions = []`: Danh sách để lưu các lời giải hợp lệ.
  - `state = []`: Trạng thái hiện tại – danh sách cột của các quân hậu đã đặt (theo từng hàng).
  - Gọi hàm `search()` để đệ quy tìm tất cả lời giải.
  - Trả về danh sách các lời giải sau khi tìm xong.

- `__main__` Khởi chạy chương trình, nhập số lượng quân hậu, tìm lời giải và in kết quả.

  - Nhập số lượng quân hậu
  - tạo bàn cờ rỗng `empty_board`
  - gọi hàm `solve()` với `num_queens` là số lượng quân hậu đã nhập, tìm lời giải hợp lệ
  - In ra tổng số lượng lời giải tìm được
  - Duyệt qua từng lời giải:
    - Tạo lại bàn cờ rỗng cho từng lời giải.
    - Đặt quân hậu vào đúng vị trí (theo hàng – cột trong `solution`).
    - In số thứ tự `index` và danh sách vị trí quân hậu trong lời giải.
  - In từng dòng của bàn cờ.
