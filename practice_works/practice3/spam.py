import random

with open("spam.txt", "w", encoding='utf-8') as f:
    for i in range(10):
        for j in range(128):
            num = (i+j) + int(random.random()*100)
            print(num)
            sym = chr(num)
            if sym != '\n':
                f.write(sym)
