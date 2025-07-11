# LAB 05 : CNN
### Phần bài tập lý thuyết:


### Phần bài tập thực hành:

1. Đánh giá sau khi thay đổi số lượng epoch:
- Sau 5 epoch, mô hình đã đạt được độ chính xác rất cao (`~98.4–98.5%`) và loss giảm mạnh so với epoch đầu. 
- Khi tiếp tục huấn luyện đến 10 epoch, loss tiếp tục giảm nhẹ và accuracy tăng thêm một chút (`~98.98%`), nhưng tốc độ cải thiện đã chậm lại rõ rệt.
- Điều này cho thấy mô hình đã học rất tốt chỉ sau 5 epoch, các epoch tiếp theo chủ yếu giúp tinh chỉnh thêm chút.

2. Thêm một tầng tích chập:
- Độ chính xác tăng nhanh qua từng epoch, từ `84.93%` lên `98.13%`.
- Loss giảm mạnh từ `0.4780` xuống `0.0606`, cho thấy mô hình học rất tốt ở các epoch đầu, các epoch sau thì cải thiện accuracy và loss chậm lại, mô hình dần hội tụ.
- Điều này cho thấy chỉ cần 3–5 epoch, mô hình đã đạt hiệu quả cao, các epoch sau chủ yếu giúp tinh chỉnh thêm một chút.
- độ chính xác cuối cùng trên tập test giảm nhẹ 0.5%, cho thấy mô hình bị overfit nhẹ

3. So sánh `Lr=0.1` và `Lr=0.001`:
- Khi sử dụng learning rate nhỏ (`lr=0.001`), mô hình học chậm hơn, mất nhiều epoch để đạt độ chính xác cao, nhưng quá trình học ổn định và tránh được việc nhảy qua các cực trị.
- Với learning rate lớn hơn (`lr=.1`), mô hình học rất nhanh, chỉ sau 1–2 epoch đã đạt accuracy cao, loss giảm mạnh. Tuy nhiên, nếu learning rate quá lớn có thể gây mất ổn định hoặc không hội tụ, nhưng trong trường hợp này, `lr=0.1` vẫn cho kết quả tốt

4. So sánh feature map
- Feature Map 1 không kích hoạt (đen), cho thấy kernel chưa học được đặc trưng
- Feature Map 2 thể hiện rõ nét số 7, chứng tỏ đã học được đặc trưng như cạnh/nét
- Thêm tầng conv2 giúp trích xuất đặc trưng sâu hơn và rõ ràng hơn
- Các feature map ở conv2 có độ trừu tượng cao hơn, nhưng vẫn giữ đuợc hình dạng số 7
- Tầng Feature Map từ `conv2` cho thấy quá trình học đặc trưng tiến triển từ đơn giản đến phức tạp trong CNN