# A palindrome is a word or a phrase or a number, that when reversed, stays the same.
# For example, the following sequences are palindromes : "azobi4amma4iboza" or "anna".
# But this time, we are not interested in words but numbers. A "number palindrome" is a number, that taken backwards, remains the same.
# For example, the numbers 1, 4224, 9999, 1221 are number palindromes.
# Implement a function, which given an integer computes if it's a palindrome.

def is_numeric_palindrome(n):
	digits = []
	i=0
	while n>0:
		digits.append(n%10)
		i+=1
		n=n//10
	i-=1
	j=0
	while j<i:
		if digits[i]!=digits[j]:
			return False
		j+=1
		i-=1
	return True

print is_numeric_palindrome(100001)