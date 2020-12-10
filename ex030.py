string = 'abcd'
string.replace('b','B')
# replace('a','b') 메서드는 'a'를 'b'로 변경을 뜻함
# 하지만 'b'를 'B'로 변경한 이후 바인딩되지 않았기 때문에 메모리에서 사라짐
# 그렇기 때문에 'abcd' 그대로 출력
print(string)
