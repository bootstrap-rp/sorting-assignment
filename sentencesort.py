def sortSentence( s: str) -> str:
    
		
    word_list = sorted(s.split(), key = lambda word: word[-1], reverse = False)
    return " ".join([word[:-1] for word in word_list])  

print(sortSentence("is2 sentence4 This1 a3"))