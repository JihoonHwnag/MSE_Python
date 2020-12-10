fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과"}
# 질문 및 입력칸 제공
user = input("좋아하는 과일은?")
# 질문의 답이 fruit의 dict 속 values에 포함되어있다면 정답, 포함되어 있지않다면 오답 표기
if user in fruit.values():
	print("정답입니다.")
else:
	print("오답입니다.")