# Sprawdza, czy z podanych boków można utworzyć trójkąt. Zwraca bool
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)