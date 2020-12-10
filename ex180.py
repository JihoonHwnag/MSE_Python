low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

# volatility를 리스트로 설정
volatility = []

# i의 범위 설정, len(low_prices) = 5이므로 range(5)로 표현 가능
for i in range(len(low_prices)) :
	# 반복문으로 구해진 값을 volatility에 추가하기 위해서 append() 매서드 사용
	volatility.append(high_prices[i] - low_prices[i])