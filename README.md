# Fingerprint Recognition
* BTL Nhập môn An toàn thông tin
* Mô tả yêu cầu: Tìm hiểu và xây dựng chương trình nhận diện vân tay

* python tkinter01.py


* Một số hình ảnh minh họa:
 
- Tổng quan Chương trình:

  ![image](https://user-images.githubusercontent.com/62825098/119702224-69cb7e80-be7f-11eb-8f45-b7048f9653b2.png)

- Chọn ảnh đầu vào
  
  ![image](https://user-images.githubusercontent.com/62825098/119702233-6cc66f00-be7f-11eb-8039-2df1857b0eb5.png)

- Tiền xử lý
  + Chuẩn hóa ảnh:
  
  ![image](https://user-images.githubusercontent.com/62825098/119702245-718b2300-be7f-11eb-9e9a-bf4dceb0f8a7.png)

  + Phân đoạn ảnh:
  
  ![image](https://user-images.githubusercontent.com/62825098/119702292-810a6c00-be7f-11eb-8fec-38e978ceb601.png)

  + Ước lượng hướng vân cục bộ:
  
  ![image](https://user-images.githubusercontent.com/62825098/119702327-89fb3d80-be7f-11eb-8a4c-5b1f630323d7.png)

  + Lọc Gabor:
  
  ![image](https://user-images.githubusercontent.com/62825098/119702353-9089b500-be7f-11eb-920f-aecae9066931.png)

  + Làm mỏng:
  
  ![image](https://user-images.githubusercontent.com/62825098/119702378-97b0c300-be7f-11eb-919b-e5db52f714a6.png)

  + Trích chọn đặc trưng minutias:
  
  ![image](https://user-images.githubusercontent.com/62825098/119702394-9da6a400-be7f-11eb-9c45-c986c94d31dc.png)

  + Trích chọn đặc trưng singularities:
 
  ![image](https://user-images.githubusercontent.com/62825098/119702420-a4351b80-be7f-11eb-9a1d-44f1fcb2be9e.png)


- Đối sánh: 
  + Vân tay có trong cơ sở dữ liệu:
 
  ![image](https://user-images.githubusercontent.com/62825098/119704087-73ee7c80-be81-11eb-847e-6f11a8ead93f.png)
  
  + Vân tay không tồn tại trong cơ sở dữ liệu:
  
  ![image](https://user-images.githubusercontent.com/62825098/119702574-cd55ac00-be7f-11eb-92a9-adf478985f6e.png)
