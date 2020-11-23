## Lưu ý :
- Nên chuẩn hóa dữ liệu trong khoảng từ 0-> 1 để làm giảm ảnh hưởng của Noise
- Thường dùng kỹ thuật Data Normalization để chuẩn hóa
- Ngoài norm 1 hoặc 2 thì có nhiều cách tính khoảng cách khác (tìm số điểm khác nhau giữa hai điểm dữ liệu)


## Ưu điểm :
- Độ phức tạp của quá trình training là 0
- Việc dự đoán kết qủa của dữ liệu mới đơn giản
- Không cần giải sử gì về phân phối của class

## Nhược điểm :
- KNN rất nhạy với nhiễu, đặc biệt là khi K nhỏ
- KNN là thuật toán mà mọi tính toán này ở khâu test, do đó
tính toán từ dữ liệu đến từng điểm trong training set sẽ rất tốn time, khi mà số điểm dữ liệu lớn, số chiều nhiều.
- KNN mà có K càng lớn thì càng phức tạp hơn trong tính toán. Ảnh hưởng đến hiệu năng của KNN

## Tăng tốc KNN
- Ngoài cách là tính khoảng cách từ 1 điểm test data đén tất cả các điểm trong traing set (Brute Force) thì còn những cách khác.
- K-D Tree : 
- Ball Tree:
