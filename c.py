try:                         #Для отлова ошибок ввода
    a=int(input('Введите количество критериев '))
    ber=[]
    j=[]
    for i in range(1,a+1):   #Для подсчёта количества комбинаций чисел           
        for c in range(1,a+1):
            if i!=c and not([c,i] in ber):
                ber.append([i,c])
    for h in ber:               
        j.append(float(input(f'Задайте отношения критерия {h[0]} к {h[1]} ')))
except ValueError:                
    print('Введите числовые значения')
    quit()
v=[]
sums=0
for k in range(1,a+1):       #Для подсчёта весовых коэффициентов
    for n in range(len(ber)):
        if ber[n][0]==k: 
            sums+=j[n]
        elif ber[n][1]==k:
            sums+=1/j[n]
    sums+=1
    v.append(sums)
    sums=0
u=0
for l in v:                  # Для вывода значений 
    u+=1
    print(f"{u}: {l/sum(v):.2}")