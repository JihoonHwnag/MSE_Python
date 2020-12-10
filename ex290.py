class 부모:
    def __init__(self):
        print("부모생성")

# 부모 class를 상속받는 자식
class 자식(부모):
    def __init__(self):
        print("자식생성")
		# super 키워드를 통해 부모 class의 클래스 공간에 접근
        super().__init__()

# 자식 class의 객체 생성
나 = 자식()

# "자식생성" 출력 후 (super을 통해 명시적으로 부모 class에 접근하였기에) "부모생성" 출력