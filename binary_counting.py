"""
Przemienia liczbę na wartość binarną i zwraca sumę jedynek występującą w wartości binarnej
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""
def countBits(n):
    # szybsza metoda
    # return bin(n).count("1")
    final = 0
    for x in str(bin(n)):
        if x == '1':
            final += 1
    return final


print(countBits(1234))