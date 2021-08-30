import pyperclip
text = pyperclip.paste()
shiki = text.split('", "')
for i in range(len(shiki)):
	shiki[i] = '("SSR - ' + shiki[i] +'",' + str(1) + ')'

	
text = ','.join(shiki)
pyperclip.copy(text)
input('Press enter to exit')

#("SSR - Hoang",1),("SSR - Hoa Điểu Quyển",1),("SSR - Huy Dạ Cơ",1),("SSR - Yêu Đao Cơ",1),("SSR - Thanh Hằng Đăng",1),("SSR - Nhất Mục Liên",1),("SSR - Diêm Ma",1),("SSR - Hoang Xuyên Chi Chủ",1),("SSR - Tiểu Lộc Nam",1),("SSR - Tỳ Mộc Đồng Tử",1),("SSR - Tửu Thôn Đồng Tử",1),("SSR - Đại Thiên Cẩu",1),("SSR - Bát Kỳ Đại Xà",1),("SSR - Quỷ Thiết",1),("SSR - Diện Linh Khí",1),("SSR - Bạch Tàng Chủ",1),("SSR - Sơn Phong",1),("SSR - Bỉ Ngạn Hoa",1),("SSR - Tuyết Đồng Tử",1),("SSR - Ngọc Tảo Tiền",1),("SSR - Ngự Soạn Tân",1),("SSR - Quỷ Đồng Hoàn",1),("SSR - Duyên Kết Thần",1),("SSR - Vân Ngoại Kính",1),("SSR - Đại Nhạc Hoàn",1),("SSR - Bất Tri Hỏa",1),("SSR - Lang Dạ Xoa Cơ",1)