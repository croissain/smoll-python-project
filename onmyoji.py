import random, time
shiki = [("R - Huỳnh Thảo",79),("R - Sơn Đồng",79),("R - Thủ Vô",79),("R - Tọa Phu Đồng Tử",79),("R - Giác",79),("R - Thanh Oa Từ Khí",79),
		("R - Cổ Lung Hỏa",79),("R - Hồ Điệp Tinh",79),("R - Thiết Thử",79),("R - Sơn Thố",79),("R - Quản Hồ",79),("R - Tiêu Đồ",79),
		("R - Thực Phát Quỷ",79),("R - Độc Nhãn Tiểu Tăng",79),("R - Sửu Thì Chi Nữ",79),("R - Binh Dũng",79),("R - Khiêu Muội",79),
		("R - Khiêu Đệ",79),("R - Vũ Nữ",79),("R - Võ Sĩ Chi Linh",79),("R - Tam Vĩ Hồ",79),("R - Cổ Độc Sư",79),("R - Nha Thiên Cẩu",79),
		("R - Ngạ Quỷ",79),("R - Đồng Nữ",79),("R - Đồng Nam",79),("R - Hà Đồng",79),("R - Lý Ngư Tinh",79),("R - Ly Miêu",79),
		("R - Cửu Mệnh Miêu",79),("R - Trùng Sư",79),("R - Tiểu Tụ Chi Thủ",79),("R - Cấu Thường",79),
		("SR - Hạp Trung Thiếu Nữ",20),("SR - Dĩ Tân Chân Thiên",20),("SR - Trậm",20),("SR - Kim Ngư Cơ",20),("SR - Yên La La",20),
		("SR - Bạch Đồng Tử",20),("SR - Hắc Đồng Tử",20),("SR - Dạ Xoa",20),("SR - Thanh Phường Chủ",20),("SR - Bát Nhã",20),
		("SR - Anh Hoa Yêu",20),("SR - Lạc Tân Phụ",20),("SR - Huệ Bỉ Thọ",20),("SR - Hải Phường Chủ",20),("SR - Bạch Lang",20),
		("SR - Nhị Khẩu Nữ",20),("SR - Cô Hoạch Điểu",20),("SR - Liêm Dứu",20),("SR - Thanh Cơ",20),("SR - Thực Mông Mô",20),
		("SR - Yêu Cầm Sư",20),("SR - Yêu Hồ",20),("SR - Hấp Huyết Cơ",20),("SR - Hỏa Phụng Hoàng",20),("SR - Phán Quan",20),
		("SR - Khuyển Thần",20),("SR - Quỷ Sứ Hắc",20),("SR - Mạnh Bà",20),("SR - Đào Hoa Yêu",20),("SR - Khôi Lỗi Sư",20),
		("SR - Khiêu Huynh",20),("SR - Cốt Nữ",20),("SR - Quỷ Nữ Hồng Diệp",20),("SR - Quỷ Sứ Bạch",20),("SR - Tuyết Nữ",20),
		("SR - Hóa Kình",20),("SR - Nhất Phản Mộc Miên",20),("SR - Nhập Liệm Sư",20),("SR - Vu Cúc Trùng",20),("SR - Truy Nguyệt Thần",20),
		("SR - Nhật Hòa Phường",20),("SR - Bách Mục Quỷ",20),("SR - Thư Ông",20),("SR - Dịch",20),("SR - Huân",20),
		("SR - Miêu Chưởng Quỹ",20),("SR - Chỉ Vũ",20),("SR - Tinh Hùng Đồng Tử",20),("SR - Cửu Thứ Lương",20),("SR - Giải Cơ",20),
		("SR - Phong Ly",20),("SR - Yết Nữ",20),
		("SSR - Hoang",1),("SSR - Hoa Điểu Quyển",1),("SSR - Huy Dạ Cơ",1),("SSR - Yêu Đao Cơ",1),("SSR - Thanh Hằng Đăng",1),
		("SSR - Nhất Mục Liên",1),("SSR - Diêm Ma",1),("SSR - Hoang Xuyên Chi Chủ",1),("SSR - Tiểu Lộc Nam",1),("SSR - Tỳ Mộc Đồng Tử",1),
		("SSR - Tửu Thôn Đồng Tử",1),("SSR - Đại Thiên Cẩu",1),("SSR - Bát Kỳ Đại Xà",1),("SSR - Quỷ Thiết",1),("SSR - Diện Linh Khí",1),
		("SSR - Bạch Tàng Chủ",1),("SSR - Sơn Phong",1),("SSR - Bỉ Ngạn Hoa",1),("SSR - Tuyết Đồng Tử",1),("SSR - Ngọc Tảo Tiền",1),
		("SSR - Ngự Soạn Tân",1),("SSR - Quỷ Đồng Hoàn",1),("SSR - Duyên Kết Thần",1),("SSR - Vân Ngoại Kính",1),("SSR - Đại Nhạc Hoàn",1),
		("SSR - Bất Tri Hỏa",1),("SSR - Lang Dạ Xoa Cơ",1),("SSR - Linh Lộc Ngự Tiền",1),("SSR - Khẩn Na La",1),("SSR - Thiên Cơ",1),
		("SSR - Đế Thích Thiên",1), ("SSR - A Tu La",1),
		("SP - <Xích Ảnh> Yêu Đao Cơ",1),("SP - <Thương Phong> Nhất Mục Liên",1),("SP - <Tẫn Thiên> Ngọc Tảo Tiền",1),
		("SP - <Đạo Hà> Ngự Soạn Tân",1),("SP - <Ngự Oán> Bát Nhã",1),("SP - <Thiếu Vũ> Đại Thiên Cẩu",1),
		("SP - <Kiêu Lãng> Hoang Xuyên Chi Chủ",1),("SP - <Linh Hải> Kim Ngư Cơ",1),("SP - <Luyện Ngục> Tỳ Mộc Đồng Tử",1),
		("SP - <Quỷ Vương> Tửu Thôn Đồng Tử",1),("SP - <Thiên Kiếm Nhận Tâm> Quỷ Thiết",1),("SP - <Phù Thế> Thanh Hằng Đăng",1),
		("SP - <Phược Cốt> Thanh Cơ",1),("SP - <Lộc Minh> Đại Nhạc Hoàn",1),("SP -<Đãi Tiêu> Cô Hoạch Điểu",1),("SP - <Sơ Linh> Sơn Phong", 1),
		("SP - <Dạ Minh> Bỉ Ngạn Hoa", 1), ("SP - <Thiền Băng> Tuyết Nữ", 1), ("SP - <Không Tương> Diện Linh Khí",1)]

def same_rarity_R(sk):
	arr = []
	for i in sk:
		if i[0] == "R":
			arr.append(i)
	if len(arr) == 10:
		print ("THẬP R HỘI TỤ")
	else:
		print ("THẬP HỒN HỘI TỤ")


shiki_list = [x for x, y in shiki for i in range(y)]

shiki_temp = []

for i in range (0, 10):
	shiki_temp.append(random.choice(shiki_list))
for j in shiki_temp:
	time.sleep(0.5)
	print(j)

print ("\n")
same_rarity_R(shiki_temp)

print("\n")