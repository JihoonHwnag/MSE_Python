# Ture, False를 언급하지 않으면 True로 인식
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
# 위의 if문과 관련 X
print("5")
# 3, 5 출력됨