# Sprawdza string z numerami pod kątem niepasujących wartości
# Na liście z parzystymi zwraca indeks numeru nieparzystego i odwrotnie
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1
    