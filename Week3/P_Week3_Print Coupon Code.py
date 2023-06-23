coupon_code = int(input("COUPON CODE: "))
first = coupon_code//100000
second = coupon_code%100000//100
third = coupon_code%100000%100
print(str(first)+"-"+str(second)+"-"+str(third))