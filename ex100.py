data = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
# zip으로 data와 close_price를 묶은 후 이를 dict로 변경, 이를 close_table로 명명
close_table = dict(zip(data, close_price))
print(close_table)