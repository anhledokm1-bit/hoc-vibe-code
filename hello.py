# Viết chương trình nhập tên người dùng và in ra lời chào kèm theo ngày giờ hiện tại
# Viết chương trình nhập tên người dùng và in ra lời chào kèm theo ngày giờ hiện tại

from datetime import datetime

ten = input("Nhập tên của bạn: ")
ngay_thang_nam = datetime.now()
print("Xin chào " + ten + ", ngày " + str(ngay_thang_nam.day) + " tháng " + str(ngay_thang_nam.month) + " năm " + str(ngay_thang_nam.year)) 
