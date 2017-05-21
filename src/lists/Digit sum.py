# Implement a program, which given an integer n, computes the sum of its digits.
# If a negative number is given, the function should work as if it was positive.
# For example, if n is 1325132435356, the digit's sum is 43. If n is -10, the sum is 1 + 0 = 1.
# In the test cases for this task we will have that -2^63 < n < 2^63.

def digit_sum(number):
	sum = 0
	number = abs(number)
	while number > 0:
		sum += number % 10
		number = number // 10
	return sum

print digit_sum(1325132435356)