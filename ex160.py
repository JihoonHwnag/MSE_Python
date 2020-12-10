리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for 변수 in 리스트:

	# 이름 name과 확장자 ext을 "."을 기점으로 분리 => split() 메서드 사용
	name,ext = 변수.split(".")
	
	# 분리한 확장자가 'h' 또는 'c'인지 판별
	if ext == 'h' or ext == 'c':
		print(변수)
		# name, ext 모두를 표현해야하므로, 조건이 성립할 때 이를 모두 바인딩하고 있는 '변수'를 출력