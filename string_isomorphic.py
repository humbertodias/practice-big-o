def is_isomorphic(s,t):
	#1
	if len(s) != len(t): 
		return False
	
	length = len(s) #1

	char_map_s = [0] * length # n
	char_map_t = [0] * length # m
	
	# n-1
	for i in range(length-1):
		if s[i] == s[i+1]:
			char_map_s = 1
		if t[i] == t[i+1]:
			char_map_t = 1
	# 2n
	return char_map_s==char_map_t


#1+1 + 2n + n-1 + 2n
#2 + 5n -1
#1+ 5n

s = "egg"
t = "xdd"
print (is_isomorphic(s,t))