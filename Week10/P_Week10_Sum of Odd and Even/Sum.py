def sum_odd_and_even(num):
	a = [x for x in range(1,num+1) if x%2==1]
	b = [x for x in range(1,num+1) if x%2==0]
	return sum(a),sum(b)

n = int(input())
print(sum_odd_and_even(n))