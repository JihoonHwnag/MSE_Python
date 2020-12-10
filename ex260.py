# 클래서 OMG 정의
class OMG : 
	# 클래스 OMG 속 함수 print() 정의
    def print() :
        print("Oh my god")

mystock = OMG()
mystock.print()

# 클래스 OMG 안의 print() 함수에 인자가 없음
# 하지만 mystock.print()로 호출 시 파이썬에서는 OMG.print(mystock)으로 변경되어 호출
# OMG의 print 함수에는 인자가 없지만 변경되어 OMG.print(mystock)으로 호출하면 인자가 넘어오게 되어 오류 발생