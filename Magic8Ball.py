import random

messages =['Tất nhiên là vậy rồi',
			'Nó đã được định sẵn như vậy rồi',
			'Không còn nghi ngờ gì nữa',
			'Chắn chắn là vậy rồi',
			'Bạn có thể tin tưởng điều đó',
			'Cũng gần như vậy',
			'Khả quan đấy',
			'Khá là mơ hồ, thử lại xem',
			'Hãy hỏi lại vào lần tới',
			'Tốt nhất là không nên nói với bạn lúc này',
			'Không thể tiên tri ngay bây giờ được',
			'Tập trung tư tưởng rồi hỏi lại lần nữa',
			'Đừng trông đợi gì nhiều',
			'Câu trả lời của tôi là "Không"',
			'Tôi tra Google thì nó nói "Đừng"',
			'Không mấy khả quan',
			'Rất đáng ngờ']

print('Hãy hỏi tôi 1 câu hỏi đúng/sai đi:\n')
answer = input()
print('Câu hỏi của bạn: ' + answer)
print('Lời tiên tri của tôi: ' + messages[random.randint(0, len(messages) - 1)])