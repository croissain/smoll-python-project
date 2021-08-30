"""
Cho 1 mảng đầu vào là A có n phần tử. Hãy viết 1 đoạn chương trình để put từng phần tử của mảng A vào 1 mảng trống là B với các tiêu chí của mảng B như sau:

sorted_by = ASC or DESC (các phần tử được sắp xếp theo thứ tự tăng dần hoặc giảm dần)
allow_dup = FALSE (các phần tử của mảng B không được trùng nhau)
add_way = SORTED_INS (phần tử mới được chèn theo thứ tự được quy định bởi sorted_by)
find_med = BINARY (dùng phương pháp tìm kiếm nhị phân để sắp xếp)

Ví dụ: Mảng A = [1, 3, 9, 6, 7, 2, 1], sắp xếp giảm dần (sorted_by = DESC)

Input:

2

1 3 9 6 7 2 1

Output:

9 7 6 3 2 1

Input Format

Dòng đầu tiên: cho biết thứ tự sắp xếp của mảng output B (1→ sorted_by = ASC, 2 → sorted_by = DESC)

Dòng thứ 2: là dãy các phần tử của mảng input A và mỗi phần tử cách nhau bằng khoảng trắng.

Constraints

0 < n < 100

Output Format

1 dòng: gồm các phần tử của mảng output B, mỗi phần tử cách nhau bằng khoảng trắng

Sample Input 0

2
1 3 9 6 7 2 1
Sample Output 0

9 7 6 3 2 1
"""

def print_arr(a):
	for i in a:
		print(str(i) + " ", end = '')

def allow_dup(a):
	for i in range (1, len(a)):
		for j in range (0, i):
			if a[i]==a[j]:
				for k in range (i, len(a)):
					a[k] = a[k+1]
				len(a) = len(a)-1
				i=i-1

def sorted_by_ASC(a):
	for i in range(0, len(a) - 1):
		for j in range (i + 1, len(a)):
			if a[i]>a[j]:
				a[i], a[j] = a[j], a[i]
	print("\nMảng tăng dần là:\n")
	print_arr(a)

def sorted_by_ASC(a):
	for i in range(0, len(a) - 1):
		for j in range (i + 1, len(a)):
			if a[i]<a[j]:
				a[i], a[j] = a[j], a[i]
	print("\nMảng giảm dần là:\n")
	print_arr(a)

a = [1,3,9,6,7,2,1]

allow_dup(a)
print_arr(a)
sorted_by_ASC(a)
