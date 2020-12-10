per = ["10.31", "", "8.00"]

for i in per:
	# 실행 코드
    try:
        print(float(i))
    # 예외가 발생했을 때 수행할 코드
	except:
        print(0)
	# 예외가 발생하지 않았을 때 수행할 코드
    else:
        print("clean data")
	# 예외 발생 여부와 상관없이 수행할 코드
    finally:
        print("변환 완료")
		
# 첫 번째 시행: 10.31	clean data 	변화 완료	출력 (예외가 존재하지 않기에 except를 제외하고 실행)
# 두 번째 시행: 0					변화 완료	출력 (수가 존재하지 않기에 except 실행 후 finally 실행)
# 세 번째 시행: 8.00		clean data	변화 완료	출력 (예외가 존재하지 않기에 except를 제외하고 실행)
