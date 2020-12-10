# 원소 a, b를 가진 my_print 함수 설정
def my_print (a, b) :
	# "왼쪽:"을 출력 후 a 출력
    print("왼쪽:", a)
	# "오른쪽:"을 출력 후 b 출력
    print("오른쪽:", b)

# a와 b의 자리가 바뀌었지만 변수를 지정하여 바인딩을 시켰기 때문에 자리와 상관없이 없음
my_print(b=100, a=200)

# 왼쪽: 200   오른쪽: 100 출력