import progressbar
import time

print('Выберите кофе:\n1.Американо - 60р\n2.Латте - 80р\n3.Каппучино - 40р\n4.Экспрессо - 50р\n5.Двойной экспрессо - 70р\n6.Горячий шоколад - 60р')

t = int(input())

p = [60, 80, 40, 50, 70, 60]

n = []

if t < 1 or t > 6:
    print("Введите число от одного до шести")
else:
    print("Внесите " + str(p[t-1]) + " рублей")

m = int(input())


if m < p[t-1]:
    while m < p[t-1]:
        if m < 0:
            print("Сбагоюзить теперь не получится)")
            m -= m
        print("Мало деняк, дай еще " + str(p[t-1] - m) + " рублей")
        a = int(input())
        m += a

print("Твой кофе уже готовится...")

bar = progressbar.ProgressBar().start()

for i in range(101):
    bar.update(i)
    time.sleep(0.02)
bar.finish()

if m > p[t-1]:
    print("Бери свой кофе и сдачу не забудь (" + str(m-p[t-1]) + " рублей)")
else:
    print("Забирай свой кофе")
