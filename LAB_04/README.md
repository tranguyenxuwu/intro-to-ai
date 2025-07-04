# Lab 3: Phân tích Thuật Toán Di Truyền

**Deadline:** 04/07/2025 (2 tuần)

Dưới đây là phần nhận xét chi tiết về output của từng đoạn code trong file Jupyter Notebook `lab3.ipynb`. Qua các thí nghiệm này, tôi đã có những quan sát thú vị về cách hoạt động của thuật toán di truyền trong thực tế.

## Phân tích kết quả thí nghiệm

### Ví dụ 1: Tối ưu hóa hàm một biến

Hàm mục tiêu: Tối đa hóa `f(x) = -x² + 10x + 50`  
Nghiệm lý thuyết: `x = 5`, `f(x) = 75`

Kết quả thu được:

```
Thế hệ 1: x = 4.9903, f(x) = 74.9992
Thế hệ 2: x = 5.0034, f(x) = 74.9999
Thế hệ 3: x = 5.0034, f(x) = 75.0000
...
Kết quả cuối cùng: x = 5.0000, f(x) = 75.0000
```

Điều đáng chú ý là thuật toán hội tụ cực kỳ nhanh, chỉ cần 3-5 thế hệ để đạt nghiệm gần như chính xác. Với hàm parabol đơn giản như này, các phép lai ghép và lựa chọn đã khai thác hiệu quả vùng không gian chứa nghiệm tối ưu. Biểu đồ cho thấy sự tăng trưởng nhanh của fitness ở đầu, sau đó đi ngang khi đã đạt trạng thái ổn định.

### Ví dụ 2: Tối ưu hóa hàm hai biến

Hàm mục tiêu: Tối thiểu hóa `g(x, y) = x² + y²`  
Nghiệm lý thuyết: `(x, y) = (0, 0)`

Kết quả:

```
Thế hệ 1: (x, y) = (-0.3979, -0.3380), g(x, y) = 0.3585
...
Thế hệ 8: (x, y) = (0.0008, -0.0019), g(x, y) = 0.0000
...
Kết quả cuối cùng: (x, y) = (0.0002, -0.0010), g(x, y) = 0.0000
```

Thuật toán xử lý bài toán đa biến khá tốt, hội tụ về nghiệm `(0, 0)` với độ chính xác cao. Việc biến đổi bài toán tối thiểu hóa thành tối đa hóa bằng cách lấy giá trị âm tỏ ra là một chiến lược hiệu quả. Các giá trị cuối cùng của x và y đều là những số rất nhỏ, cho thấy thuật toán đã tìm được nghiệm với sai số minimal.

### Bài tập 1 & 2: Hàm lượng giác với mã hóa nhị phân

Hàm mục tiêu: Tối đa hóa `h(x) = sin(x) + cos(x)`  
Nghiệm lý thuyết: `x = π/4 ≈ 0.7854`, `h(x) = √2 ≈ 1.4142`

Kết quả sau 60 thế hệ:

```
Thế hệ 60, x tốt nhất = 0.7857, h(x) = 1.4142
Sai số tuyệt đối cho x: 0.000300
Sai số tuyệt đối cho h(x): 0.000000
```

Mã hóa nhị phân chứng tỏ hiệu quả của GA trong việc hoạt động trên không gian biểu diễn trừu tượng. Các phép toán trên chuỗi bit vẫn dẫn đến nghiệm tối ưu sau khi giải mã, mặc dù tốc độ hội tụ chậm hơn so với mã hóa thực. Điều này có thể do không gian tìm kiếm phức tạp hơn và hàm sin/cos có nhiều cực trị cục bộ.

Khi tăng `mutation_rate` lên 0.05, kết quả gần như không thay đổi, cho thấy với bài toán này, tỷ lệ đột biến cao hơn không gây nhiễu loạn quá trình tìm kiếm.

### Bài tập 3: Ảnh hưởng của các tham số

**Kích thước quần thể (Population Size):**

- 200 cá thể: Hội tụ nhanh nhất và ổn định nhất
- 50 cá thể: Hiệu suất khá tốt nhưng chậm hơn
- 10 cá thể: Hội tụ rất chậm, thường bị kẹt ở giá trị thấp

Kích thước quần thể lớn giúp tăng đa dạng di truyền, khám phá không gian tốt hơn và tránh các cực trị cục bộ.

**Tỷ lệ đột biến (Mutation Rate):**

- 0.01 và 0.05: Đều cho kết quả tốt
- 0.001: Hội tụ chậm do thiếu đa dạng

Tỷ lệ đột biến cần được cân bằng để đảm bảo sự khám phá và khai thác phù hợp.

**Tỷ lệ lai ghép (Crossover Rate):**

- 0.8 và 1.0: Hiệu suất cao nhất
- 0.2: Tốc độ hội tụ rất chậm

Lai ghép là toán tử chính thúc đẩy quá trình tìm kiếm, tỷ lệ cao thường mang lại hiệu quả tốt.

### Bài tập 4: So sánh phương pháp lựa chọn

**Roulette Wheel và Tournament (k=3):** Cả hai đều hội tụ nhanh về giá trị tối ưu với hiệu suất cao và tương đương nhau.

**Random Selection:** Gần như không có cải thiện đáng kể, đường cong gần như đi ngang ở giá trị thấp.

Kết quả này chứng minh tầm quan trọng của sức ép chọn lọc trong thuật toán di truyền. Việc ưu tiên các cá thể có fitness cao là động lực chính của quá trình tiến hóa. Random selection biến thuật toán thành tìm kiếm ngẫu nhiên không có định hướng.

### Bài tập 5: Trực quan hóa 3D

Hàm mục tiêu: Tối thiểu hóa `k(x, y, z) = x² + y² + z²`  
Nghiệm lý thuyết: `(0, 0, 0)`

Animation 3D cho thấy quá trình tiến hóa một cách trực quan:

- **Thế hệ đầu:** Các cá thể phân bố ngẫu nhiên rộng khắp trong không gian [-5, 5]
- **Các thế hệ giữa:** Quần thể bắt đầu co cụm và di chuyển về phía điểm tối ưu
- **Các thế hệ cuối:** Hầu hết các cá thể tập trung dày đặc xung quanh điểm (0, 0, 0)

Sự biến đổi từ phân bố rộng sang tập trung cho thấy quá trình chuyển từ khám phá sang khai thác của thuật toán.

## Kết luận

Các thí nghiệm đã minh họa rõ ràng các khía cạnh quan trọng của thuật toán di truyền: khả năng hội tụ, vai trò của các toán tử, và ảnh hưởng của việc điều chỉnh tham số. Đặc biệt, việc trực quan hóa giúp hiểu rõ "hành vi" của thuật toán trong quá trình tìm kiếm nghiệm. Từ hàm đơn giản một biến đến bài toán 3D phức tạp, GA đều thể hiện khả năng thích ứng và hiệu quả trong việc tìm kiếm nghiệm tối ưu.
