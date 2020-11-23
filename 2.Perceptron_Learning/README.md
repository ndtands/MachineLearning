# Perceptron Learning Algorithm (PLA)
## 1. Introduce:
- Perceptron là một thuật toán Classification cho trường hợp đơn giản nhất : Chỉ có hai class (lớp) hay còn gọi là binary classification và cũng chỉ hoạt động được trong một số trường hợp cũ thể. Nó là một phần của Neural Networks.
- Bài toán được phát biểu như sau: Chó hai class được gán nhãn, hãy tìm một đường thẳng sao cho toàn bộc ác điểm thuộc class 1 nằm về 1 phía, toàn bộ các điểm thuộc class 2 nằm về phía còn lại của đường thẳng đó. Nếu tồn tại đường thằng như vậy thì nó gọi là linearly separable. Các thuật toán classification tạo ra các boundary là các đường thẳng được gọi chung à Linear Classifier.
## 2. Thuật toán (PLA)
- Giống như các thuật toán lặp trong K-means Clustering và GradientDescent, ý tưởng cơ bản của PLA là xuất phát từ một nghiệm dự đoán nào đó, qua mỗi vòng lặp, nghiệm sẽ được cập nhật đến vị trí tốt hơn. Việc cập nhật này dựa trên việc giảm giá trị của một hàm mất mát nào đó.
### Tóm tắt PLA
1. Chọn ngẫy nhiên một vector hệ số w với các phần tử gần 0.
2. Duyệt ngẫu nhiên qua từng điểm dữ liệu x_i:
- Nếu x_i được phần lớp đúng, tức sgn(W.T*x_i)=y_i, chúng ta không cần làm gì.
- Nếu x_i bị misclassifed, cập nhật w theo công thức :
        w = w +y_i*x_i
3. Kiểm tra xem có bao nhiêu điểm bị misclassifed. Nếu không còn điểm nào, dừng thuật toán. Nếu còn, quay lại bước 2
### Kết quả thực hiện được với giải thuật PLA
<p align="center">
  <img src="pla_vi.gif" />
</p>

### Ứng dụng
- Hàm số xác định class của Perceptron: label(x)=sgn(w.T*x) có thể được mô tả như 1 network.
<p align="center">
  <img src="n.png" />
</p>

- Hay y = sgn(z).
- Trong giải thuật PLA là ta đi tìm các weights (w) sao cho ứng mỗi x_i đặt ở output, cho ra input của network trùng với nhãn y_i tương ứng.
- Khi đó hàm số sgn(z) gọi là **activation function**. Có nhiều hàm như vậy: tanh(x), sigmoi(x),...
- Dễ dàng nhận xét thấy, nếu y=z thì nó là hàm mô tả thuật toán Linear Regresstion.

### Vấn đề phát sinh
- PLA có thể cho vô số nghiệm khác nhau.
- PLA đòi hỏi dữ liệu linearly separable: Nếu có một điểm thuộc class này lại nằm trong class kia thì PLA sẽ không làm việc được vì luôn có ít nhất 1 điểm bị misclassified. Nên giải thuật sẽ không hội tụ.
=> Việc không hội tụ với dữ liệu gần linearly separable là một nhược điểm lớn. 
- Để cải biến chuyện này, người ta đã đưa ra một thuật toán Pocket Algorithm

### Pocket Algorithm
- Nếu như giải thuật PLA cố gắng phân 2 class hoàn toàn, thì giải thuật PA sẽ cố gắng đi kiếm w mà có số lượng misclassified nhỏ nhất.
=> Thuật toán này giống với thuật toán tìm phần tử nhỏ nhất trong 1 mảng.


