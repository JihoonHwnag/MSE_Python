# 4) num * 2를 수행한 후 바인딩, 그 값을 return
def 함수0(num) :
    return num * 2
	
# 3) num + 2를 수행한 후 바인딩, 그 값을 가지고 함수0 실행 후 return
def 함수1(num) :
    return 함수0(num + 2)

# 2) num += 10을 수행한 후 바인딩, 그 값을 가지고 함수1 실행 후 return
def 함수2(num) :
    num = num + 10
    return 함수1(num)

# 1) 함수2 실행
c = 함수2(2)

# 5) 함수를 거친 후 return된 함수2(2) 값을 받은 c = '28' 출력
print(c)

