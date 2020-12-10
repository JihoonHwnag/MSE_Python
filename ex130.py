import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# btc 속 변동폭, 시가, 최고가, 최저가 불러오기
# 처음 불러온 값들은 문자열 타입이므로 산수 계산을 하기위해 숫자 관련 타입인 float으로 변경
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

# 상승장, 하락장을 출력하는 조건식 구성
if (시가 + 변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")