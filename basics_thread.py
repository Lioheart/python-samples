import threading
import time
import queue

def func(q,a):
    t = threading.currentThread()
    print(t.getName())
    print('Nowy wątek')
    time.sleep(1)
    print('w trakcie')
    time.sleep(1)
    print('Koniec wątku')
    q.put(1)

t = threading.currentThread()
print(t.getName())

# zwrot z funkcji w innym wątku
que = queue.Queue()

# Przypisanie funkcji do wątku i 4 do a
x = threading.Thread(target=func, args=(que, 4))
x.start()

# Sprawdzenie aktywnych wątków
print('Ilość wątków:',threading.activeCount())
time.sleep(1)
print(que.get())
print('Zakończenie Main')
