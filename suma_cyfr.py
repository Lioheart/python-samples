# Zwraca sumę cyfr. Jeśli suma jest większa od 10, to zwraca sumę cyfr sumy.
# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6
def digital_root(n):
    while n>9:
        n=sum(map(int,str(n)))
    return n