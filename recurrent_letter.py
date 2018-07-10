# https://www.youtube.com/watch?v=GJdiM-muYqc

def firstRecurrentLetter(word):
	count_words = [0] * 256
	for sw in word:
		w = ord(sw)
		count_words[w] = count_words[w]+1
		if count_words[w]>1:
			return sw
	return None


word = "ABCA"
word = "BCABA"
word = "X"
print(firstRecurrentLetter(word))