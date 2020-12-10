# 초기값 설정
result = 1
# 반복문 설정 : i 값이 범위(1,11) 안에 있을때 반복, i의 초기값 = 1
for i in range(1,11):
	result *= i
# 조건을 만족하여 반복문이 끝났을때 마지막 바인딩된 result값 출력
print(result)