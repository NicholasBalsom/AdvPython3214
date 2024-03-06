def this_recursion(t):
	if (t > 0):
		ans = t + this_recursion(t-1)
		print(ans)
	else:
		ans = 0
	return ans

print (f"\nRecursion Example Results\n{this_recursion(4)}")
 