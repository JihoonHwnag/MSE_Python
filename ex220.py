# a, b, c 세 개의 원소를 가진 print_max 함수 정의
def print_max(a, b, c) :

	# if문 및 부등호를 사용하여 크기 비교
	if a > b and a > c:
		print(a)
	# 3개 이상의 조건이므로 elif 사용
	elif b > c and b > a:
		print(b)
	else:
		print(c)
