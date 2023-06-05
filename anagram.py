def find_anagrams(words):
	anagrams={}
	for word in words:
		sorted_word=''.join(sorted(word))
		if sorted_word in anagrams:
			anagrams[sorted_word].add(word)
		else:
			anagrams[sorted_word]={word}
	return list(anagrams.values())
words= ['cat','dog','god','act','tac']
result=find_anagrams(words)
print(result)