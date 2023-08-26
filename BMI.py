mass = int( input('Введите ваш вес в кг: '))
height = int(input('Введите ваш рост в см: '))
height = height/100 #перевод в метры
def index(mass,height):
    index_mass = round(mass/(height**2)) #формула из Википедии
    print('Ваш индекс массы тела равен: ', index_mass)
index(mass,height)
#ну, какая уж получилась шкала. Вывода одной строкой, к сожелению не выходило
x=round(mass/(height**2))
l1=int(x)-14
l2=45-int(x)
x='|'
print(14, x, sep= ("=")*l1, end='')
print(x, 45, sep= ("=")*l2)