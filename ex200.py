ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 총 수익금 초기값 설정
total_profit = 0

for day_price in ohlc[1:]:
	# 각 거래일 수익금: 종가 - 시가
    profit = (day_price[3] - day_price[0])
	# 총 수익금
	total_profit += profit