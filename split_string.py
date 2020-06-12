"""
Dzieli napis na listę liter co dwa. Jeśli ilość znaków jest nieparzysta, brakujący znak to podkreślnik
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
import re

def solution(s):
    # Rozwiązanie 1
    l = []
    if len(s) % 2 != 0:
        s += '_'
    for i in range(len(s)-1):
        if i %2 == 0:
            l.append(s[i] + s[i+1])
    return l

    # Rozwiązanie 2
    return re.findall(".{2}", s + "_")

print(solution('abc'))
print(solution('abcdef'))
print(solution(""))