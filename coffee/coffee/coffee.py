import progressbar
import time
import os

while 0 == 0:
    while 0 == 0:
        print('Выберите кофе:\n1.Американо - 60р\n2.Латте - 80р\n3.Каппучино - 40р\n4.Экспрессо - 50р\n5.Двойной экспрессо - 70р\n6.Горячий шоколад - 60р')
        try:
            t = int(input())
        except ValueError:
            print("\n")
            continue
        break

    p = [60, 80, 40, 50, 70, 60]
    
    while t < 1 or t > 6:
        print("\nВведите число от одного до шести")
        t = int(input())
    while 0 == 0:
        print("\nВнесите " + str(p[t-1]) + " рублей")
        try:
            m = int(input())
        except ValueError:
            continue
        break

    if m < p[t-1]:
        while m < p[t-1]:
            if m < 0:
                print("\nИ как ты это сделал?")
                m -= m
            while 0 == 0:
                print("\nНедостаточно средств на балансе... Добавьте еще " + str(p[t-1] - m) + "р")
                try:
                    a = int(input())
                except ValueError:
                    continue
                break
            m += a

    print("\nТвой кофе уже готовится...\n")

    bar = progressbar.ProgressBar().start()

    for i in range(101):
        bar.update(i)
        time.sleep(0.02)
    bar.finish()

    if m > p[t-1]:
        print("\n\nБери свой кофе и сдачу не забудь! (" + str(m-p[t-1]) + "р)")
    else:
        print("\nЗабирай свой кофе!")
    time.sleep(3)
    os.system('cls')