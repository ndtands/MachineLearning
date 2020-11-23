# Binary Classififiers
Các giải thuật classififiers đã được đề cập : Perceptron Learning Algorithm và Logisstic Regression hoặc Linear Regression.
### Binary Classifiers cho Multi-class Classification problems
- Nếu nhiều hơn 2 class thì có thể xài nhiều giải thuật khác, nhưng ở đây, chúng ta có thể dùng binary classifier để thực hiện việc này.
- Có its nhất 4 cách áp dụng được binary classdifier.
#### 1. One vs One
- Xây dựng rất nhiều bộ binary classifiers cho từng cặp classes. 
- Nếu có C classé thì tổng số binary classifiers là c(c-1)/2. Đây là con số lớn nếu c nhiều => không mang lại lợi ích về mặt tính toán.

#### 2. Hierachical (phân tầng)
- Cách làm này sẽ làm giảm thời gian trainning so với one-vs-one.
- Ví duj: phân biệt 4,5,6,7. Nếu dùng one-vs-one thì cần 6 bộ binary classifiers. Nhưng nếu chúng ta phân tầng : Tầng 1: Phân biệt 2 cụm 4,7 và 5,6. Tầng 2: Phân biệt 4,7. Tầng 3: Phân biệt 5,6. Như vậy chỉ cần 3 bộ binary classifies.
- Hạn chế là nếu như có 1 tầng làm việc sai thì dẫn dến các tầng sau đó có thể sai.

#### 3.Binary coding
- Tức mã hóa đầu vào theo mã nhị phân. m = [log2(C)], làm tròn lên.
- Hạn chế : Chỉ cần 1 bit phân loại sai thì dẫn đến dữ liệu bị phân loại sai. Hơn nữa, nếu số classes không phải là lũy thừa của hai, mã nhịn phân nhận được không thể là một giá trị không tương ứng với class nào cả.

#### 4. One-vs-rest hay one-hot coding
- Phương pháp này được sử dụng nhiều nhất. Cụ thể là nếu có C lasses thì ta sẽ xây dựng C classifies, một classidier tương ứng với một class. Classifier thứ nhất phân biệt class 1 với not class 1, classifier thứ hai phân biệt class 2 với not class 2,.... Kết quả cuối cùng có thể được xác định bằng cách xác định class mà nột điểm rơi vào với xác suất cao nhất.
- Ví dụ 1,2,3,4 tương ứng là 1000,0100,0010,0001.
- Hạn chế : Theo góc nhìn xác suất, một điểm dữ liệu có thể được dự đoán thuộc vào class 1,2,... C với xác xuất lần lược là p1,p2,...pC. Tuy nhiên, tổng các xác suất này không thể bằng 1. Nhưng có cách để đạt được chuyện này là dùng Softmax Regression.