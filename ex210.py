# 'A'를 출력하는 message1
def message1():
    print("A")

# 'B'를 출력하는 message2
def message2():
    print("B")

def message3():

	# 3번 반복하는 i
    for i in range (3) :
	
		# 'B'를 출력하는 message2와 'C'를 출력
        message2()
        print("C")
	
	# 반복문이 끝난 후 'A'를 출력하는 message1
    message1()

message3()

# 예상 답: B C B C B C A 