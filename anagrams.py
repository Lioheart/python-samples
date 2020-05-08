# Sprawdza, czy dane słowo jest anagramem innego słowa w liście 
# i zwraca listę słów, które są anagramem
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]